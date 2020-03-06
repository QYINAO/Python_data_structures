''' [1,3,5,7,9] 求列表中元素的和'''
# 遍历求和
# def listSum(numList):
#     sum = 0
#     for i in numList:
#         sum = sum + i
    
#     return sum 

# print(listSum([1,3,5,7,9]))


#  不能使用while或者for，使用小学的内容：连加
# （1+（3+（5+（7+9））））第四个数 + 后面所有数的和
#     （1+（3+（5+16））） 第三个数 + 后面所有数的和
#          （1+（3+21）） 第二个数 + 后面所有数的和
#               （1+24） 第一个数 + 后面所有数的和
#                   25

'''
    listSum2([1,3,5,7,9]) 
  = 1 + listSum2([3,5,7,9])
  = 3 + listSum2([5,7,9])
  = 5 + listSum2([7,9])
  = 7 + listSum2([9])
'''
# def listSum2(numList):  # 递归函数：调用自身的函数
#     if len(numList) == 1:
#         return numList[0]     # 只有一个数直接返回
#     else:
#         return numList[0] + listSum2(numList[1:])  

# print(listSum2([1,3,5,7,9]))



# 递归实现整数转换成任意进制字符串
# 思路：如769转为10进制，769/10 得76 余9
                       # 76/10 的7  余6
                    #    结果为7 6 9
                    # 结论：整数n不断对进制base取模，直到n<base时结束
# def toStr(n,base):  
#     str1 = '0123456789ABCDEF'      
#     # 比如0，1 < 2 
#     if n < base:            
#         return str1[n]
#     else:
#         return toStr(n//base,base) + str1[n%base]
#               # 对n取模，进行下次递归      对n取余记录为字符串

# print(toStr(1453,16))          # n是要转换的数，base是进制

'''
   toStr(10,10) + '0'
   toStr(1,10) + '0'
   '1'
'''


# 用循环和递归分别求 10！（阶乘）
#循环完成
def product1(num):
    product=1
    for i in range(1,num+1):
        product=product * i
    return product
print(product1(10))
 
#递归完成
def product2(num):
    if num==1:
        return 1
    else:
        return num * product2(num-1)
print(product2(10))






# 栈 实现递归
from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = '0123456789ABCDEF'

    while n > 0:                 
        if n < base:         # 小于进制压入栈，大于则取余压入栈
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])   
        
        n = n // base     # 对n取模并重新赋值，进行下次循环（递归）
    
    res = ""
    while not rStack.isEmpty():   # 栈不为空，则移除栈内的数，并将该数转为字符串与res拼接
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))

''' [0]
    100   0
    10    0

'''