import tabulate
import Stats, random

def rprint(*s):
    print ('depth: %3d'% recur_depth, ' ' * recur_depth * 2 + ' '.join(map(str, s)))
    pass

def is_sorted(A):
    # A function to check if an array is sorted 

    # Complete the code here, see README on course website for problem description and instructions.
    n = len(A)
    for i in range(1, n):
        if A[i] < A[i - 1]:
            return False
    return True


recur_depth = 0 
def IIP(A, i):
    # insert in place A[i] into A[0:i] (exclusive i)
    
    global recur_depth 
    recur_depth += 1

    rprint(A, '  i=', i, '  IIP')

    
    # remember to do `recur_depth-=1` before every return statement
    
    # Complete the code here, see README on course website for problem description and instructions.
    
    if i > 0 and A[i] < A[i-1]:
        A[i], A[i-1] = A[i-1], A[i]
        Stats.Inc('swapcnt')
        IIP(A, i-1)
    
    if i > 0:
        Stats.Inc('cmpcnt')
    recur_depth -= 1



def INSERTION_SORT_r(A, r):

    global recur_depth 
    recur_depth += 1

    rprint(A, '  r=', r, '  INSERTION_SORT_r')    
    # remember to do `recur_depth-=1` before every return statement
    
    # Complete the code here, see README on course website for problem description and instructions.
    if r > 1:
        INSERTION_SORT_r(A, r-1)
        IIP(A, r-1)

    recur_depth -= 1
    return A

def main(A):
    Stats.Reset()
    Stats.PrintArray(A, "input ")
    B  = [i for i in A]
    random.shuffle(B)
    assert not is_sorted(B)
    A = INSERTION_SORT_r(A, len(A))
    assert  is_sorted(A)
    Stats.PrintArray(A, "sorted")
    Stats.PrintStats()
    return A
if __name__ == '__main__':

    A = [5,2,4,6,1,3]
    
    main(A)
    

    