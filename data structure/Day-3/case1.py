# 栈抽象数据类型的底层实现采用什么？   list
# 通过确定列表的哪一端是顶部，然后使用append和pop来实现操作

# 栈有以下操作：
# - Stack()创建一个空的新栈。它不需要参数，并返回一个空栈
# - push(item)将一个新项添加到栈的顶部，它需要item做参数并不返回任何内容
# - pop()从栈中删除顶部项。它不需要参数并返回item。栈被修改
# - peek()从栈返回顶部项，但不会删除它。不需要参数。不修改栈（因为栈后进先出的特性，即返回新添加的项）
# - isEmpty() 测试栈是否为空。不需要参数，返回布尔值
# - size()返回栈中的item数量。不需要参数，返回一个整数

# 假设列表的尾部是栈的顶部元素，push(添加)
# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):        # 测试是否为空
#         return self.items == []
    
#     def push(self,item):      # 在顶部添加
#         self.items.append(item)

#     def pop(self):            # 删除顶部项
#         return self.items.pop()
    
#     def peek(self):           # 返回顶部项
#         return self.items[len(self.items)-1]
    
#     def size(self):           # 大小
#         return len(self.items)



# pythonds模块测试
# from pythonds.basic.stack import Stack

# s = Stack()   

# print(s.isEmpty())    # 测试是否为空
# s.push(4)             # 添加
# s.push('lalla')

# print(s.peek())       # 返回顶部项

# s.push(True)

# print(s.size())        # 大小

# print(s.isEmpty())

# s.push(10.9)
# print(s.pop())
# print(s.pop())
# print(s.size())



# （）匹配
from pythonds.basic.stack import Stack

#  symbolString  假设 “（（））”
# 思路：index小于symbolString的长度且不为空时；
# 如果获是“(”就添加到栈中，否则判栈是否为空，不为空把栈的顶部项删除，为空则退出循环。
# 简单说就是一个“(”和一个“)”抵消，如果正好抵消为True。（利用了栈后进先出的特性）

def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                s.pop()

        index = index + 1

    if flag and s.isEmpty():
        return True
    else:
        return False


print(parChecker('(())'))
print(parChecker('((())'))
