#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd


# In[11]:


flights=pd.read_csv('flights.csv')


# In[16]:


flights.drop_duplicates(subset=None, keep='first', inplace=True)


# In[14]:


flights.head(20)
