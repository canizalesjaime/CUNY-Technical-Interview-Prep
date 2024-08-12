from disj_sets import DisjSets

class Solution:
    def numIslands(self, grid):
        pos, rows, cols = 0, len(grid), len(grid[0])
        num_islands=rows*cols
        ds = DisjSets(num_islands)

        # time complexity: O(rows*cols)
        # space complexity: O(rows*cols)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="0":
                    num_islands-=1

                else:
                    if grid[row][col-1]=="1" and col!=0:# to the left 
                        left=ds.find(pos-1)
                        ds.union(pos,left)
                        num_islands-=1
                    
                    if grid[row-1][col]=="1" and row!=0:#to the top
                        root_pos=ds.find(pos)
                        up=ds.find(pos-cols)
                        ds.union(root_pos,up)
                        if root_pos!=up:    num_islands-=1
                pos+=1
                                                                                                                                                                                                                                                                                  
        return num_islands