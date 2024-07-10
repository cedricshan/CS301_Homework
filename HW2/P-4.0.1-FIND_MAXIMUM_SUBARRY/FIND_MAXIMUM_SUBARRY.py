# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 


import math
import tabulate
from Stats import Stats

indent  = 0

def BruteForce(B):
    # Complete the code here, see README on course website for problem description and instructions.

    ret = -math.inf;
    for i in range(len(B)):
        sum = 0
        for j in range(len(B) - i):
            sum += B[i+j]
            ret = max(ret, sum)
    return ret
        



def FIND_MAXIMUM_SUBARRAY(A, low, high):

    global indent 
    indent +=2 
    print()

    """



    """ 
    # Complete the code here, see README on course website for problem description and instructions.
########################################################################################################################
    #print("^^^^^^^^^^^^")
    #print(low, high)
########################################################################################################################

    print(Stats.PrintArrayRange(A, low, high, []) + ' %s   FIND_MAXIMUM_SUBARRAY [%d:%d]' % (' '*(indent-2), low, high))

    if low == high - 1:
        print(Stats.PrintArrayRange(A, low, high, [low]) + ' %s   base-case return %d' % (' '*(indent-2), A[low]))
        indent -=2
        return (low, high, A[low])
    if low > high - 1:
        indent -= 2
        return (low, high, 0)
    mid = (low + high)//2
    (lft_l, rgt_l, max_l) = FIND_MAXIMUM_SUBARRAY(A, low, mid)
    (lft_r, rgt_r, max_r) = FIND_MAXIMUM_SUBARRAY(A, mid + 1, high)
    indent +=2
    (lft_mid, rgt_mid, max_mid) = FIND_MAX_CROSS_SUBARRAY(A, low, mid, high)

    max_sum = max(max_l, max_r, max_mid)

    if max_l == max_sum:
        lft = lft_l
        rgt = rgt_l
    elif max_r == max_sum:
        lft = lft_r
        rgt = rgt_r   
    elif max_mid == max_sum:
        lft = lft_mid
        rgt = rgt_mid

    print(Stats.PrintArrayRange(A, low, high, list(range(lft, rgt))) + ' %s   return %d -- FIND_MAXIMUM_SUBARRAY [%d:%d] '% (' '*(indent-2), max_sum, low, high))
    indent -= 4
    return (lft, rgt, max_sum)




def FIND_MAX_CROSS_SUBARRAY(A, low, mid, high): # must cross mid  
 
    print(Stats.PrintArrayRange(A, low, high, [mid]) + ' %s   FIND_MAX_CROSS_SUBARRAY %s %s %s '% (' '*(indent-2), low, high, mid))
    # Complete the code here, see README on course website for problem description and instructions.

    left_sum = -math.inf
    sum = 0

    left_max = mid

    for i in range(mid-1, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left_max = i

    right_sum = -math.inf
    sum = 0
    right_max = mid
    for j in range(mid + 1, high):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            right_max = j

    lft = mid
    rgt = mid
    
    if left_sum >  0:
        lft = left_max
    if right_sum > 0:
        rgt = right_max

    max_sum = max(A[mid], A[mid] + left_sum, A[mid] + right_sum, A[mid] + left_sum + right_sum)
    print(Stats.PrintArrayRange(A, lft, rgt+1, list(range(lft, rgt+1)), symbol = 'x') + ' %s   FIND_MAX_CROSS_SUBARRAY return %d' %(' '*(indent-2), max_sum))
    #print(Stats.PrintArrayRange(A, low, high, list(range(lft, rgt+1))) + ' return ')
    
    max_sum = max(A[mid], A[mid] + left_sum, A[mid] + right_sum, A[mid] + left_sum + right_sum)
    return (lft, rgt + 1, max_sum)

def Transform(A):
    ret = []
    for i in range (1, len(A)):
        ret.append(A[i] - A[i-1])
    return ret

def dash(msg, n=60):
    print()
    print('-'*n)
    print(msg)
    print('-'*n)
    pass

def main(A):
    dash('Original array')

    print(Stats.PrintArrayRange(A, 0, len(A)))

    Stats.Reset()
    dash('After transformation')
    B = Transform(A)

    print(Stats.PrintArrayRange(B, 0, len(B)))

########################################################################################################################
    #print("^^^^^^^^^^^^^^")
    #print(len(B))
########################################################################################################################
 
    dash('Solving for maximum subarray')
    u = FIND_MAXIMUM_SUBARRAY(B, 0, len(B))

########################################################################################################################
    #print("return :",u)
    #b = BruteForce(B)
    #print("return_2 :",b)
########################################################################################################################

    return u
    
if __name__ == '__main__':


    A='100 113 110 85 105 102 86 63 81 101 94 106 101 79 94 90 97'.split()
    
    A=list(map(int, A))
    B = Transform(A)
    
    a = main(A)

    dash('Divide and conquer result')
    print(a)
    b = BruteForce(B)
    dash('Brutforce result')
    print(b)

    assert (b==a)
    