# 
# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import random, Stats,  math, os
import numpy as np


#------------------------------------------------
# Feel free to introduce helper functions.
#------------------------------------------------

def PARTITION(A, p, r):
    # copy this from your earlier JPA
    # Complete the code here, see README on course website for problem description and instructions.

    pivot = A[r-1]
    i = p - 1
    for j in range(p,r-1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r-1] = A[r-1], A[i+1]

    return i + 1



def PARTITION_modified(A, p, r,x ):

    #print("^^^^^^^^^^^^^^^^^^^^")
    #print(p)
    #print(r)
    
    # We know is the value of the pivot var, but we don't know where
    # it is, this for loop is to find its occurrence searching from
    # left to right of the list, and then call PARTITION
    
    # Complete the code here, see README on course website for problem description and instructions.

    for i in range(p, r):
        if A[i] == x:
            A[i], A[r - 1] = A[r - 1], A[i]
            break
    
    q = PARTITION(A, p, r)
    return q


recur_depth = 0

def lower_median(data):
    data = sorted(data)
    return data[len(data) // 2]

def SELECT(A, p, r, ith):

    # Note: the semantics is to return x = sorted(A)[ith]

    global recur_depth
    print( ' ' * recur_depth* 2 , 'SELECT( %s, %s)' % ( A[p:r], ith))

    recur_depth += 1

    # select the i_th from [p..r) , excluding position q
    # i starts with 0

    if r-p <=5 :
        assert ith<5
        sx = list(sorted(A[p:r]))
        recur_depth -=1
        return sx[ith]

    # Complete the code here, see README on course website for problem description and instructions.

    medians = []
    for i in range(p, r, 5):
        end = min(i + 5, r)
        data = list(A[i: end])
        median = lower_median(data)
        #print(median)
        #median = SELECT(A, i, end, (end - i) // 2)
        medians.append(int(median))

    pivot = SELECT(medians, 0, len(medians), len(medians) // 2)

    q = PARTITION_modified(A, p, r, pivot)  
    k = q - p  

    # print("p=",p)
    # print("r=",r)
    # print("q=",q)
    # print("k=",k)

    if ith == k:  
        recur_depth -=1
        return A[q]
    elif ith < k: 
        ret = SELECT(A, p, q, ith)
        recur_depth -= 1
        return ret
    else:  
        ret = SELECT(A, q + 1, r, ith - k - 1)
        recur_depth -= 1
        return ret



#--------------------------------------------------------------------
# Don't modify below this line
#--------------------------------------------------------------------
def main(A, i = None):
    global verbose
    verbose = len(A)< 20
    if i == None : i = len(A) //2 # pick the median

    Stats.Reset()
    n = len(A)
    Stats.Set('len(A)', n)
    Stats.Set('i', i)
    Stats.PrintArray(A, 'A (input)')
    
    B = SELECT(A, 0, len(A), i)


    Stats.Set('%s_{th} order-stats' % i, B)
    Stats.PrintStats()
    return B
    pass


#--------------------------------------------------------------------
# Ignore below, SAG judge execute SELECT.py from main.py
#--------------------------------------------------------------------
if __name__=='__main__':
    #A = [2,3,5,0,2,3,0,3]
    random.seed(0)
    A = list(range(22))
    random.shuffle(A)
    #A = [3, 1, 4, 2, 0, 5, 6, 9, 8, 7] 
    # A =  [1, 4, 3, 0, 2, 5, 6, 7, 8, 9, 10, 11, 19, 17, 20, 15, 13, 18, 12, 21, 14, 16] 
    # A =  [4, 5, 1, 6, 3, 0, 2, 7, 8, 9, 14, 10, 17, 21, 11, 19, 13, 12, 16, 20, 18, 15] 
    # A = [6, 7, 8, 3, 9, 1, 4, 2, 5, 0]
    main(A,9)
    for i in range(len(A)):
        #print('main', A, i)
        random.shuffle(A)
        main(A,i+len(A)//2)
        break
        pass
    pass