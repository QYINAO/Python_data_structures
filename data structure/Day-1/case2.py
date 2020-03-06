'''
乱序字符串:一个字符串只是另一个字符串的重新排列。
练习：
前提：字符串由26个小写字母集合组成，长度相同
比如：python 和 typhon      head 和 deah
目的：写一个布尔函数（返回值是布尔值的函数）
    solutions1('abcd','dbca')
'''

# 方法一：
# 穷举法：排除。原因：如果字符串过长，20个长度 20！

# 方法二：
# 检查： 第一个字符串是不是出现在第二个字符串中   O(n^2)

# def solutions1(s1,s2):
#     alist = list(s2)

#     pos1 = 0
#     flag = True
    
#     while flag and pos1 < len(s1):     # n
#         pos2 = 0
#         found = False
#         while pos2 < len(s2) and not found:  #  n   n^2
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1
        
#         if found:
#             alist[pos2] = None
#             pos1 = pos1 + 1
#         else:
#             flag = False

#     return flag


# print(solutions1('abcd','dbca'))
# print(solutions1('pythoa','typhon'))



# 方法三：
# 计数和比较法    aaaabbbbccccc  ccccaaaabbbb
# 思路：计算某个字符在两个字符串中出现的次数是否相同；用conunt记录相同的次数，
# 因为前提是26个字母组成，所以count小于26。

# 算法复杂度   T(n) = n+n+26 = 2n + 26    O(n)

def solutions2(s1,s2):
    # 分别给c1,c2初始长度26，用于记录26个字母的出现次数
    c1 = [0]*26  # 记录s1中字母出现的次数 [4,4,4,0,0,0,0,0....]
    c2 = [0]*26  # 记录s2中字母出现的次数 [4,4,4,0,0,0,0,0....]

    # ord()  返回的是字符在阿斯克码中的数字
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')   # 拿出s1中的每个字符与ord(a)相减，来判断当前字符是26个字母中的哪一个
        c1[pos] = c1[pos] + 1          # 顺带相减的值可以做下标来查询到c1中相应字母的位置，并对其加1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')   # 拿出s2中的每个字符与ord(a)相减，来判断当前字符是26个字母中的哪一个
        c2[pos] = c2[pos] + 1         # # 顺带相减的值可以做下标来查询到c1中相应字母的位置，并对其加1

    
    count = 0  # 如果某个字符在s1和s2中出现的次数相同，那么count+1
    flag = True

    while count < 26 and flag:
        if c1[count] == c2[count]:      # 如果c1和c2中每个对应位置的数都相同，则两字符串是乱序字符串。
            count = count + 1       #  26
        else:
            flag = False
    
    return flag


print(solutions2('aaaabbbbcccc','bbbbaaaacccc'))
print(solutions2('python','thonpy'))



# 方法四：
# 排序和比较:  即使s1,s2不同 它们都是由完全相同的字符组成的。
# 思路：从 a-z 排列每一个字符串，如果两个字符串相同，那这两个字符串就是乱序字符串
# aaaabbbbcccc    bbbbaaaacccc
# 算法的复杂度：不是  O(n)  而是O(n^2)

# def solutions3(s1,s2):
#     alist1 = list(s1)      # 转换为列表才能进行排序
#     alist2 = list(s2)

#     # 排序   排序通常复杂度 O(n^2)或者 O(logn)
#     alist1.sort()
#     alist2.sort()
    
#     flag = True
#     pos = 0
    
#     while pos < len(s1) and flag:    # 循环比较每个位置上的字符是否相同
#         if alist1[pos] == alist2[pos]:
#             pos = pos + 1                #  n
#         else:
#             flag = False
#     return flag


# print(solutions3('aaaabbbbcccc','bbbbaaaacccc'))
# print(solutions3('python','ythpna'))