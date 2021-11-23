# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:31:22 2021

@author: PaulLeroy
"""

import os, shutil

root_ = '//lidar-server/DATA/RENNES1/New_Zealand'

raw = os.path.join(root_, 'Zone_B', '2017', 'Donnees_brutes', 'assemblage_')
lists = [os.listdir(raw + str(k)) for k in range(1, 9)]

path_ = os.path.join(root_, 'AAM_27413A03NOK_Kaikoura_2017', '01_Classified_Point')

dataIris = 'C:/DATA/New_Zealand/01_Classified_Point_2017_Thomas_Bernard'

list_ = os.listdir(path_)

# build the list of the files to move
toMove = {}
for i, l in enumerate(lists):
    toMove[f'assemblage{i+1}'] = []
    currentList = toMove[f'assemblage{i+1}']
    for f in l:
        root, ext = os.path.splitext(f)
        name = root[:-2] + '.laz'
        if name in list_:
            currentList.append(name)

# move the files
for assemblage in toMove:
    for file in toMove[assemblage]:
        src = os.path.join(path_, file)
        dst = os.path.join(dataIris, assemblage)
        if not os.path.exists(dst):
            os.mkdir(dst)
        print(f'{assemblage} {i} {f}')
        shutil.copy(src, dst)
