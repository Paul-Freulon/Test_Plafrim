#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
sys.path.append("../Functions")
from Functions_plf_test import *


# ##### Test d'import des fonctions

# In[2]:


fonc1()


# In[3]:


fonc2()


# ##### Test d'import de données

# In[6]:


test_df = pd.read_csv('../Datas/fichier_test_plafrim.csv', usecols=[2])


# In[9]:


test_df_out = test_df+1


# In[10]:


test_df_out.head()


# In[11]:


test_df_out.to_csv('output_plf.csv')


# In[ ]:




