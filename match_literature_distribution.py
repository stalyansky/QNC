#Written by Seth Talyansky on September 4, 2025
#Code adapted from binomial distribution tutorial to replicate Fig. 2B/D from Searl and Silinsky (J. Physiol. 2002)
import numpy as np
import collections
import matplotlib.pyplot as plt
from scipy.stats import binom

p = 0.089
n = 38                      # number of "trials" per "experiment"
num_experiments = 10000;     # number of "experiments"
outcomes = binom.rvs(n,p,size=num_experiments)

# Show a bar plot (histogram) of all of the possible outcomes
counts = collections.Counter(outcomes)
plt.bar(counts.keys(), counts.values())
plt.xlim([-1, n+1])
plt.title(f'Strontium-mediated MEPPs (binomial model), n={n}, p={p}, {num_experiments} simulations')
plt.ylabel('Count')
plt.show()