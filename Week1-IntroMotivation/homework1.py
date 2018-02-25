import numpy as np


def seq_sum(n):
    """ input: n, generate a sequence of n random coin flips
        output: return the number of heads 
        Hint: For simplicity, use 1,0 to represent head,tails
    """
    #
    num_heads = 0
    result_list = np.random.rand(n)
    for flip in result_list:
        if flip > 0.5:
            num_heads += 1
    
    return num_heads
    #

#x = seq_sum(100)
#print(x)
#assert unique([seq_sum(2) for x in  range(0,200)]).tolist() == [0, 1, 2]
#[seq_sum(2) for x in  range(0,200)]






def estimate_prob(n, k1, k2, m):
    """Estimate the probability that n flips of a fair coin result in k1 to k2 heads
         n: the number of coin flips (length of the sequence)
         k1,k2: the trial is successful if the number of heads is 
                between k1 and k2-1
         m: the number of trials (number of sequences of length n)
         
         output: the estimated probability 
         """
    #
    success = 0

    for trial in range(m):
        
        num_heads = seq_sum(n)
        
        if k1 < num_heads < k2-1:
            success += 1
            trial += 1
        else:
            trial += 1
        
    estimated_prob = float(success/m)
    return estimated_prob

print(estimate_prob(100,45,55,1000))
print(estimate_prob(100, 40, 60, 100))

#print(x)
#assert 'float' in str(type(x))







# =============================================================================
# def calc_prob(n,k1,k2):
#     """Calculate the probability using a normal approximation"""
#     n=float(n);k1=float(k1);k2=float(k2)
#     z1=(k1-0.5*n)/(sqrt(n)/2)
#     z2=(k2-0.5*n)/(sqrt(n)/2)
#     return (erf(z2/sqrt(2))-erf(z1/sqrt(2)))/2
# 
# from math import erf,sqrt
# def evaluate(n,q1,q2,m,r=100):
#     """Run calc_range many times and test whether the estimates are consistent with calc_prob"""
#     k1=int(q1*n)
#     k2=int(q2*n)
#     p=calc_prob(n,k1,k2)
#     std=sqrt(p*(1-p)/m)
#     print('computed prob=%5.3f, std=%5.3f'%(p,std))
# 
#     L=[estimate_prob(n,k1,k2,m) for i in range(r)]
#     med=np.median(L)
#     print('ran estimator %d times, with parameters n=%d,k1=%d,k2=%d,m=%d'%(r,n,k1,k2,m))
#     print('median of estimates=%5.3f, error of median estimator=%5.3f, std= %f5.3'%(med,med-p,std))
#     return L,med,p,std,abs((med-p)/std)
# 
# def test_report_assert(n,q1,q2,m,r=100):
#     k1=int(q1*n)
#     k2=int(q2*n)
#     L,med,p,std,norm_err=evaluate(n,q1,q2,m,r=100)
#     hist(L);
#     plot([p,p],plt.ylim(),'r',label='true prob')
#     plot([med,med],plt.ylim(),'k',label='median of %d estimates'%r)
#     mid_y=mean(plt.ylim())
#     plot([p-std,p+std],[mid_y,mid_y],'g',label='+-std')
#     legend();
#     print('normalized error of median=',norm_err,'should be <1.0')
#     title('r=%d,n=%d,k1=%d,k2=%d,m=%d,\nnorm_err=%4.3f'%(r,n,k1,k2,m,norm_err))
#     assert norm_err<1.0
#     
#     
# =============================================================================
