def nextGreaterElementsBruteForce(self, nums):
    # time: O(n^2)
    # space: O(n)
    nums_next=[]
    for i in range(len(nums)):
        nums_next.append(-1)
        for j in range(i+1,i+len(nums)):
            if nums[j%len(nums)]>nums[i]:
                nums_next[-1]=nums[j%len(nums)]
                break

    return nums_next


def nextGreaterElements(self, nums):
    # time: O(n)
    # space: O(n)
    # Use a stack to keep track of the next max element.
    nums_next,stack=[-1]*len(nums),[]

    for i in range(2*len(nums)):
        index = i % len(nums)
        num = nums[index] 
        if not stack:
            stack.append([num, index])
        elif stack[-1][0] >= num:
            stack.append([num, index])
        else:
            while stack and stack[-1][0] < num:
                if nums_next[stack[-1][1]] == -1:
                    nums_next[stack[-1][1]] = num
                
                stack.pop()
            stack.append([num, index])
    
    return nums_next

