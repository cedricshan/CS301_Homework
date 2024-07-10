# 
# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import random


recur_depth = 0        


def GetStatusLine0(A, p, r, tag):
    B = [ ''] * p + A[p:r] + [''] * (len(A)-r)
    B = ['%4s'%i for i in B]
    wspace = ' ' * 4
    s = ' '.join(B) + wspace + tag
    return s

def GetStatusLine(A, p, r, recur_depth, func_name):
    indent = ' ' * recur_depth *3
    f = '%s(A, %s, %s)' % (func_name, p, r)
    tag = indent + f + (' rdepth = %s'% recur_depth)
    return GetStatusLine0(A, p, r, tag)
    

def PARTITION(A, p, r):
    # Complete the code here, see README on course website for problem description and instructions.

    pivot = A[r-1]
    i = p - 1
    for j in range(p,r-1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r-1] = A[r-1], A[i+1]

    B = [' '] * len(A)
    B[i+1] = '#' + str(A[i+1])
    print(GetStatusLine(B, p,r,recur_depth, 'PARTITION'))
    return i + 1


def QUICKSORT(A, p, r):

    global recur_depth
    print(GetStatusLine(A, p,r,recur_depth, 'QUICKSORT'))
    recur_depth+=1
    # Complete the code here, see README on course website for problem description and instructions.

    if p < r - 1:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q)
        QUICKSORT(A, q + 1, r)
    recur_depth-=1
    return 0



#-----------------------------------------------------
# Don't modify below this line
#-----------------------------------------------------

def main(A):
    global show_detail
    show_detail = len(A)<20

    QUICKSORT(A, 0, len(A))

    print(GetStatusLine0(A, 0, len(A), "sorted"))

    assert A == list(sorted(A))
    pass

if __name__=='__main__':
    random.seed(1)
    A = list(range(10))
    random.shuffle(A)
    A = [2,8,7,1,3,5,6,4]
    main(A)
    pass