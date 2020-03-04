#  匹配{[()]}   ( [ )]
# 每一个开始的符号被压入栈，等待匹配结果
# 当出现结束符号的时候，必须检查栈顶部的开始符号是什么类型，如果两个符号不匹配，则字符串不匹配
# 整个字符串处理完并且栈为空，则字符串匹配

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]

        if symbol in "([{":     # [{
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                top = s.pop()   # 栈中最顶部的元素
                start = '([{'   # 定义开括号顺序start和闭括号顺序end，判断pop出来的开括号在start中的下标 与 闭括号在end中的下标是否一致。
                end = ')]}'     # 一致则抵消，不一致则没有匹配到返回flase。

                if not start.index(top) == end.index(symbol):
                    flag = False
        index = index + 1 

    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChecker('{[()]}'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))




'''
十进制：由0,1,2,3,4,5,6·····组成
二进制：由0,1组成
十进制转换为二进制：除二法（除二取余，倒序排列，高位补零）
二进制转换为十进制：各个位分别与2^n相乘后相加（n：个位为0，十位为1，百位为2....）
使用"除2"算法，将输入的十进制数字转换成8位2进制数字
'''
# from pythonds.basic.stack import Stack

# def divide2(desNumber):
#     s = Stack()

#     while desNumber > 0:
#         rem = desNumber % 2   # 取余放入栈
#         s.push(rem)
#         desNumber = desNumber//2    # 取整
    
#     binString = ""
#     while not s.isEmpty():
#         binString = binString + str(s.pop())
    
#     return binString

# print(divide2(233))


'''
八进制，十六进制
'''
from pythonds.basic.stack import Stack

def divideBase(desNumber,base):
    digits = '0123456789ABCDEF'
    s = Stack()

    while desNumber > 0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base
    
    binString = ""
    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    
    return binString

print(divideBase(233,2))
print(divideBase(233,8))
print(divideBase(233,16))