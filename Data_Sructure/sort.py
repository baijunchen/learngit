class Sort:
    def __init__(self,list):
        self.list = list
    def bubble_sort(self):
        #最坏情况下时间复杂度O(n^2),平均时间复杂度O(n^2),最好情况下时间复杂度O(n)
        #空间复杂度O(1),具有稳定性，具有适应性
        for i in range(len(self.list)-1):
            flag = True
            for j in range(len(self.list)-i-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j],self.list[j+1] = self.list[j+1],self.list[j]
                    flag = False
            if flag:
                break
    def select_sort(self):
        #最坏情况下时间复杂度O(n^2),平均时间复杂度O(n^2),最好情况下时间的复杂度O(n^2)
        #空间复杂度O(1),不具有稳定性，不具有适应性
        for i in range(len(self.list)-1) :
            min = i
            for j in range(i,len(self.list)):
                if self.list[j] < self.list[min]:
                    min = j
            if min!= i:
                self.list[min],self.list[i] = self.list[i],self.list[min]
    def insert_sort(self):
        #最坏情况下时间复杂度O(n^2),平均时间复杂度O(n^2),最好情况下时间复杂度O(n)
        #空间复杂度O(1),具有稳定性，具有适应性
        for i in range(1,len(self.list)):
            j=i
            x=self.list[i]
            while j>0 and x<self.list[j-1] :
                self.list[j]=self.list[j-1]
                j -= 1
            self.list[j] = x
    @staticmethod
    def partition(list,left,right):
        tem = list[left]
        while left < right :
            while left<right and tem<=list[right]:
                right -= 1
            list[left] = list[right]
            while left<right and tem>=list[left] :
                left += 1
            list[right] = list[left]
        list[left] = tem
        return left
    def quick_sort_x(self,left,right):#快速排序
        #最坏情况的时间复杂度O(n^2),平均时间复杂度O(nlogn),最好情况的时间复杂度O(nlog)
        #不具有稳定性，不具有适应性
        if left<right:
            mid = self.partition(self.list,left,right)
            self.quick_sort_x(left,mid-1)
            self.quick_sort_x(mid+1,right)


data = [5,3,9,0,1,4,12,76,45,21,90,5]
solution = Sort(data)
solution.quick_sort_x(0,len(data)-1)
print (data)