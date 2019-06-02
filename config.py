# -*- coding: utf-8 -*-

"""
@Author: lyzhang
@Date:
@Description: Global Configuration
"""
SEED = 7
POS_EMBED_SIZE = 50  # 46个
MLP_LAYERS = 1  # 隐层384的时候rel和nucl得到的输出高达1920单元
HIDDEN_SIZE = 256  # 针对ELMo大向量的情况: 256 - 384 - 512 - 640 - 768
USE_tracker = True
CROSS_GROUP_ID = 7
SAVE_MODEL = False  # 是否存储最好模型
USE_CUDA = True
CUDA_ID = 0
USE_DEV = False
USE_TD_error = True  # 是否在 offline用TD_error过滤
USE_DUELING = False
EDU_ENCODE_VERSION = 1  # 0: rnn mean, 1: word vector mean
MIX_RATE = 0.4  # 预学习的量

# === hyper-parameters
dropout = 0.2
l2_penalty = 1e-5
LR = 0.001
REWARD_DECAY = 0.9
E_GREEDY = 0.9
E_GREEDY_INCREMENT = None
BATCH_SIZE = 1
UPDATE_TRG_EPOCH = 7  # 隔17棵树更新一次target网络参数

# === static settings
TRAN_IN_SIZE = HIDDEN_SIZE
NR_IN_SIZE = HIDDEN_SIZE * 5 if USE_tracker else HIDDEN_SIZE * 4
EPOCH_ALL = 40.
SKIP_STEP = 20  # evaluate every 30 trees
MODEL_SAVED = "data/rl.model"
