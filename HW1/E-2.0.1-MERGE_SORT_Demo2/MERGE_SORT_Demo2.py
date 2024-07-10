import math, Stats

# Hint: 
#
#    Can use the following fmt_num and PrintPartArray function to
#    instrument MERGE_SORT

def fmt_num(n): return '%3s' % str(n)

def PrintPartArray(A, p, q, tag=''  ):
    r = [''] * p + A[p:q] + ['']* (len(A) -q)
    r =  ' '.join(map(fmt_num, r)) + '    ' + tag
    print(r)
    return r

def MERGE(A, p, q, r):
        
    # MERGE(A[p:q] with A[q:r]

    # Complete the code here, see README on course website for problem description and instructions.

    # PrintPartArray(A, p, q, '*')

    ok_print = 0
    if p == 0 and r == len(A):
        ok_print = 1
        list_prt = list(A)


    n1 = q - p 
    n2 = r - q

    L = [A[p + i] for i in range(n1)]
    R = [A[q + j ] for j in range(n2)]

    i = j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            if ok_print == 1:
                list_prt[p + i] = '*'
            if ok_print == 1:
                tag = "k={}".format(k) + " L+R"
                PrintPartArray(list_prt, p, r, tag)
                PrintPartArray(A, 0, k+1, "A")
                print("")
                list_prt[p + i] = '-'
            i += 1
            Stats.Inc('cmpcnt')
        else:
            A[k] = R[j]
            if ok_print == 1:
                list_prt[q + j] = '*'
            if ok_print == 1:
                tag = "k={}".format(k) + " L+R"
                PrintPartArray(list_prt, p, r, tag)
                PrintPartArray(A, 0, k+1, "A")
                print("")
                list_prt[q + j] = '-'
            j += 1
            Stats.Inc('cmpcnt')
        k += 1

    while i < n1:
        A[k] = L[i]
        if ok_print == 1:
            list_prt[p + i] = '*'
        if ok_print == 1:
            tag = "k={}".format(k) + " L+R"
            PrintPartArray(list_prt, p, r, tag)
            PrintPartArray(A, 0, k+1, "A")
            print("")
            list_prt[p + i] = '-'
        i += 1
        k += 1
        Stats.Inc('r_inf_move_cnt')
        Stats.Inc('cmpcnt')

    while j < n2:
        A[k] = R[j]
        if ok_print == 1:
            list_prt[q + j] = '*'
        if ok_print == 1:
            tag = "k={}".format(k) + " L+R"
            PrintPartArray(list_prt, p, r, tag)
            PrintPartArray(A, 0, k+1, "A")
            print("")
            list_prt[q + j] = '-'
        j += 1
        k += 1
        Stats.Inc('cmpcnt')

    pass


def MERGE_SORT(A, p, r):

    # Note: we are following Python list index semantics

    # Sort subarray A[p:r]
    # e.g. to sort A[:] use MERGE_SORT(A, 0, len(A))

    # Complete the code here, see README on course website for problem description and instructions.

    # PrintPartArray(A, p, r, '*')

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
    MERGE_SORT(A, 0, len(A))
    Stats.PrintArray(A)
    n = len(A)
    Stats.Set (' %s*log_2(%s)'%(n,n), n*(math.log2(n)))
    Stats.PrintStats()
    return A
if __name__ == '__main__':

    A = [5,2,4,7,1,3,2,6 ] 


    main(A)

