# -*- coding: utf-8 -*-

"""
@Author: lyzhang
@Date: 2019.1.7
@Description: A novel RL learner with different scoring strategy.
"""
import torch
import random
import numpy as np
from config import *
import torch.nn as nn
from model.mlp import MLP
torch.manual_seed(SEED)
np.random.seed(SEED)
random.seed(SEED)


class RLModel(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
        self.score_state = MLP(input_size=TRAN_IN_SIZE, output_size=Transition_num, num_layers=MLP_LAYERS)
        self.score_state_trg = MLP(input_size=TRAN_IN_SIZE, output_size=Transition_num, num_layers=MLP_LAYERS)
        self.capture_rate = nn.Linear(TRAN_IN_SIZE, Transition_num)
        # 提高e-greedy的epsilon值，提高对模型的信任
        self.epsilon = 0 if E_GREEDY_INCREMENT is not None else E_GREEDY

    def update_trg_net(self):
        """ Update the parameters of the target Net every TE time.
        """
        self.score_tran_trg.load_state_dict(self.score_tran.state_dict())

    def forward(self, data_):
        """ 根据状态转移，比例分配情况，反馈信息计算网络的目标值和当前值。
        """
        state_before, rate_before, action, reward, state_next = data_
        indicator_ = self.capture_rate(rate_before)
        q_pred = self.score_state(state_before).squeeze(0) + indicator_
        q_real = (self.score_state_trg(state_next).squeeze(0) + indicator_).data.numpy()

        """ In double DQN, we use the newest parameters to compute the rates of Q real, the value of Q real still
            comes from the original parameters. In this way, the problem of Error Propagation is alleviated.
        """
        q_real_ = self.score_state(state_next).data.numpy()
        actions_idx = np.argmax(q_real_, axis=1)[0]
        q_next = q_real[actions_idx]

        q_target = q_pred.data.numpy().copy()
        q_target[action] = reward + REWARD_DECAY * q_next
        q_target = torch.FloatTensor(q_target)
        # We enlarge the value of e_greedy's epsilon to improve trust in our model but not random SEED.
        self.epsilon = self.epsilon + E_GREEDY_INCREMENT if self.epsilon < E_GREEDY else E_GREEDY
        return q_pred, q_target
