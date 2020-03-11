myTree = ['a',['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]],[]]]

print('左树：',myTree[1])
print('根节点：',myTree[0])
print("右树：",myTree[2])


'''
    抽象数据类型  ADT或者节点表示方式
'''
class Node(object):
    """节点类"""
    # elem为本身的值，lchild为左孩子，rchild为右孩子
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild