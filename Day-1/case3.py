# 拼接
def test1():
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]

# append方式
def test2():
    list1 = []
    for i in range(1000):
        list1.append(i)

# 列表的推导式
def test3():
    list1 = [i for i in range(1000)]


def test4():
    list1 = list(range(1000))

# 测试执行速度的模块 Timer
from timeit import Timer