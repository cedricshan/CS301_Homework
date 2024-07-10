#
# Created by Jiang Long 
#
# DKU CS301 FALL 2021 SESSION 02
# 

import tabulate, Stats, rIO

class Record:
    def __init__(self, key, payload):
        self.key, self.payload = key, payload
        self.nxt , self.pre = None, None
        pass
    def __str__(self):
        return '%s:%s'% (self.key, self.payload)
    pass

class HashTable:

    def __init__(self, n):
        self.A = [None] * n
        self.n = n
        self.h = lambda i: i % self.n
        self.population = 0
        pass

    def CHAINED_HASH_INSERT(self, x):
        Stats.Inc('INSERT cnt')
        newItem = True         # if x.key exists in T or not

        # Note 1: A trick for simpler implementation is to put x in front of
        # the collision and then traverse the chain to delete the
        # record that has the same key as x.key
        
        
        # Note 2: Before return use the following to print the output. 
        # 
        # Tabulate(self, 'INSERT(%s) %s' % (['update', 'new'][newItem], str(x)))
        # 


        # Complete the code here, see README on course website for problem description and instructions.

        index = self.h(x.key)
        x.pre = None
        x.nxt = self.A[index]
        if self.A[index] is not None:
            self.A[index].pre = x
        self.A[index] = x

        i = x.nxt
        key_insert = x.key
        while i is not None:
            if i.key == key_insert:
                newItem = False
                Stats.Inc('INSERT hit')
                self.CHAINED_HASH_DELETE_Modify(i)
            i = i.nxt

        if newItem == True:
            self.population += 1
        Tabulate(self, 'INSERT(%s) %s' % (['update', 'new'][newItem], str(x)))

        return x

    def CHAINED_HASH_INSERT_Modify(self, x):
        newItem = True         # if x.key exists in T or not

        index = self.h(x.key)
        x.pre = None
        x.nxt = self.A[index]
        if self.A[index] is not None:
            self.A[index].pre = x
        self.A[index] = x

        i = x.nxt
        key_insert = x.key
        while i is not None:
            if i.key == key_insert:
                newItem = False
                #Stats.Inc('INSERT hit')
                self.CHAINED_HASH_DELETE_Modify(i)
            i = i.nxt

        #if newItem == True:
            #self.population += 1
        #print("************************************")
        #Tabulate(self, '**************************')

        return x

    
    def CHAINED_HASH_DELETE(self, x): # remove itself
        Stats.Inc("DELETE cnt")
        # Complete the code here, see README on course website for problem description and instructions.

        #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        #print(str(x.pre))
        # If x is the first
        if x.pre is None:
             #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
             index = self.h(x.key)
             self.A[index] = x.nxt
             # x.nxt = None

        # x is not the first and last
        elif x.nxt is not None:
            x.pre.nxt = x.nxt
            x.nxt.pre = x.pre
            # x.pre = None
            # x.nxt = None
        
        # x is the last
        else:
            x.pre.nxt = x.nxt
            # x.pre = None

        Tabulate(self, 'DELETE %s' % str(x))
        self.population -= 1
        return x

    def CHAINED_HASH_DELETE_Modify(self, x): # remove itself
        # Stats.Inc("DELETE cnt")
        # Complete the code here, see README on course website for problem description and instructions.

        # If x is the first
        if x.pre is None:
             index = self.h(x.key)
             self.A[index] = x.nxt
             # x.nxt = None

        # x is not the first and last
        elif x.nxt is not None:
            x.pre.nxt = x.nxt
            x.nxt.pre = x.pre
            # x.pre = None
            # x.nxt = None
        
        # x is the last
        else:
            x.pre.nxt = x.nxt
            # x.pre = None

        # Tabulate(self, 'DELETE %s' % str(x))
        return x


    def CHAINED_HASH_SEARCH(self,key):
        Stats.Inc('SEARCH cnt')
        # Complete the code here, see README on course website for problem description and instructions.

        index = self.h(key)
        i = self.A[index]

        while i is not None:
            Stats.Inc('SEARCH visits(cost)')
            if i.key == key:
                Stats.Inc('SEARCH hit')
                #self.CHAINED_HASH_INSERT_Modify(Record(i.key, i.payload))

                # if i is not in the first
                if i.pre is not None:
                    i.pre.nxt = i.nxt
                    if i.nxt is not None:
                        i.nxt.pre = i.pre
                    i.nxt = self.A[index]
                    i.pre = None
                    self.A[index] = i

                Tabulate(self, 'SEARCH(hit) %s' % key)
                return i
            i = i.nxt

        Stats.Inc('SEARCH miss')
        Tabulate(self, 'SEARCH(miss) %s' % key)
        return None             # not found
    pass
#

def Tabulate(T, tag):
    
    rIO.dash(tag)

    # Then print the records in each slot

    # Complete the code here, see README on course website for problem description and instructions.

    for i in range(T.n):
        current = T.A[i]
        if current is not None:
            prt = str(current)
            current = current.nxt
        else:
            prt = "NIL"
        while current is not None:
            prt = prt + ' -> ' + str(current)
            current = current.nxt
        print('%3d  %s' % (i, prt))


#--------------------------------------------------
# Don't modify below this line
#--------------------------------------------------
def main(T):

    Stats.Set('SEARCH visits(cost)', 0)

    r =   T.CHAINED_HASH_SEARCH(1)
    T.CHAINED_HASH_INSERT(Record(1, 'penny'))
    T.CHAINED_HASH_INSERT(Record(8, '8_cents'))

    T.CHAINED_HASH_INSERT(Record(1, 'penny'))
    
    T.CHAINED_HASH_INSERT(Record(5, 'nickel'))
    T.CHAINED_HASH_INSERT(Record(10, 'dime'))
    T.CHAINED_HASH_INSERT(Record(10, 'jiao'))
    u = T.CHAINED_HASH_INSERT(Record(25, 'quarter'))
    T.CHAINED_HASH_INSERT(Record(100, 'dollar'))
    v = T.CHAINED_HASH_INSERT(Record(100, 'pound'))
    T.CHAINED_HASH_INSERT(Record(50, 'fifty'))
    T.CHAINED_HASH_INSERT(Record(40, 'forty'))

    rx = [24, 10, 1] 
    for i in rx:
        r =   T.CHAINED_HASH_SEARCH(i)
        if not r is None:
            T.CHAINED_HASH_DELETE(r)
        pass

    T.CHAINED_HASH_INSERT(Record(1, 'dollar'))
    T.CHAINED_HASH_INSERT(Record(2, 'pound'))
    T.CHAINED_HASH_INSERT(Record(24, 'twentyfour'))
    T.CHAINED_HASH_INSERT(Record(24+len(T.A) + 2, 'twentyfour+N'))
    T.CHAINED_HASH_INSERT(Record(40, 'forty_'))

    T.CHAINED_HASH_DELETE(u)
    T.CHAINED_HASH_DELETE(v)
    rx = [24, 40, 8] 
    for i in rx:
        r =   T.CHAINED_HASH_SEARCH(i)
        if not r is None:
            T.CHAINED_HASH_DELETE(r)
        pass


    Stats.Set('Population', T.population)
    Stats.Set('Load factor(alpha)', T.population/ len(T.A))
    Stats.PrintStats()
    return T

if __name__ == '__main__':
    N = 7
    T = HashTable(N)
    T = main(T)
    pass