'''
In computer science, the time complexity is the computational complexity that describes the amount
of computer time it takes to run an algorithm.
There are many notations to compute time complexity but most of the time we use Big O

Types of analysis
    1. Experimental Analysis
    2. Theoratical Analysis
'''
# Experimental Analysis
import time

start = time.time()
l = [1,5,2,3,5,6,7]
duplicate = None # k1
for i in range(len(l)): #n
    for j in range(i+1,len(l)): #n
        if l[i] == l[j]:    # k3
            duplicate = l[i]    #k4

print("duplicate : ",duplicate)
end = time.time()
print("time : ",end-start)
'''
k + k1 + k2 + k3 + k4 + n^2 + n => n^2 => O(n^2)
Important rules
1. Drop non dominant terms
2. Drop the constant
'''