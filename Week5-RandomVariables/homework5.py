"""
Suppose that a 6-sided die is rolled nn times. Let XiXi be the value of the top face at the iith roll, and let X≜max1≤i≤nXiX≜max1≤i≤nXi be the highest value observed. For example, if n=3n=3 and the three rolls are 4, 1, and 4, then X1=4,X2=1,X3=4X1=4,X2=1,X3=4 and X=4X=4.

To find the distribution of XX, observe first that X≤xX≤x iff Xi≤xXi≤x for all 1≤i≤n1≤i≤n, hence P(X≤x)=(x/6)nP(X≤x)=(x/6)n. It follows that P(X=x)=P(X≤x)−P(X≤x−1)=(x/6)n−((x−1)/6)nP(X=x)=P(X≤x)−P(X≤x−1)=(x/6)n−((x−1)/6)n. For example, P(X=1)=(1/6)nP(X=1)=(1/6)n, and P(X=2)=(1/3)n−(1/6)nP(X=2)=(1/3)n−(1/6)n.

In this problem we assume that each of the nn dice has a potentially different number of faces, denoted fifi, and ask you to write a function largest_face that determines the probability P(x)P(x) that the highest top face observed is xx. largest_face takes a vector ff of positive integers, interpreted as the number of faces of each of the dice, and a value xx and returns P(x)P(x). For example, if f=[2,5,7]f=[2,5,7], then three dice are rolled, and P(1)=(1/2)⋅(1/5)⋅(1/7)P(1)=(1/2)⋅(1/5)⋅(1/7) as all dice must be 1, while P(7)=1/7P(7)=1/7 as the third die must turn up 7.
"""

import numpy as np

def largest_face(m, m_max):
    # inputs: m is a list of integers and m_max is an integer
    # output: a variable of type 'float'
    
    #
    
    def calc_prob(f, f_max):
        
        prob = [(f_max/num) for num in f if f_max <= num]
        
        return np.prod(prob)
    
    
    prob_x_max = calc_prob(m, m_max) - calc_prob(m, m_max - 1)
    
    return prob_x_max
    #
    

#print(largest_face([2,5,8], 8))
#print(largest_face([2], 1))
#print(largest_face([3,4], 2))
#print(largest_face([2, 5, 7, 3], 3))







def constrained_compositions(n, m):
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples
    
    k = len(m)
    parts = set()
    if k == n:
        if 1 <= min(m):
            parts.add((1,)*n)
    if k == 1:
        if n <= m[0]:
            parts.add((n,))
    else:
        for x in range(1, min(n-k+2,m[0]+1)):
            for y in constrained_compositions(n-x, m[1:]):
                parts.add((x,)+y)
    return parts


def face_sum(m, s):
    # inputs: m is list of integers and s is an integer
    # output: a variable of type 'float'
    
    #
    
    len_sum = len(constrained_compositions(s, m))
#    
#    if len_sum == 0:
#        return 0
#    else: 
#        return len_sum / np.prod(m)
    #
    
    return 0 if len_sum ==0 else len_sum / np.prod(m)


print(face_sum([3, 4, 5], 13))
print(face_sum([2,2], 3))
print(face_sum([3, 4, 5], 7))
    
    
    
    
    
