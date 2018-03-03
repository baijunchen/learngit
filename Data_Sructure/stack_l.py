import os
class StackUnderflow(AttributeError):
    def __init__(self,msg):
        self.msg = msg
class LNode():
    def __init__(self,elem,next_ = None):
        self.elem = elem
        self.next_ = next_
class LStack():
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top == None
    def push(self,val):
        self.top = LNode(val,self.top)
    def pop(self):
        if self.top == None:
            try :
                raise StackUnderflow("stack underflow")
            except StackUnderflow as e:
                print (e)
                os._exit(0)
        p = self.top
        self.top = p.next_
        return p.elem
    def topest(self):
        if self.top is None :
            try :
                raise StackUnderflow("stack is None")
            except StackUnderflow as e:
                print (e)
                os._exit(0)
        else :
            return self.top.elem


def main():
    st1 = LStack()
    list1 = [1,2]
    for num in list1 :
        st1.push(num)
    print (st1.pop())
    print (st1.pop())
    print (st1.topest())
main()