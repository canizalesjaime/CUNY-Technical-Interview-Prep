import random
import math

hired_employee=""
ranks=[]

# the random() function will return a number between 0 and 1. 
# It follows a uniform distribution.
# Multiplying the random() function by some value x, will increase the range 
# of the function. For example, random()*17 will generate random real numbers 
# between 0 and 17. 
# random()*x:           generates random numbers between 0 and x
# random()*x + start:   generates random numbers between start and x+start
# using the floor function you generate integers in the range (start,start+spread)
def rand(start, spread, real=False):
    rand_num=random.random()*spread + start
    if real:    return rand_num
    else:   return math.floor(rand_num)

    
# The total number of permutations of an array are n!. 
# [n,(n-1),(n-2),(n-3),...,1]: n*(n-1)*(n-2)*...*1=n!
# probalitiy of selecting a random permutation: 1/n!. This follows a 
# uniform distribution.
# sorted array: [1,2,3,4,...10] has 1/n! probability of occuring. Is the worst case. 
def randomizeArray(arr):
    for i in range(len(arr)):
        rand_index=math.floor(random.random()*len(arr)) 
        arr[rand_index], arr[i]= arr[i], arr[rand_index]


def interviewCandidate(spread):
    for i in range(1000):   pass #C_i
    return math.floor(random.random()*spread)


def hireCandidate(employee):
    for i in range(1000000):    pass #C_h
    global hired_employee
    hired_employee=employee


# An agency is sending you candidates and you want to hire the best candidate.
# As the candidates come in, you are willing to hire the best candidate you've
# seen thus far but it comes with a cost(call this cost C_h). C_i will be the 
# cost to interview a candidate. What is the average time complexity for 
# this problem?

# The worst case is obvious, and is O(C_i*n + C_h*n)

# average time: Using indicator random variables, we can show that the average
# runtime is O(C_i*n + C_h*ln|n|)
def offlineHiring(list_candidates):
    randomizeArray(list_candidates)
    best_candidate=0
    global ranks
    ranks=[]
    for i in range(len(list_candidates)):
        ranks[-1].append(interviewCandidate(len(list_candidates)))#cost of C_i
        if ranks[-1] > best_candidate:
            hireCandidate(list_candidates[i])
            best_candidate=ranks[-1]


# consider a variant of the hiring problem. Suppose now that
# we do not wish to interview all the candidates in order to find the best one. We
# also do not wish to hire and fire as we find better and better applicants. Instead, we
# are willing to settle for a candidate who is close to the best, in exchange for hiring
# exactly once. We must obey one company requirement: after each interview we
# must either immediately offer the position to the applicant or immediately reject the
# applicant. 
# 
# We wish to determine, for each possible value of k, the probability that we
# hire the most qualified applicant.
# worst case: O(C_i*n + C_h)
# average case: O(C_i*n +C_h)
def onlineHiring(k, list_candidates):
    randomizeArray(list_candidates)
    best_candidate = 0
    global ranks
    ranks=[]
    for i in range(k):
        ranks.append(interviewCandidate(len(list_candidates)))
        best_candidate = max(best_candidate,ranks[-1])

    for i in range(k,len(list_candidates)):
        ranks.append(interviewCandidate(len(list_candidates)))
        if ranks[-1] > best_candidate:
            hireCandidate(list_candidates[i])
            return 
    
    hireCandidate(list_candidates[-1])
        


###############################################################################
test = ["Adam","Jane","Steve","Caitlyn","James","Chris","Emily"]
#offlineHiring(test)
#print(hired_employee)


###############################################################################
onlineHiring(int(len(test)//2.718),test) #k == 2 
print(test)
print(hired_employee)

#look at what the rest of the interviews would have been
for i in range(len(test)-len(ranks)):
    ranks.append(interviewCandidate(len(test)))
print(ranks)