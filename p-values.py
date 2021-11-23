# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:54:11 2021

@author: PaulLeroy
"""

import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv', usecols=['mpg', 'wt'])

model = smf.ols('mpg ~ wt', data=df).fit()
