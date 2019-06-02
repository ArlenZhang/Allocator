# -*- coding: utf-8 -*-

"""
@Author: Lyzhang
@Date:
@Description:
"""
import numpy as np


class Provider:
    def __init__(self, name):
        self.state = np.random.randn(10)  # 假设用一维数组表示服务器状态
        self.name = name

    def get_state(self):
        return self.state

    def process_request(self, req):
        print("服务提供者" + self.name + "处理请求完成")
        self.state = np.random.randn(10)  # 因 python 不好模拟，用随机变化作为服务器状态变化
