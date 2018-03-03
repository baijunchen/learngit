import os
class StackUnderflow(AttributeError) :
    def __init__(self,msg):
        self.msg = msg

class SStack():
    def __init__(self):
        self.elem = []
    def isempty(self):
        return self.elem == []
    def push(self,elem_):
        self.elem.append(elem_)
    def top(self):
        if self.elem == []:
            try :
                raise StackUnderflow("stack is None")
            except StackUnderflow as e:
                print (e)
                os._exit(0)
        return self.elem[-1]
    def pop(self):
        if self.elem == [] :
            try:
                raise StackUnderflow("stack underflow")
            except StackUnderflow as e:
                print (e)
                os._exit(0)
        return self.elem.pop()
def main() :
    stack = SStack()
    for i in range(2) :
        stack.push(i)
    print (stack.pop())
    print (stack.pop())
    print (stack.pop())
main()