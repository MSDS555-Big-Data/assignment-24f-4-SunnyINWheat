#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd


# In[11]:


flights=pd.read_csv('flights.csv')


# In[19]:


flights.dropna().head(20)
