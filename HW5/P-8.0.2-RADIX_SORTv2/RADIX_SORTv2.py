#
# Created by Jiang Long 
#
# DKU CS301 FALL 2021 SESSION 02
#

import Stats, math, random

def RADIX_SORT(A, r, d):
    # d: number of digits
    # r: radix in number of r binary bits
    
    Stats.PrintArray(A, 'RADIX_SORT(A, 2^%d, %d)'% (r,d))
    
    # In each iteration of the COUNTING_SORT_on_radix, you should use
    # the following to print out the Array after the re-arrangement:
    
    # for i in range(d): 
    #    .... call COUNTING_SORT_on_radix
    #    Stats.PrintArray(A, 'iter %s'%i)
    
    # Complete the code here, see README on course website for problem description and instructions.

    for i in range(d):
        A = COUNTING_SORT_on_radix(A, r, i)
        Stats.PrintArray(A, 'iter %s'%i)

    return A


def COUNTING_SORT_on_radix(A, r, i_th):

    # r is the number of binary bits in the radix
    # i_th `digit`
    # return array B which is sorted on the i_th 'digit' base on radix 2^r

    # Complete the code here, see README on course website for problem description and instructions.


    k = 2 ** r  # Radix
    n = len(A)

    B = [0] * n  # Output array
    C = [0] * k  # Count array to store occurrences

    # Store count of occurrences in count array
    for num in A:
        digit = (num >> (r * i_th)) & (k - 1)  # Extract i_th digit from the right
        C[digit] += 1

    # Update count array to contain actual position of the digit in output array
    for i in range(1, k):
        C[i] += C[i - 1]

    # Build the output array
    for num in reversed(A):
        digit = (num >> (r * i_th)) & (k - 1)  # Extract i_th digit from the right
        B[C[digit] - 1] = num
        C[digit] -= 1

    return B


#-------------------------------------------
# Don't modify below this line
#-------------------------------------------
def main(A, r=4, d=3):
    
    # The default is radix 16 and total 3 hex digits

    Stats.Reset()
    n = len(A)

    B = RADIX_SORT(A, r, d)
    assert(list(sorted(B))==B)
    Stats.PrintArray(B, 'SORTED A')
    
    pass


if __name__=='__main__':
    A = [2,3,5,0,2,3,0,3]

    random.seed(len(A))
    A = [ int(random.uniform(512, 4096)) for i in range(10)]
    A = [329, 457,657, 839,436,720, 355]
    main(A)
    pass