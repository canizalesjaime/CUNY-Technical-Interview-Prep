from disj_sets import DisjSets #detect cycles
import heapq #get the minimum edge


###############################################################################
class edge:
    def __init__(self,u,v,weight):
        self.u=u
        self.v=v
        self.weight=weight

    # for heap comparison
    def __lt__(self, other): 
        return self.weight < other.weight

    # for printing 
    def __str__(self):
        return "u: {0} v: {1} weight: {2} ".format(self.u,self.v,self.weight)


###############################################################################
# V is the set of vertices, and E is the set of edges
# time complexity: O(|V| log(|E|))
# space complexity: O(V)
# example of a greedy algorithm
def kruskal(edges,num_vertices):
    ds=DisjSets(num_vertices)
    pq=edges.copy()
    heapq.heapify(pq) # create a minheap from the set of edges
    mst=[]#minimum spanning tree
    # minimum spanning trees always have one less edge than vertices
    while len(mst)!= num_vertices-2: # O(|V|)
        e=heapq.heappop(pq)  # Edge e = (u, v) is the minimum weight edge; O(log(|E|))
        uset = ds.find(e.u) #O(1) 
        vset = ds.find(e.v) #O(1)
        if uset != vset: # Accept the edge
            mst.append(e)
            ds.union(uset, vset)
        
    return mst # return set of edges


###############################################################################
num_vertices = 8 #nodes from 1 to 7
#bidirected edges
# count: 12 edges
edges=[edge(1,2,2),edge(1,3,4),edge(1,4,1),
       edge(2,4,3),edge(2,7,10),
       edge(3,4,2),edge(3,6,5),
       edge(4,5,7),edge(4,6,8),edge(4,7,4),
       edge(5,7,6),
       edge(6,7,1)] 

# verify: minimum spanning trees always have one less edge than vertices!
mst=kruskal(edges,num_vertices)
for edge in mst:  print(edge)