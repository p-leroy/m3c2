# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

import numpy as np
import cc

dir_ = 'C:/DATA/test_build_planes'
sbf1 = os.path.join(dir_, 'plane1.sbf')
sbf2 = os.path.join(dir_, 'plane2.sbf')
sbf3 = os.path.join(dir_, 'plane3.sbf')
sbfCore = os.path.join(dir_, 'corePoint.sbf')

def build_pc(A, B, C, D, xx, yy):
    # Ax + By + Cz = D
    zz = (D -B * xx - C * yy) / A
    pc = np.c_[xx.flatten(), yy.flatten(), zz.flatten()]
    return pc

nx, ny = 101, 101
x = np.linspace(-10, 10, nx)
y = np.linspace(-10, 10, ny)
xx, yy = np.meshgrid(x, y) ## sparse=False by default

# this is important to add some noise otherwise M3C2 does not manage to compute N!
pc1 = build_pc(1, 1, 1, 0, xx, yy)
pc1 += np.random.normal(0, 0.1, pc1.shape)
cc.write_sbf(sbf1, pc1, None) # None => no scalar field

pc2 = build_pc(1, 1, 1, 10, xx, yy)
pc2 += np.random.normal(0, 0.1, pc2.shape)
cc.write_sbf(sbf2, pc2, None) 

pc3 = build_pc(1, 1, 1, 15, xx, yy)
pc3 += np.random.normal(0, 0.2, pc3.shape)
cc.write_sbf(sbf3, pc3, None) 

## core point
corePoint = np.array([0, 0, 0]).reshape(1, -1)
cc.write_sbf(sbfCore, corePoint, None) # None => no scalar field
