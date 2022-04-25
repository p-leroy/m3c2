# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:37:31 2022

@author: PaulLeroy
"""

import os

import cc

i_n1 = 0
i_n2 = 1
i_std1 = 2
i_std2 = 3
i_sig = 4
i_uncer = 5
i_dist = 6

dir_ = 'C:/DATA/tbe/Pre_andPost_EQ_results'
d5_yes_1_4_sbf = os.path.join(dir_, 'd5 yes 1_4.sbf')
d5_yes_2_8_sbf = os.path.join(dir_, 'd5 yes 2_8.sbf')
d5_yes_1_4_equal_2_8_sbf = os.path.join(dir_, 'd5 yes 1_4 equal 2_8.sbf')

pc0, sf0, config0 = cc.read_sbf(d5_yes_1_4_sbf)
pc1, sf1, config1 = cc.read_sbf(d5_yes_2_8_sbf)

dist0 = sf0[:, i_dist]
dist1 = sf1[:, i_dist]

valid = dist0 == dist1

cc.write_sbf(d5_yes_1_4_equal_2_8_sbf, pc0[valid, :], sf0[valid, :], config0)
