#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tgtg import TgtgClient
client = TgtgClient(email="guillaume.kravitz@gmail.com")
credentials = client.get_credentials()
print(credentials)

