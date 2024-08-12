def totalFruit(fruits):
    map_fruits={} # {fruit num, count}
    l, ans=0,0

    for r in range(len(fruits)):
        map_fruits[fruits[r]]=map_fruits.get(fruits[r],0)+1

        while len(map_fruits) > 2:
            map_fruits[fruits[l]]-=1
            if map_fruits[fruits[l]]==0:    map_fruits.pop(fruits[l])
            l+=1
        
        ans=max(ans,r-l+1)

    return ans 
