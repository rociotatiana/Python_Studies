#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:20:32 2021

@author: kala
"""
csv_path = 'file1.csv'

df = pd.read_csv(csv_path)

x = np.linspace ( 0, 2*np.pi, 100)
y = np.sin(x)

%matplotlib inline
plt.plot(x, y)