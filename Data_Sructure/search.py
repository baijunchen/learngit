class Search:
    def __init__(self,list):
        self.list = list
    def bin_search(self,val):#二分查找的时间复杂度 O(logn)
        low = 0
        high = len(self.list)
        while low<=high:
            mid = (low+high)//2
            if self.list[mid] == val:
                return mid
            elif self.list[mid] < val:
                low = mid+1
            else:
                high = mid-1
        return None
data=[1,3,4,6,7,8,12]
list_ = Search(data)
index = list_.bin_search(8)
print (index)