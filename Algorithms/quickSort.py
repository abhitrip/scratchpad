class QuickSort():
    """
    Simple Algorithm to find QuickSort
    """

    def __init__(self,arr):
        self.array = arr

    def display(self):
        print self.array

    def partition(self,left,right,pivot):
        i = left
        j = right
        while True:
            while self.array[i]<pivot:
                i+=1
            while self.array[j]>pivot:
                j-=1
            if i>=j:
                break
            else:
                self.array[i],self.array[j] = self.array[j],self.array[i]
        return i

    def sort(self,left,right):
        if left >=right:
            return
        else:
            pivot = self.array[right]
            partitionIndex = self.partition(left,right,pivot)
            self.sort(left,partitionIndex-1)
            self.sort(partitionIndex+1,right)


if __name__=="__main__":
    arr = [4,6,3,2,1,9,7]
    obj = QuickSort(arr)
    obj.sort(0,len(arr)-1)
    obj.display()
