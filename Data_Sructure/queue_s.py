import os
class QueueUnderflow(AttributeError) :
    def __init__(self,msg):
        self.msg = msg
class SQueue():
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
def main():
    queue = SQueue()
    for i in range(5) :
        queue.enqueue(i)
    print (queue.dequeue())
    print (queue.dequeue())
    queue.enqueue(6)
    print (queue.dequeue())
main()