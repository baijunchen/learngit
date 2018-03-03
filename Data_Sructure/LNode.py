class LNode(object):
    def __init__(self,elem,next_ = None):
        self.elem = elem
        self.next_ = next_

class LinkList(object) :
    def __init__(self):
        self.head = 0
    def creatlist(self,data):
        if not data :return None
        self.head = LNode(data[0])
        p = self.head
        for num in data[1:] :
            p.next_ = LNode(num)
            p = p.next_
    def printlist(self):
        temp = self.head
        while temp != None :
            print (temp.elem)
            temp = temp.next_
    def getlong(self):
        iCount = 0
        temp = self.head
        while temp != None and self.head != 0 :
            iCount += 1
            temp = temp.next_
        return iCount
    def isempty(self):
        if not self.head:return True
        return False
    def clear(self):
        self.head = 0
    def append(self,num):
        temp = self.head
        while temp.next_ != None :
            temp = temp.next_
        p = LNode(num)
        temp.next_ = p
        p = None
    def insert(self,n,long,val):
        if n<1 or n>long :
            return False
        p = LNode(val)
        temp = self.head
        i = 0
        while i<n-1:
            i += 1
            temp = temp.next_
        p.next_ = temp.next_
        temp.next_ = p
    def delet(self,n,long):
        if n<1 or n>long :
            return False
        temp = self.head
        if n==1 :
            self.head = self.head.next_
        else:
            i = 0
            while i<n-2 :
                i += 1
                temp = temp.next_
            temp.next_ = temp.next_.next_
    def element(self):#定义一个生成器
        p = self.head
        while p is not None :
            yield p.elem
            p = p.next_
    def prepend(self,val):
        self.head = LinkList(val,self.head)

def main() :
    val = [1,2,3,4,5,6]
    LNodeList = LinkList()
    LNodeList.creatlist(val)
    for x in LNodeList.element():#迭代器，里面是对没个元素进行操作
        x = x + 1
        print (x)
main()
