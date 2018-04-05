"""
In the lecture we considered the sample-mean estimator for the distribution mean. Another estimator for the distribution mean is the min-max-mean estimator that takes the mean (average) of the smallest and largest observed values. For example, for the sample {1, 2, 1, 5, 1}, the sample mean is (1+2+1+5+1)/5=2 while the min-max-mean is (1+5)/2=3. In this problem we ask you to run a simulation that approximates the mean squared error (MSE) of the two estimators for a uniform distribution.

Take a continuous uniform distribution between aa and bb - given as parameters. Draw a 10-observation sample from this distribution, and calculate the sample-mean and the min-max-mean. Repeat the experiment 1,000,000 times, and for each estimator calculate its average bias, and its (Bessel-corrected) sample-variance over the 1,000,000 estimates. Take the square of the average bias plus the sample variance as your MSE estimates.

Note that you can use the function numpy.random.uniform to generate random samples. You can calculate the mean and variance using the formulas presented in the lecture or via the function numpy.mean and numpy.var. To calculate the unbiased sample variance using function numpy.var, you will need to set ddof=1.

For this problem, you are asked to write a function Sample_Mean_MSE that experimentally calculates the MSE of the sample-mean estimator for samples drawn from uniform distribution given the bounds aa and bb.

"""



import numpy as np
import math


#def calculate_mean(a, b):
#    
#    
#    sample_variance = np.var(sample)
#    bessel_variance = np.var(sample, ddof=1)
#    
#    return sample_variance, bessel_variance
    

def Sample_Mean_MSE(a,b):
    # inputs: bounds for uniform distribution a and b
    # sample size is 10
    # number of experiments is 1,000,000
    # output: MSE for sample mean estimator with sample size 10
    
    total_experiment = []
#    total_bias = []
#    distribution_mean = (b-a)/10
    
    for i in range(1000000):
        sample = np.random.uniform(a, b, 10)
        sample_mean = np.mean(sample)
        total_experiment.append(sample_mean)
#        total_bias.append(sample_mean - distribution_mean)
    
#    total_sample_mean = np.mean(total_sample)
#    total_bias_mean = np.mean(total_bias)
    
    total_bessel_variance = np.var(total_experiment, ddof=1)
    
    return total_bessel_variance
        

def MinMax_Mean_MSE(a, b):
    # inputs: bounds for uniform distribution a and b
    # sample size is 10
    # number of experiments is 1,000,000
    # output: MSE for sample mean estimator with sample size 10
    
    total_experiment = []
    
    for i in range(1000000):
        sample = np.random.uniform(a, b, 10)
        sample_minmax_mean = (np.max(sample) - np.min(sample)) / 10
        total_experiment.append(sample_minmax_mean)
    
    total_bessel_variance = np.var(total_experiment, ddof=1)
    
    return total_bessel_variance  

    
    
    

#[63.7, 63.5, 63.6, 63.6, 63.9]

#print(Sample_Mean_MSE(0,10))
# 0.83433254206591267
    

print(MinMax_Mean_MSE(0, 10))
# 0.37865973633197908