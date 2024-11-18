#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:


pop1=pd.read_csv('NYC-pop1.csv',skiprows=5)


# In[3]:


## Part 1: All regions
pop1.set_index('Year').plot()