#Written by Seth Talyansky on September 2, 2025
##Exercise 1
#A positive test result is not significant at the P < 0.05 level because P = 0.05 (5% of the time the test yields a positive result in an individual without HIV, i.e., given the null hypothesis that HIV is absent)
##Exercise 2
#Bayes' theorem: P(HIV|+) = P(+|HIV) * P(HIV)/P(+), where P(+|HIV) is the true positive rate, P(HIV) is the prevalence of HIV, and P(+) is the total probability of a positive result
import numpy as np
true_positive = 1-0 #1 - false negative rate
false_positive = 0.05
for prevalence in np.arange(0, 1.1, 0.1):
    p_hiv = true_positive * prevalence/(true_positive*prevalence+false_positive*(1-prevalence))
    print('When the prevalence is %d%%, the probability of infection given a positive test result is %d%%.' %(100*prevalence, 100*p_hiv))
#Output:
'''
When the prevalence is 0%, the probability of infection given a positive test result is 0%.
When the prevalence is 10%, the probability of infection given a positive test result is 68%.
When the prevalence is 20%, the probability of infection given a positive test result is 83%.
When the prevalence is 30%, the probability of infection given a positive test result is 89%.
When the prevalence is 40%, the probability of infection given a positive test result is 93%.
When the prevalence is 50%, the probability of infection given a positive test result is 95%.
When the prevalence is 60%, the probability of infection given a positive test result is 96%.
When the prevalence is 70%, the probability of infection given a positive test result is 97%.
When the prevalence is 80%, the probability of infection given a positive test result is 98%.
When the prevalence is 90%, the probability of infection given a positive test result is 99%.
When the prevalence is 100%, the probability of infection given a positive test result is 100%.
'''
