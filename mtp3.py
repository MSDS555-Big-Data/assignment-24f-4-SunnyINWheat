#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd


pop2=pd.read_csv('NYC-pop2.csv')


# In[7]:


df=pop2.set_index('Borough')


# In[9]:


df1=df.T


# In[10]:


df1.plot()
