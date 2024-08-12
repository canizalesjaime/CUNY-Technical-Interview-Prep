class MinHeap():
    def __init__(self, arr):
        self.arr=arr.copy()
        self.heapify()


    def percolateDown(self,hole):
        elem = self.arr[hole]
        while 2*hole < len(self.arr): #left child =2*hole of hole
            child=2*hole
            if child!=len(self.arr)-1 and self.arr[child] > self.arr[child+1]:
                child+=1

            if self.arr[child] < elem:
                self.arr[hole]=self.arr[child]
            else:
                break
            hole=child

        self.arr[hole]=elem


    # O(log(n))
    def deleteRoot(self):
        elem=self.arr[1]
        self.arr[1]=self.arr[-1]
        self.arr.pop()
        self.percolateDown(1)
        return elem


    # O(n)
    def heapify(self):
        self.arr.insert(0, None)
        for i in range(len(self.arr)//2,0,-1):  self.percolateDown(i)


    # O(log(n))
    def insert(self,elem):
        self.arr.append(elem)
        hole=len(self.arr)-1
        while(hole > 1 and elem < self.arr[hole//2]):
            self.arr[hole]=self.arr[hole//2]
            hole = hole//2
        self.arr[hole]=elem


    def __str__(self):
        return " ".join(map(str,self.arr))

        

###############################################################################
class MaxHeap():
    def __init__(self, arr):
        self.arr=arr.copy()
        self.heapify()


    def percolateDown(self,hole):
        elem = self.arr[hole]
        while 2*hole < len(self.arr):
            child=2*hole
            if child!=len(self.arr)-1 and self.arr[child] < self.arr[child+1]:
                child+=1

            if self.arr[child] > elem:
                self.arr[hole]=self.arr[child]
            else:
                break
            hole=child
            
        self.arr[hole]=elem


    def deleteRoot(self):
        elem=self.arr[1]
        self.arr[1]=self.arr[-1]
        self.arr.pop()
        self.percolateDown(1)
        return elem


    def heapify(self):
        self.arr.insert(0, None)
        for i in range(len(self.arr)//2,0,-1):  self.percolateDown(i)


    def insert(self,elem):
        self.arr.append(elem)
        hole=len(self.arr)-1
        while(hole > 1 and elem > self.arr[hole//2]):
            self.arr[hole]=self.arr[hole//2]
            hole = hole//2
        self.arr[hole]=elem


    def __str__(self):
        return " ".join(map(str,self.arr))