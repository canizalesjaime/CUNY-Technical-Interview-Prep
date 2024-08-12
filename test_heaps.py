from heaps import *


###############################################################################
class TestObj:
    def __init__(self,num,name):
        self.num=num
        self.name=name
 

    # for heap comparison: over for less than operator
    def __lt__(self, other): 
        return self.num < other.num
    

    def __str__(self):
        return "("+str(self.num) + ", " + self.name+")"



###############################################################################
# arr1=[10,9,8,715,1,3,15]
# arr1_heap=MinHeap(arr1)
# print(arr1)
# print(arr1_heap)


arr2=[TestObj(1,"J"), TestObj(9,"I"),TestObj(6,"M"),TestObj(3,"B"),TestObj(2,"O"),
      TestObj(11,"F"), TestObj(98,"R"),TestObj(5,"A"),TestObj(111,"N"),TestObj(0,"C"), TestObj(987,"E")]
arr2_heap=MaxHeap(arr2)
for elem in arr2:   print(elem,end="")
print()
print(arr2_heap)
