#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 05:10:46 2022

@author: nhinguyen
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./api_results.csv')
data['time'] = pd.to_datetime(data['time'])

plt.scatter(data['time'], data['factor'])
plt.xlabel('Time')
plt.ylabel('Factor')
plt.show()

plt.scatter(data['time'], data['pi'])
plt.xlabel('Time')
plt.ylabel('Pi')
plt.show()

plt.plot(data['time'], data['factor'])
plt.xlabel('Time')
plt.ylabel('Factor')
plt.show()