from bin.pivot import Pivot


# 可通信接口
class Associated:
    pivot = Pivot  # 通过控制中心 Pivot 实现对外联系
