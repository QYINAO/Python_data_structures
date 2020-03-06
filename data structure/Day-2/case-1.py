import timeit
from timeit import Timer

# 测试pop
x = range(2000000)
pop_start = Timer("x.pop(0)","from __main__ import x")
print("pop_start ",pop_start.timeit(number=1000), "seconds")
x = range(2000000)
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_.23-end.timeit(number=1000), "seconds")

# ('pop_start ', 1.9101738929748535, 'seconds')
# ('pop_end ', 0.00023603439331054688, 'seconds')
