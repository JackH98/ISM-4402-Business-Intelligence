#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
Location = "/Users/jackh/Downloads/datasets/datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[12]:


df.head()


# In[14]:


import pandas as pd
Location = "/Users/jackh/Downloads/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)


# In[15]:


df.head()


# In[16]:


import pandas as pd
Location = "/Users/jackh/Downloads/datasets/datasets/smallgradesh.csv"
# To add headers as we load the data...
df = pd.read_csv(Location, names=['Names','Grades'])
# To add headers to a dataframe
df.columns = ['Names','Grades']


# In[17]:


df.head()


# In[18]:


df.to_csv('studentgrades.csv',index=False,header=False)


# In[19]:


df.head()


# In[ ]:




