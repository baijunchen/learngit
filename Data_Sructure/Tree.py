import os#引入os模块，在异常处理时终止程序
class QueueUnderflow(AttributeError) :#自定义一个异常类
    def __init__(self,msg):
        self.msg = msg
class SQueue():#队列类，在二叉树的按层遍历时用到
    def __init__(self,init_len = 8):
        self._len = init_len
        self._elem = [0] * init_len
        self._head = 0
        self._num = 0
        self._rear = 0
    def is_empty(self):
        return self._num == 0
    def peek(self):
        if self._num == 0:
            try :
                raise QueueUnderflow("Queue is None")
            except QueueUnderflow as e :
                print (e)
                os._exit(0)
        return self._elem[self._head]
    def dequeue(self):
        if self._num == 0:
            try:
                raise QueueUnderflow("Queue underflow")
            except QueueUnderflow as e:
                print (e)
                os._exit(0)
        e = self._elem[self._head]
        self._head = (self._head + 1)%self._len
        self._num -= 1
        return e
    def enqueue(self,e):
        if self._num == self._len :
            self._extend()
        #self._elem[(self._head+self._num)%self._len] = e
        self._num += 1
        self._elem[self._rear] = e
        self._rear = (self._rear + 1)%self._len
    def _extend(self):
        old_len = self._len
        self._len += 10
        new_elem = [0]*self._len
        for i in range(old_len) :
            new_elem[i] = self._elem[self._head]
            self._head = (self._head+1)%self._len
        self._head,self._elem = 0,new_elem
        "队列的类"
class BinTNode():
    def __init__(self,data,letf = None,right = None):
        self.data = data
        self.left = letf
        self.right = right


class BinTree :
    def __init__(self):
        self._root = None
        self.a = []
    def preorder_creat(self):#先序建立一棵二叉树
        val = input(">>>")
        node = BinTNode(val)
        if val != "#":
            node.left = self.preorder_creat()
            node.right = self.preorder_creat()
        return node
    def preorder(self,_node):#先序遍历一棵二叉树
        if _node.data is "#":return None
        self.a.append(_node.data)#print (_node.data)
        self.preorder(_node.left)
        self.preorder(_node.right)
    def midorder(self,_node):#中序遍历一棵二叉树
        if _node.data is "#":return None
        self.midorder(_node.left)
        print (_node.data)
        self.midorder(_node.right)
    def lastorder(self,_node):#后序遍历一棵二叉树
        if _node.data is "#":return None
        self.lastorder(_node.left)
        self.lastorder(_node.right)
        print (_node.data)
    def count_BiTree(self,_node):
        if _node.data is "#":
            return 0
        else:
            return 1+self.count_BiTree(_node.left)+\
                   self.count_BiTree(_node.right)
    def sum_BiTree(self,_node):
        if _node.data is "#" :
            return 0
        else:
            return int(_node.data) + self.sum_BiTree(_node.left) + \
                   self.sum_BiTree(_node.right)
    def level_order(self,_node):#层次遍历
        queue = SQueue()
        if _node.data is "#" :
            return None
        else:
            queue.enqueue(_node)
            while not queue.is_empty() :
                key = queue.dequeue()
                print (key.data)
                if key.left.data is not "#":
                    queue.enqueue(key.left)
                if key.right.data is not "#":
                    queue.enqueue(key.right)

tree = BinTree()
tree._root = tree.preorder_creat()
tree.preorder(tree._root)
print (tree.a)
