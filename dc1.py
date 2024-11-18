#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd


# In[11]:


flights=pd.read_csv('flights.csv')


# In[13]:


flights['year'].fillna(flights['year'].mode()[0], inplace=True)


# In[14]:


flights.head(20)
