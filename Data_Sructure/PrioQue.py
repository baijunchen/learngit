import os
class QueueError(Exception):
    def __init__(self,msg):
        self.msg = msg
class PrioQue:
    def __init__(self,elist=[]):
        self.elems = list(elist)
        self.elems.sort(reverse=True)
    def enqueue(self,e):
        num = len(self.elems)-1
        while num>=0:
            if e<=self.elems[num]:
                break
            else:num -= 1
        self.elems.insert(num+1,e)
    def is_empty(self):
        return not self.elems
    def peek(self):
        if self.is_empty():
            try:
                raise QueueError("queue is empty")
            except QueueError as e :
                print (e)
                os._exit(0)
        return self.elems[-1]
    def dequeue(self):
        if self.is_empty():
            try:
                raise QueueError("queue is empty")
            except QueueError as e:
                print (e)
                os._exit(0)
        return self.elems.pop()


class PrioQueue :
    def __init__(self,elist=[]):
        self.elems = list(elist)
        if elist :
            self.buildheap()
    def is_empty(self):
        return not self.elems
    def peek(self):
        return self.elems[0]
    def enqueue(self,e):
        self.elems.append(None)
        self.siftup(e,len(self.elems)-1)
    def siftup(self,e,last):
        elems,i,j=self.elems,last,(last-1)//2
        while i>0 and e<elems[j] :
            elems[i] = elems[j]
            i,j = j,(j-1)//2
        elems[i] = e
    def deququ(self):
        e0 = self.elems[0]
        e = self.elems.pop()
        if len(self.elems) > 0:
            self.siftdown(e,0,len(self.elems))
        return e0
    def siftdown(self,e,begin,end):
        elems,i,j = self.elems,begin,begin*2+1
        while j < end:
            if j+1 <end and elems[j+1] <elems[j]:
                j += 1
            if e < elems[j] :
                break
            elems[i] = elems[j]
            i,j = j,2*j+1
        elems[i] = e
    def buildheap(self):
        end = len(self.elems)
        for i in range(end//2,-1,-1):
            self.siftdown(self.elems[i],i,end)
    def heap_sort(self):
        def siftdown(elems,e,begin,end):
            i,j = begin,begin*2+1
            while j <end:
                if j+1<end and elems[j+1]<elems[j]:
                    j+=1
                if e < elems[j]:
                    break
                elems[i] = elems[j]
                i,j = j,2*j+1
            elems[i] = e
        end = len(self.elems)
        for i in range(end//2,-1,-1):
            siftdown(self.elems,self.elems[i],i,end)
        for i in range((end-1),0,-1):
            e = self.elems[i]
            self.elems[i] = self.elems[0]
            siftdown(self.elems,e,0,i)
a = [4,6,1,9,0,12,87,-1,2,7]
LIST = PrioQueue(a)
#LIST.buildheap()
LIST.heap_sort()
print (LIST.elems)
