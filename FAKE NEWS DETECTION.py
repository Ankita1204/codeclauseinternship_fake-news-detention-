#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string


# In[5]:


dataset = pd.read_csv("Fake (2).csv")


# In[6]:


dataset.head()


# In[7]:


dataset.tail()


# In[ ]:




