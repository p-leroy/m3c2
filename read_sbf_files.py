# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:17:46 2022

@author: PaulLeroy
"""

import os

import cc

dir_ = "C:/DATA/test_double_intercept_dla"

#sbf = os.path.join(dir_, "sharpMean sig removed.sbf")
#sbf = os.path.join(dir_, "M3C2_initial_remaining.sbf")
#sbf = os.path.join(dir_, "M3C2_removed_by_sharpMean.sbf")
#sbf = os.path.join(dir_, "sharp sig ++.sbf")
sbf = os.path.join(dir_, "sharp ++.sbf")

pc, sf, config = cc.read_sbf(sbf)
