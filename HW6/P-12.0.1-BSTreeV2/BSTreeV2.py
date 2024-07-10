#
# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 


import random
import random,  queue
import rIO, drawtree, Stats

class BST_Nil:
    def __init__(self):
        self.size = 0
        self.key = '#'
        self.left = None
        self.right = None
        pass
    def IsNil(self): return True
    def __str__(self): return '#'
    @property 
    def val(self): return 'nil'
    pass

nil = BST_Nil()

class BST_Node:
    def __init__(self, key):
        self.left = nil
        self.right = nil
        self.p = nil
        self.key = key
        
        pass
    def IsNil(self): return False
    def __str__(self): return str(self.key)
    @property 
    def val(self): return self.key
    pass

class BST_Tree:
    def __init__(self):
        self.root = nil
        pass

    # Note: You may need to add additional methods for recursion

    # Complete the code here, see README on course website for problem description and instructions.

    def inorder(self):
        return self.inorder_node(self.root)
    
    def inorder_node(self, node):
        if node.IsNil():
            return []
        ret = []
        ret = self.inorder_node(node.left)
        ret += [node]
        ret += self.inorder_node(node.right)
        return ret


    def preorder(self):
        return self.preorder_node(self.root)
    
    def preorder_node(self, node):
        if node.IsNil():
            return []
        ret = [node]
        ret += self.preorder_node(node.left)
        ret += self.preorder_node(node.right)
        return ret
    
    def TREE_INSERT(self, node):
        assert isinstance(node, BST_Node)
        
        if self.root.IsNil():
            self.root = node
        else:
            current = self.root
            while True:
                if node.key < current.key:
                    if current.left.IsNil():
                        current.left = node
                        node.p = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right.IsNil():
                        current.right = node
                        node.p = current
                        break
                    else:
                        current = current.right


    def Ith(self, ith):
        # return a BST_node
        return self.Ith_node(self.root, ith)
    
    def Ith_node(self, node, ith):
        # return the ith node in the trees rooted at node
        size_left = self.size_node(node.left)

        if size_left == ith:
            return node
        if size_left > ith:
            return self.Ith_node(node.left, ith)
        else:
            return self.Ith_node(node.right, ith - size_left - 1)
    
    def size(self):
        # return number of nodes in tree rooted at self.root
        return self.size_node(self.root)
    

    def size_node(self, node):
        if node.IsNil():
            return 0
        return 1 + self.size_node(node.left) + self.size_node(node.right)

        
        
    # And auxiliary functions for recursion



    def DrawTree(self):
        if self.root.IsNil(): return 'nil'
        return drawtree.drawtree2(self.root)
    pass

#-----------------------------------------------------------
# Don't modify below this line
#-----------------------------------------------------------
def main(A):
    T =BST_Tree()
    random.seed(0)
    random.shuffle(A)
    rIO.dash("Input:")
    print(A)
    print()
    
    rIO.dash("Test TREE_INSERT: "+ str(A))
    for i in A:
        T.TREE_INSERT(BST_Node(i))
        pass

    v = [i.key for i in T.inorder()]
    print('\nPost ALL INSERT Inorder: ', v)
    
    v = [i.key for i in T.preorder()]
    print('\nPost ALL INSERT Preorder: ', v)
    print()

    print(T.DrawTree())


    # Test DELETE and Ith

    r = T.size()
    for i in reversed(range(r)):
        

        ith = random.randint(0,i)

        # Get the ith elem and delete it 
        a = T.Ith(ith)
        print("INFO: %d_th key in T: %s" % (ith, a.key))
        #assert T.check()

        pass
        
    pass

if __name__=='__main__':
    A = list(range(20))
    
    main(A)
    pass