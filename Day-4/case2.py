# class Deque:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def addFront(self, item):
#         self.items.append(item)

#     def addRear(self, item):
#         self.items.insert(0,item)

#     def removeFront(self):
#         return self.items.pop()

#     def removeRear(self):
#         return self.items.pop(0)

#     def size(self):
#         return len(self.items)

# from collections import deque
# 双端队列练习：判断输入的字符是不是：回文字符  
# 尾部  山西运煤车煤运西山  首部   
from pythonds.basic.deque import Deque

def palChecker(aString):
    chardeque = Deque()     # 队列
    for ch in aString:
        chardeque.addRear(ch)       # 遍历后添加到队列
    flag = True

    while chardeque.size() > 1 and flag:  
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:     # 两端取出的是否一致
            flag = False

    return flag

print(palChecker('山西运煤车煤运西山'))
print(palChecker('上海自来水来自海上'))
print(palChecker('python'))