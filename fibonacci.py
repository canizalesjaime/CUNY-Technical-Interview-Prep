# time: O(2^n)
# space: O(1)
def fib_recursive(n):
    if n==1 or n==2:    return 1
    return fib_recursive(n-1)+fib_recursive(n-2)

# time: O(n)
# space: O(n)
def fib_dynamic_programming1(n):
    dp=[1,1] # base cases
    for i in range(2,n):
        dp.append(dp[-1]+dp[-2])
    return dp[-1]

# time: O(n)
# space: O(1)
def fib_dynamic_programming2(n):
    prev,curr=1,1 # base cases
    for i in range(2,n):
        prev,curr=curr, prev+curr
    return curr


print(fib_recursive(8), fib_dynamic_programming1(8), fib_dynamic_programming2(8))