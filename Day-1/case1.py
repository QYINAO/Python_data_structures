'''问题描述：使用函数，求前n个整数的和'''

# 方法一
import time

def sumOfN(n):
    start_time = time.time()    # 开始
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    end_time = time.time()      # 结束
    return sum,end_time-start_time
# print("计算的结果是%d 需要%10.7f秒"%sumOfN(1000))

# 方法二：高斯函数
def sumOfN2(n):
    return (n*(n+1))/2
start_time = time.time()   # 开始
print(sumOfN2(10000000))
end_time = time.time()     # 结束
print(end_time-start_time)


# 结论：方法一随着需要处理的数增加，消耗时间也以相同的倍数增加；高斯函数不会因为处理数据的量而影响消耗的时间。
# 1. sumOfN()函数中，对执行的语句进行计数。
#    T(n) = 1 + n (n表示问题的规模)       T(n)是解决大小为n的问题所花费的时间，也就是1+n个步长
# 2. 数量级叫做“大O符号”，O(n)是T(n)的近似值
#    O(f(n))：计算机中实际步数的近似值   
#    sumOfN()的运行时间：O(n)


'''案例：
T(n) = 3*n^2 + 2n + 4
O(n^2)
'''

# a = 5    1
# b = 6    1
# c = 10   1

# for i in range(n):
#     for j in range(n):      3*n^2
#         x = i*i
#         y = j*j
#         z = i*j

# for k in range(n):   
#     w = a*k + 100     2n
#     v = b*b

# d = 300     1