#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tgtg import TgtgClient
import requests

client = TgtgClient(access_token='e30.eyJzdWIiOiIxMTI0MDc4NjciLCJleHAiOjE2OTE5NDA1NTMsInQiOiJMSnd2SWpiVVRKZTNDa2hSRDlDMm5BOjA6MSJ9.LRYOSo944p79_Ei03AaeudBGIrJRlq8rmAc5o1Vg8do', 
                    refresh_token=credentials["refresh_token"],
                    user_id="112407867", 
                    cookie='datadome=2lqnRUe6C~ctcLOz_iTU-92MWRcLfLb2CLjzurbAFzyWLthbr~Bhw43Qyf4TguB1TD~FzQ199zfrAz2pFoIx~4yikyPqREsqYDZOOoVgDTPeG-FSOqGOv-B4Oc0WBEuO')

items = client.get_items()

token = "5764203582:AAFVmVIu9ftKRqabrQNr2z-ZIwlYW5eO-VM"
url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": "6494358014", "text": "Hello World"}

for k in items : 
    if k['items_available'] > 0 :
        params = {"chat_id": "6494358014", "text": f"Un panier est disponible à {k['display_name']}"}
        r = requests.get(url + "/sendMessage", params=params)

