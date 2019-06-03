# Allocator
RL games between providers and consumers.


##################### Easy One

    基本理念：将 rate 分配问题转变成 rate 变化的游戏。初始 rate 即为游戏起点，有6个操作类型:
        0 rate_1++   1 rate_2++   2 rate_3++   3 rate_1--   4 rate_2--   5 rate_3--
    阶段1：状态改变——>反馈——>模型参数适应（泛化）——>RL模型
    阶段2：压力测试入口——>初始化分配比例——>RL模型编码当前状态和当前比例——>Action选择——>Rate根据action改变——>服务端分配
           ——>下一状态和比例（循环）
           速度不会变慢，只是矩阵运算


-- 阶段 1. 训练 --

./main.py 强化学习（Double DQN）训练入口

./module Java 框架，以简单 python 模拟

./model python 中间件，强化学习模型训练

-- 阶段 2. 压测（模型本身具备通用性，但是框架目前若能把 python 转 Java 或者 python 预训练的模型数据（简单看成有输入输出的函数）
可变成可运行脚本） --

./module/test.py 即为简单压力测试示意
