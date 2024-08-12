###############################################################################
def median3(l,r,nums):
    arr=sorted([nums[l], nums[r], nums[(l+r)//2]])#3log3
    nums[l], nums[r], nums[(l+r)//2]=arr[0], arr[1], arr[2]
    return nums[r]


###############################################################################
def sort_L_R(l,r,nums):
    temp=sorted(nums[l:r+1])
    for i in range(l,r+1):
        nums[i]=temp[i-l]


###############################################################################
def partition(l,r,nums):
    pivot=median3(l,r,nums)
    i,j=l,r-1
    while i<j:
        while nums[i]<pivot:    i+=1
        while nums[j]>pivot:    j-=1
        if (i<j):   nums[i],nums[j] = nums[j],nums[i]
    nums[r], nums[i]=nums[i], nums[r]
    return i


###############################################################################
def quikSort(l,r,nums):
    if r-l < 1:
        sort_L_R(l,r,nums)
        return
    
    part=partition(l,r,nums)

    quikSort(l,part-1,nums) #left partition
    quikSort(part+1,r,nums) #right partition


###############################################################################
def quikSelect(l,r,k,nums):
    if r-l < 1:
        sort_L_R(l,r,nums)
        return nums[k]
    
    part=partition(l,r,nums)

    if part==k:
        return nums[part]
    elif part>k:
        return quikSelect(l,part-1,k,nums) #left partition
    else:
        return quikSelect(part+1,r,k,nums) #right partition
    


###############################################################################
test=[40, 12, 33, 67, 42, -5, 55, 100, 6, 5, 11, 2, -100, 77, 45, 12, 13, 9, 
      -22, 31, 47, 22, 89, 72, 4, 7, 18, -54, 21, 30]

k=input("Enter kth value:")
print(quikSelect(0, len(test)-1, int(k), test))

# quikSort(0,len(test)-1,test)
# print(test)
