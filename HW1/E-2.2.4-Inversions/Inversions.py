import math
import tabulate
import Stats


def brute_inversion(A):
    # Complete the code here, see README on course website for problem description and instructions.
    ret = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                ret += 1
    return ret



def MERGE(A, p, q, r):
    # MERGE(A[p:q] with A[q:r]

    # Complete the code here, see README on course website for problem description and instructions.

    n1 = q - p 
    n2 = r - q

    L = [A[p + i] for i in range(n1)]
    R = [A[q + j ] for j in range(n2)]

    i = j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            Stats.Inc('inverse_cnt', q - p - i)
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
        Stats.Inc('r_inf_move_cnt')

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

    pass
   
def MERGE_SORT(A, p, r):
    # sort subarray A[p:r]
    # e.g. to sort A[:] use MERGE_SORT(A, 0, len(A))

    # Complete the code here, see README on course website for problem description and instructions.

    if r-p <= 1:
        return;

    mid = (r+p)//2
    MERGE_SORT(A, p, mid)
    MERGE_SORT(A, mid, r)
    MERGE(A, p, mid, r)

    return;




#-------------------------------------------
# Don't change code below this line
#-------------------------------------------
def main(A):
    Stats.PrintArray(A)
    Stats.Reset()
    Stats.Set('BruteForce_cnt', brute_inversion(A))
    MERGE_SORT(A, 0, len(A))
    n = len(A)
    Stats.PrintArray(A)
    Stats.PrintStats()

    return A
if __name__ == '__main__':

    A = [2,3,8,6,1]

#    A +=A

    main(A)