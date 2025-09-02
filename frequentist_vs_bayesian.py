#Written by Seth Talyansky on September 2, 2025
##Exercise 1
#A positive test result is not significant at the P < 0.05 level because P = 0.05 (5% of the time the test yields a positive result in an individual without HIV, i.e., given the null hypothesis that HIV is absent)
##Exercise 2
#Bayes' theorem: P(HIV|+) = P(+|HIV) * P(HIV)/P(+), where P(+|HIV) is the true positive rate, P(HIV) is the prevalence of HIV, and P(+) is the true positive rate (1 minus the false negative rate) plus the false positive rate
import numpy as np
true_positive = 1-0
false_positive = 0.05
for prevalence in np.arange(0, 1.1, 0.1):
    p_hiv = true_positive * prevalence/(true_positive+false_positive)
    print('When the prevalence is %d%%, the probability of infection given a positive test result is %d%%.' %(100*prevalence, 100*p_hiv))
