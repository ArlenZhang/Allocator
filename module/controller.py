# -*- coding: utf-8 -*-

"""
@Author: Lyzhang
@Date:
@Description:
"""
from module.provider import Provider


class Controller:
    def __init__(self, model):
        self.pvd1, self.pvd2, self.pvd3 = Provider("pvd_1"), Provider("pvd_2"), Provider("pvd_3")
        self.rl_model = model
        self.rate_allocate_before = [1, 3, 5]  # 初始化分配比重，类似游戏起点
        self.rate_allocate = [1, 3, 5]  # 初始化分配比重，类似游戏起点

    def process_begin(self):
        while True:
            yield self.consumer()

    def consumer(self):
        print("消费者发出 1024 个请求...")
        requests = range(1024)
        # 调用 controller 进行比例计算
        return self.allocate(requests, self.rl_model)

    def action2rate(self, action):
        rate_ = (action + 1) * 0.1 if action <= 2 else (action - 2) * (-0.1)
        rate_other = (rate_ / 2) * (-1)
        tmp_rate_allocate = self.rate_allocate[:]
        if action in [0, 3]:
            tmp_rate_allocate[0] += rate_
            tmp_rate_allocate[1] += rate_other
            tmp_rate_allocate[2] += rate_other
        elif action in [1, 4]:
            tmp_rate_allocate[0] += rate_other
            tmp_rate_allocate[1] += rate_
            tmp_rate_allocate[2] += rate_other
        else:
            tmp_rate_allocate[0] += rate_other
            tmp_rate_allocate[1] += rate_other
            tmp_rate_allocate[2] += rate_
        return tmp_rate_allocate

    def allocate(self, requests):
        print("请求来了，计算分配比例")
        states = (self.pvd1.get_state(), self.pvd2.get_state(), self.pvd3.get_state())
        action = self.rl_model(states)
        tmp_rate_allocate = self.action2rate(action)
        states_after = self.rate2request(requests, tmp_rate_allocate)
        self.rate_allocate_before = self.rate_allocate[:]
        self.rate_allocate = tmp_rate_allocate[:]
        return states, self.rate_allocate_before, action, states_after

    @staticmethod
    def rate2request(requests, rates):
        """ 简写：请求按比例分配
        """
        return "part_a", "part_b", "part_c"
