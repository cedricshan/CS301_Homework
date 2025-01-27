#
# Created by Jiang Long for CS301 DKU Fall 2021
#

import random, Stats, functools

import  drawtree, rIO

#-------------------------------------------------
# Note: The implementation should follow textbook closely
#-------------------------------------------------

def PARENT(i): 
    # Complete the code here, see README on course website for problem description and instructions.
     return (i - 1) // 2


def LEFT(i):  
    # Complete the code here, see README on course website for problem description and instructions.
    return 2 * i + 1




def RIGHT(i):  
    # Complete the code here, see README on course website for problem description and instructions.
    return 2 * i + 2




# MAX_HEAP inherit from build-in class list
class MAX_HEAP:
    # constructor
    def __init__(self, A=[], key = None, verbosity = True):
        self.A = A
        self.verbosity = verbosity # debug printing
        
        self.key = key
        if self.key is None : self.key = lambda i: i
        self.heapsize = len(A)
        self.recur_depth = 0
        self.BUILD_MAX_HEAP()
        
        
        pass
    def HEAPSIZE(self): return self.heapsize
    def BUILD_MAX_HEAP(self):
        # if self.verbosity :
        #     rIO.dash("BUILD_MAX_HEAP: %s" %str(self.A))
        
        # Complete the code here, see README on course website for problem description and instructions.
        for i in range(self.heapsize // 2 - 1, -1, -1):
            self.MAX_HEAPIFY(i)

        assert self.Check_IsHEAP()
        pass
    
    def Check_IsHEAP(self):
        # Complete the code here, see README on course website for problem description and instructions.

        for i in range(self.heapsize):
            left_child = LEFT(i)
            right_child = RIGHT(i)

            # Check left child
            if left_child < self.heapsize and self.key(self.A[left_child]) > self.key(self.A[i]):
                return False
            
            # Check right child
            if right_child < self.heapsize and self.key(self.A[right_child]) > self.key(self.A[i]):
                return False

        return True
    
    
    def MAX_HEAPIFY(self, i):   # use self.heapsize as the heapsize
        
        self.recur_depth +=1

        # move the larger ones to the leaf
        # if self.verbosity :
        #     rIO.dash("MAX_HEAPIFY %s (recur_depth:%d)" % (i, self.recur_depth))
        
        # remember the current tree 
        #before = self.DrawTree(i) # for use in print the tree/heap transformation
        Before = list(self.A)

        # Coding Task
        #
        # 1. Implement MAX_HEAPIFY as in textbook
        #
        # 2. Use self.DrawTree and rIO.concat_text_block to visualize
        # the process (see README)
        #
        
        # Complete the code here, see README on course website for problem description and instructions.

        left_child = LEFT(i)
        right_child = RIGHT(i)
        largest = i
        
        if left_child < self.heapsize and self.key(self.A[left_child]) > self.key(self.A[largest]):
            largest = left_child

        if right_child < self.heapsize and self.key(self.A[right_child]) > self.key(self.A[largest]):
            largest = right_child

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            # print ("POST MAX_HEAPIFY(%s):" % i, self.A)
            # print()

            # After = list(self.A)
            # After[i] = '(%s)' % After[i]
            # Before[i] = '(%s)' % Before[i]
            # s = drawtree.draw_level_order2(Before) 
            # t = drawtree.draw_level_order2(After) 
            # #print (rIO.concat_text_block(s,t,'''MAX_HEAPIFY(%d)[LOCAL_FIX]\nheapsize=%d''' % (i, self.heapsize)))
            self.MAX_HEAPIFY(largest)


        # else:
        #     # print ("POST MAX_HEAPIFY(%s):" % i, self.A)
        #     # print()

        #     After = list(self.A)
        #     After[i] = '(%s)' % After[i]
        #     Before[i] = '(%s)' % Before[i]
        #     s = drawtree.draw_level_order2(Before) 
        #     t = drawtree.draw_level_order2(After) 
        #     #print (rIO.concat_text_block(s,t,'''MAX_HEAPIFY(%d)[same]\nheapsize=%d''' % (i, self.heapsize)))

        self.recur_depth -=1

        pass
    
    def HEAP_SORT(self):
        rIO.dash("HEAP_SORT")
        # Complete the code here, see README on course website for problem description and instructions.

        while self.heapsize > 1:
            # swap the heap root (max point) with the last one
            self.A[0], self.A[self.heapsize - 1] = self.A[self.heapsize - 1], self.A[0]
            self.heapsize -= 1
            # update the heap
            self.MAX_HEAPIFY(0)
        

        pass
    
    #-------------------------------------------------
    # To be used with rIO.concat_text_block(see README)
    #-------------------------------------------------
    def DrawTree(self, k=None, all = True):
        
        B = [i for i in  (self.A if all else self.A[:self.HEAPSIZE()]) ]
        if not k is None:
            B[k] = '(%s)'% B[k]
        r = drawtree.draw_level_order2(B)
        return r

    pass
    
#-------------------------------------------------
# No need to modify below this line
#-------------------------------------------------
def main(A):

    print("Input A:", A)

    h = MAX_HEAP(A)
    
    h.HEAP_SORT()

    rIO.dash("sorted A: %s" % A)
    
    assert A == list(sorted(A))
    pass

if __name__=='__main__':
    random.seed(0)
    A = list(range(10))
    random.shuffle(A)
    main(A)
    pass