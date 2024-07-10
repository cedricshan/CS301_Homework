import math, Stats

# Hint: 
#
#    Can use the following fmt_num and PrintPartArray function to
#    instrument MERGE_SORT

def fmt_num(n): return '%3s' % str(n)

def rprint(*s):
    print ('depth: %3d'% recur_depth, ' ' * recur_depth * 2 + ' '.join(map(str, s)))
    pass

recur_depth = 0 

def is_sorted(A):
    # A function to check if an array is sorted 

    # Complete the code here, see README on course website for problem description and instructions.
    n = len(A)
    for i in range(1, n):
        if A[i] < A[i - 1]:
            return False
    return True


def MERGE(A, B):
    # merge the two sorted arrays into one, and return it

    assert is_sorted(A)
    assert is_sorted(B)
    global recur_depth
    recur_depth += 1

    rprint(A,B, '  MERGE')

    # remember to do recur_depth-=1 before every return 

    # Complete the code here, see README on course website for problem description and instructions.

    if len(A) == 0:
        recur_depth-=1
        return B

    if len(B) == 0:
        recur_depth-=1
        return A

    if A[0] <= B[0]:
        ret =  [A[0]] + MERGE(A[1:], B)
    else:
        ret = [B[0]] + MERGE(A, B[1:])
    recur_depth-=1
    return ret



def MERGE_SORT(A):
    # recursive mergesort on A[:mid] and A[mid:] where mid=len(A)//2
    
    # return the sorted array, not need to sort in place as algo in
    # the textbook
    
    global recur_depth
    recur_depth += 1
    rprint(A, 'MERGE_SORT')
    
    # remember to do recur_depth-=1 before every return 

    # Complete the code here, see README on course website for problem description and instructions.

    mid = len(A)//2

    if len(A) <= 1:
        recur_depth -= 1
        return A

    A[:mid] = MERGE_SORT(A[:mid])
    A[mid:] = MERGE_SORT(A[mid:])
    A = MERGE(A[:mid], A[mid:])

    recur_depth -= 1
    return A


    
#-------------------------------------------
# Don't change code below this line
#-------------------------------------------
def main(A):
    Stats.PrintArray(A)
    assert not is_sorted(A)
    A = MERGE_SORT(A)
    assert is_sorted(A)
    Stats.PrintArray(A)
    n = len(A)
    Stats.Set (' %s*log_2(%s)'%(n,n), n*(math.log2(n)))
    Stats.PrintStats()
    return A
if __name__ == '__main__':

    A = [5,2,4,7,1,3,2,6 ] 


    main(A)

