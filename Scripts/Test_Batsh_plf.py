#!/usr/bin/env python
# coding: utf-8

# ## Test Batsh Plafrim.

# In[1]:


import pandas as pd


# Import d'un fichier

# In[17]:


test_df = pd.read_csv('../Datas/fichier_test_2.csv')


# In[18]:


test_df.iloc[:,1] +=1


# In[19]:


test_df


# In[21]:


test_df.to_csv('../Results/output_plf_2.csv')


# In[ ]:




