class Solution1:
    def search(self, nums, target):
        l,r=0,len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if target == nums[mid]:    return mid

            elif target < nums[mid]:    r=mid-1 

            elif target > nums[mid]:    l=mid+1 
        
        return -1
    

class Solution2:
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid

            elif nums[l]<=nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid+1
                else:
                    r=mid-1

            else:
                if target < nums[mid] or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1

        return -1