#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:


pop1=pd.read_csv('NYC-pop1.csv',skiprows=5)

pop1.set_index('Year').Queens.plot(legend=True)