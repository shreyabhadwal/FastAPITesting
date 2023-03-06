# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:56:48 2023

@author: sbhadwal
"""

import pickle

infile = open('C:/Users/sbhadwal/sol1/streamapp/deployment_28042020.pkl','rb')
new_dict = pickle.load(infile)
infile.close()