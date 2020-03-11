'''
    归并排序     先拆分再合并
'''
# def mergeSort(alist):
#     print('拆分的列表',alist)
#     if len(alist) > 1:
#         mid = len(alist)//2    # 中间位置
#         leftHalf = alist[:mid]  # 拆分后左半部分
#         rightHalf = alist[mid:]  # 拆分后右半部分

#         mergeSort(leftHalf)     # 递归拆分
#         mergeSort(rightHalf)

#         i = 0   # 左列表下标
#         j = 0   # 右列表下标
#         k = 0   # 新列表下标
#         while i < len(leftHalf) and j < len(rightHalf):    
#             if leftHalf[i] < rightHalf[j]:    # 左右元素比较大小，小的放入新列表
#                 alist[k] = leftHalf[i]
#                 i = i + 1
#             else:                            
#                 alist[k] = rightHalf[j]
#                 j = j + 1
#             k = k + 1
    
#         while i < len(leftHalf):           # 大的放入列表
#             alist[k] = leftHalf[i]
#             i = i + 1
#             k = k + 1
#         while j < len(rightHalf):
#             alist[k] = rightHalf[j]
#             j = j + 1
#             k = k + 1
#     print('合并：',alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


'''
    快速排序
'''
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

# 递归调用对数列进行分区
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)   # 递归不断选择分区点

        quickSortHelper(alist,first,splitpoint-1)   # 左队列
        quickSortHelper(alist,splitpoint+1,last)    # 右队列

# 选出基准点
def partition(alist,first,last):
    # 定义基准点
    pivotvalue = alist[first]

    leftMark = first + 1
    rightMark = last

    # 停止比对
    done = False
    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivotvalue:    # 从左往右
            leftMark = leftMark + 1

        while alist[rightMark] >= pivotvalue and rightMark >= leftMark:   # 从右往左
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:                            
            temp = alist[leftMark]   
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp

    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark     

alist =  [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)