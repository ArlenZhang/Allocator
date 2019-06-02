# -*- coding: utf-8 -*-

"""
@Author: Lyzhang
@Date:
@Description:
"""
import torch
from config import MODEL_SAVED
from module.controller import Controller


if __name__ == "__main__":
    model_pretrained = torch.load(MODEL_SAVED)
    controller = Controller(model_pretrained)
    # 一分钟压力测试（后期简化为输入输出即可衔接）
    begin_time, end_time = 0, 0
    while end_time-begin_time < 60:
        controller.consumer()
