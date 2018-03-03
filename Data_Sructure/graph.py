import os
class ArgumentForGraph(AttributeError):
    def __init__(self,msg):
        self.msg = msg


class StackUnderflow(AttributeError) :
    def __init__(self,msg):
        self.msg = msg


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


class Graph:
    def __init__(self,mat,unconn=0):
        vnum = len(mat)
        for x in mat :
            if len(x) != vnum:#判断是否是一个方阵
                try:
                    raise ArgumentForGraph("Gragh is error")
                except ArgumentForGraph as e :
                    print (e)
                    os._exit(0)
        self.mat=[mat[i][:] for i in range(vnum)]
        self.vnum = vnum
        self.unconn = unconn
    def vertex_num(self):#返回行数和列数
        return self.vnum
    def invalid(self,v):
        return v>=0 and v<self.vnum
    def add_edge(self,vi,vj,val=1):
        if self.invalid(vi) and self.invalid(vj):
            self.mat[vi][vj] = val
        else:
            try:
                raise ArgumentForGraph("edge is not exit")
            except ArgumentForGraph as e:
                print (e)
                os._exit(0)
    def get_edge(self,vi,vj):
        if self.invalid(vi) and self.invalid(vj):
            return self.mat[vi][vj]
        else:
            try:
                raise ArgumentForGraph("edge is not exit")
            except ArgumentForGraph as e:
                print (e)
                os._exit(0)
    def out_edge(self,vi):
        if self.invalid(vi):
            return self._out_edge(self.mat[vi],self.unconn)
        else:
            try:
                raise ArgumentForGraph("edge is not exit")
            except ArgumentForGraph as e:
                print (e)
                os._exit(0)
    @staticmethod
    def _out_edge(row,unconn):
        edges=[]
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i,row[i]))
        return edges
    def DFS_graph(self,v0):
        vnum = self.vertex_num()
        visited = [0]*vnum
        visited[v0] = 1
        DFS_seq = [v0]
        st = SStack()
        st.push((0,self.out_edge(v0)))
        while not st.isempty():
            i,edges = st.pop()
            if i<len(edges):
                v,e=edges[i]
                st.push((i+1,edges))
                if not visited[v]:
                    DFS_seq.append(v)
                    visited[v] = 1
                    st.push((0,self.out_edge(v)))
        return DFS_seq
    def BFS_graph(self,v0):
        vnum = self.vertex_num()
        visited = [0]*vnum
        visited[v0] = 1
        BFS_seq = [v0]
        qu = SQueue()
        qu.enqueue((0,self.out_edge(v0)))
        while not qu.is_empty():
            i,edges = qu.dequeue()
            while i<len(edges):
                v,e = edges[i]
                i += 1
                if visited[v] == 0:
                    BFS_seq.append(v)
                    visited[v] = 1
                    qu.enqueue((0,self.out_edge(v)))
        return BFS_seq
    def Kruskal(self):
        vnum = self.vertex_num()
        mst,edges,doc = [],[],[]
        for vi in range(vnum):
            for v,w in self.out_edge(vi):
                edges.append((w,vi,v))
        edges.sort()
        for long,i,j in edges:
            if i not in doc or j not in doc:
                mst.append(((i,j),long))
                doc.append(i)
                doc.append(j)
        return mst
    def Prim(self,v0):
        doc=[v0]
        edges,mst=[],[]
        for vi in doc:
            for v,w in self.out_edge(vi):
                edges.append((w,vi,v))
            edges.sort()
            for long,i,j in edges:
                if j not in doc:
                    doc.append(j)
                    mst.append(((i,j),long))
                    break
        return mst


graph = [[100,1,5,4,2],[1,100,3,100,3],[5,3,100,7,100],[4,100,7,100,6],[2,3,100,6,100]]
tu = Graph(graph)
line = tu.Prim(0)
print (line)