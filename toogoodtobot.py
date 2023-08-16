#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tgtg import TgtgClient
import requests

client = TgtgClient(email="guillaume.kravitz@gmail.com")
credentials = client.get_credentials()

client = TgtgClient(access_token='e30.eyJzdWIiOiIxMTI0MDc4NjciLCJleHAiOjE2OTE5NDA1NTMsInQiOiJMSnd2SWpiVVRKZTNDa2hSRDlDMm5BOjA6MSJ9.LRYOSo944p79_Ei03AaeudBGIrJRlq8rmAc5o1Vg8do', 
                    refresh_token='e30.eyJzdWIiOiIxMTI0MDc4NjciLCJleHAiOjE3MjMzOTAxNTMsInQiOiJlUGFUcmUxNFRHS2tsOXpqZXlsdXZBOjA6MCJ9.BS4lm0elLI-vtbf8dQdUSwOZ-SQ0_tt0iWDNmDuJ6wE',
                    user_id="112407867", 
                    cookie='datadome=4s4F5UKgeELddOGszCx~1z3C~EKZiXBKgUop_4-3tuQufoGNoAr5B0WJEQQ143BDGJ39BKDSgW_ug3UVl6aQ4pYSc4WLbZlS6w3Z6WI~StFWXdp1~F9pyEDwVCZzhd7b; Max-Age=5184000; Domain=.apptoogoodtogo.com; Path=/; Secure; SameSite=Lax')

items = client.get_items()

token = "5764203582:AAFVmVIu9ftKRqabrQNr2z-ZIwlYW5eO-VM"
url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": "6494358014", "text": "Hello World"}

for k in items : 
    if k['items_available'] > 0 :
        params = {"chat_id": "6494358014", "text": f"Un panier est disponible à {k['display_name']}"}
        r = requests.get(url + "/sendMessage", params=params)
