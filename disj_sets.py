class DisjSets:
    def __init__(self, num_elements):
        self.array=[]
        for i in range(num_elements):
            self.array.append(-1)

    
    def union(self, root1, root2): #union by size
        if root1!=root2:
            if self.array[root1] <= self.array[root2]:
                self.array[root1] += self.array[root2]
                self.array[root2]=root1
            
            else:
                self.array[root2] += self.array[root1]
                self.array[root1]=root2

    
    def find(self, x): #with path compression
        if self.array[x] < 0:   return x
        else:   
            self.array[x] = self.find(self.array[x])
            return self.array[x]
        

###############################################################################
def test():
    trees=DisjSets(11)

    trees.union(3,1)
    trees.union(3,2)
    trees.union(3,4)
    trees.union(3,5)

    trees.union(9,6)
    trees.union(9,8)
    trees.union(9,7)

    print(trees.array)

#test()