# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 09:00:40 2021

@author: PaulLeroy
"""

import os

import numpy as np
import cc

i_n1 = 0
i_n2 = 1
i_std1 = 2
i_std2 = 3
i_sig = 4
i_uncer = 5
i_dist = 6

dir_ = 'C:/DATA/TMP'
d10_D5_p30_reg02 = os.path.join(dir_, 'd10_D5_p30_reg02.sbf')
d5_p30_uncer_nan = os.path.join(dir_, 'd10_D5_p30_reg02_uncer_nan.sbf')
d5_p30_dist_nan = os.path.join(dir_, 'd10_D5_p30_reg02_dist_nan.sbf')

pc, sf, config = cc.read_sbf(d10_D5_p30_reg02, verbose=False)

uncer_nan = np.where(np.isnan(sf[:, i_uncer]))[0]
dist_nan = np.where(np.isnan(sf[:, i_dist]))[0]

cc.write_sbf(d5_p30_uncer_nan, pc[uncer_nan, :], sf[uncer_nan, :], config=config)
cc.write_sbf(d5_p30_dist_nan, pc[dist_nan, :], sf[dist_nan, :], config=config)
