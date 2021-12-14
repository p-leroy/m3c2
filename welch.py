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
i_welch_p = 13
i_welch_lod95 = 14
i_welch_sig = 15

def welch_t(n1, n2, s1_in, s2_in, mu1_minus_mu2, from_cc=False):
    # dist is mean2 - mean1 in CC
    # not the same convention as in the formula used to compute t
    if from_cc:
        s1 = s1_in * (n1 / (n1-1))**0.5
        s2 = s2_in * (n2 / (n2-1))**0.5
    else:
        s1 = s1_in
        s2 = s2_in
    t_denominator = (s1**2 / n1 + s2**2 / n2)**0.5
    t = mu1_minus_mu2 / t_denominator
    return t, t_denominator

def welch_v(n1, n2, s1_in, s2_in, from_cc=False):
    if from_cc:
        s1 = s1_in * (n1 / (n1-1))**0.5
        s2 = s2_in * (n2 / (n2-1))**0.5
    else:
        s1 = s1_in
        s2 = s2_in
    v = (s1**2 / n1 + s2**2 / n2)**2 \
        / (s1**4 / (n1**2 * (n1-1)) + s2**4 / (n2**2 * (n2-1)))
    return v

def welch_p(v):
    # percent point function (inverse of cdf), percentiles [scipy]
    # isf inverse survival function
    p = t_distribution.ppf(0.975, v)
    return p

def welch_lod95(v, t_denominator):
    lod95 = welch_p(v) * t_denominator
    return lod95

def welch_q(t, v):
    q = 2 * (1 - t_distribution.cdf(abs(t), v))
    return q

def boost_welch_q(t, v):
    # sf survival function
    # also defined as 1 - cdf, but sf is sometimes more accurate [numpy]
    q = 2 * t_distribution.sf(abs(t), v)
    return q

#%%
dir_ = 'C:/DATA/test_double_intercept'
welch = os.path.join(dir_, 'welch.sbf')

pc, sf, config = cc.read_sbf(welch, verbose=False)

from_cc = True
t, den = welch_t(sf[:, i_n1], sf[:, i_n2], sf[:, i_std1], sf[:, i_std2], -sf[:, i_dist],
                 from_cc=from_cc)
v = welch_v(sf[:, i_n1], sf[:, i_n2], sf[:, i_std1], sf[:, i_std2],
            from_cc=from_cc)
q = welch_q(t, v)
p = welch_p(v)
lod95 = welch_lod95(v, den)

cc_t = sf[:, i_welch_t]
cc_v = sf[:, i_welch_v]
cc_q = sf[:, i_welch_q]
cc_p = sf[:, i_welch_p]
cc_lod95 = sf[:, i_welch_lod95]
cc_dist = sf[:, i_dist]
compare_lod = np.c_[cc_lod95, lod95]
compare_t = np.c_[cc_t, t]
#double q = cdf(complement(dist, fabs(t_stat)));

#%% scipy.stats.ttest_ind

rng = np.random.default_rng()

n1 = 100
n2 = 30

rvs1 = stats.norm.rvs(loc=5, scale=10, size=n1, random_state=rng)
rvs2 = stats.norm.rvs(loc=15, scale=20, size=n2, random_state=rng)

# If False, perform Welch’s t-test, which does not assume equal population variance
stats_ttest = stats.ttest_ind(rvs1, rvs2, equal_var=False)


#%%
s1 = rvs1.std(ddof=1) 
s2 = rvs2.std(ddof=1)
mu1 = rvs1.mean()
mu2 = rvs2.mean()

my_t, my_t_den = welch_t(n1, n2, s1, s2, mu1-mu2)
my_v = welch_v(n1, n2, s1, s2)
my_q = welch_q(my_t, my_v)
my_p = welch_p(my_v)
my_lod95 = welch_lod95(my_v, my_t_den)

print(f"mu1 - mu2 = {mu1 - mu2:.3f} (lod95 = {my_lod95:.3f})")
print(f"t = {my_t:.3f}, q = {my_q*100:.2f}%, v = {my_v:.2f}, p = {my_p:.3f}")
print(stats_ttest)












