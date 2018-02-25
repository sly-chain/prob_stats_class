def partitionfunc(n,k,l=1):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l, n+1):
        for result in partitionfunc(n-i, k-1, i):
            yield (i,)+result
            
#print(set(partitionfunc(8, 2)))

def weak_compositions(k, n, parent=tuple()):
    if k > 1:
        for i in range(n + 1):
            for x in weak_compositions(k - 1, i, parent + (n - i,)):
                yield x
    else:
        yield parent + (n,)
    
#print(set(weak_compositions(2, 8)))

def int_combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

#print(set(int_combinations(range(7), 1)))
        
        
        
        
    

from itertools import combinations
#from scipy.special import binom

def compositions(k, n):
    last = (n-1,)
    first = (-1,)
    for t in combinations(range(n-1), k-1):
        yield tuple(v - u for u, v in zip(first + t, t + last))

#print(set(compositions(2, 8)))
#print(set(compositions(2, 5)))
#print(set(compositions(3, 7)))



def constrained_compositions(n, m):
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples
    
    #
    k = len(m)
    full_set = set(compositions(k, n))
    constrained_set = full_set.copy()
    
    for i in full_set:
        for x,y in zip(i, m):
            if x > y:
                constrained_set.remove(i)
                break
    
#    constrained_set = set(i for i in full_set if all(x <= y for x, y in zip(i, m)))
    return constrained_set
        

#print(constrained_compositions(7, [1,4,4]))
print(constrained_compositions(8, [3,2,4]))


#
#constrained_test = full_test.copy()
#for i in full_test:
#    print('i', i)
#    
#    for x,y in zip(i,m):
#        if x > y:
#            constrained_test.remove(i)
            
#
#tuple(constrained_test.remove(i) for i in full_test if all(x <= y for x, y in zip(i, m)))
