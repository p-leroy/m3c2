# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:11:08 2021

@author: PaulLeroy
"""

#%%
import os

import numpy as np
from scipy import stats
from scipy.stats import t as t_distribution

import cc

i_n1 = 0
i_n2 = 1
i_std1 = 2
i_std2 = 3
i_sig = 4
i_uncer = 5
i_dist = 6
i_searchDepth1 = 7
i_searchDepth2 = 8
i_index = 9
i_welch_t = 10
i_welch_v = 11
i_welch_q = 12

def welch_t(n1, n2, s1, s2, mu1_minus_mu2): 
    # dist is mean2 - mean1 in CC
    # not the same convention as in the formula used to compute t
    t = mu1_minus_mu2 / (s1**2 / n1 + s2**2 / n2)**0.5
    return t

def welch_v(n1, n2, s1, s2):
    v = (s1**2 / n1 + s2**2 / n2)**2 \
        / (s1**4 / (n1**2 * (n1-1)) + s2**4 / (n2**2 * (n2-1)))
    return v

def welch_q(t, v):
    q = 2 * (1 - t_distribution.cdf(abs(t), v))
    return q

def boost_welch_q(t, v):
    q = 2 * t_distribution.sf(abs(t), v)
    return q

#%%
dir_ = 'C:/DATA/test_double_intercept'
welch = os.path.join(dir_, 'welch.sbf')

pc, sf, config = cc.read_sbf(welch, verbose=False)

t = welch_t(sf[:, i_n1], sf[:, i_n2], sf[:, i_std1], sf[:, i_std2], -sf[:, i_dist])
v = welch_v(sf[:, i_n1], sf[:, i_n2], sf[:, i_std1], sf[:, i_std2])

q = welch_q(t, v)
q_boost = boost_welch_q(t, v)
q_cc = sf[:, i_welch_q]
dist_cc = sf[:, i_dist]
#double q = cdf(complement(dist, fabs(t_stat)));

#%% scipy.stats.ttest_ind

rng = np.random.default_rng()

n1 = 100
n2 = 200

rvs1 = stats.norm.rvs(loc=5, scale=10, size=n1, random_state=rng)
rvs2 = stats.norm.rvs(loc=5, scale=20, size=n2, random_state=rng)

# If False, perform Welch’s t-test, which does not assume equal population variance
stats_ttest = stats.ttest_ind(rvs1, rvs2, equal_var=False)


#%%
s1 = rvs1.std(ddof=1) 
s2 = rvs2.std(ddof=1)
mu1 = rvs1.mean()
mu2 = rvs2.mean()

my_t = welch_t(n1, n2, s1, s2, mu1-mu2)
my_v = welch_v(n1, n2, s1, s2)
my_q = welch_q(my_t, my_v)

print(f"mu1 - mu2 = {mu1 - mu2}")
print(stats_ttest)
print(f"my_t {my_t}")
print(f"my_v {my_v}")
print(f"my_q {my_q}")
print(f"boost q = {boost_welch_q(my_t, my_v)}")












