import random
class Median():
    """docstring for Medins"""
    def __init__(self, arr):
        self.arr = arr
        self.medIdx = -1
    def display(self):
        print self.arr[self.medIdx]

    def partition(self,left,right,pivot):
        i = left
        j = right
        while True:
            while self.arr[i]<pivot:
                i+=1
            while  self.arr[j]>pivot:
                j-=1
            if i<=j:
                break
            else:
                self.arr[i],self.arr[j] = self.arr[j],self.arr[i]
        return i

    def medianOfMedians(self,array,ith):
        arrayLen = len(array)
        pvt = random
