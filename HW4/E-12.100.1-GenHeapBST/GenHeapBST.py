# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import drawtree
import math, random

def GenHeapBST (A):

    # Note: return an list of numbers which is either pre-order or BFS
    # order of the BST (Demo uses pre-order)

    # Complete the code here, see README on course website for problem description and instructions.

    n = len(A)
    if n <= 1:
        return A
    
    hgt = int(math.log2(n))
    full = (2 ** hgt) - 1
    left_leaf = min(2 ** (hgt-1), n - full)
    root_idx = int ((full - 1) / 2 + left_leaf)

    return [A[root_idx]] + GenHeapBST(A[:root_idx]) + GenHeapBST(A[root_idx+1:])




#-----------------------------------------------------
# Don't modify below this line
#-----------------------------------------------------
def main(A):
    A = sorted(A)
    r = GenHeapBST(A)
    print('BST preorder:', r)
    print()
    drawtree.draw_bst(r)
    # Note: usage of draw_bst
    # nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    # draw_bst(nums)
    
    pass
    
if __name__ == '__main__':
    a = list(range(22))
    random.shuffle(a)
    main(a)

    pass
    
    

    