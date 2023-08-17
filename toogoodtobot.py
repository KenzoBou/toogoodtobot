#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tgtg import TgtgClient
import requests

client = TgtgClient(email="guillaume.kravitz@gmail.com")
credentials = client.get_credentials()

client = TgtgClient(access_token='e30.eyJzdWIiOiIxMTI0MDc4NjciLCJleHAiOjE2OTI0NDk4MjcsInQiOiJHUXFtdVZQZVJzU3N5ZWU1cWlwbDlBOjA6MSJ9.U94-vimALNeFtU2qNmpATQEUI8SGNi5XKWyOl2pPaGs', 
                    refresh_token='e30.eyJzdWIiOiIxMTI0MDc4NjciLCJleHAiOjE3MjM4OTk0MjcsInQiOiJ5RV83NW96WFNWeTVhV21fUmM4ejZBOjA6MCJ9.v-NFRwvU4Zd389NAMR_q4y6Jszuyio_eF7X0OozMgLs',
                    user_id='112407867', 
                    cookie='datadome=60zF7Fsd71X-awneRLF4jDLDDwEYmIdrE8WpDW~oyFCZsHAQ9ME3P9cIQtqtJBum8Bg1syKcTIthe6wa-97~75R0_RyUA3wlDlO8y~BHKKq8TdLrc~pg-wdhJnVlJNqm; Max-Age=5184000; Domain=.apptoogoodtogo.com; Path=/; Secure; SameSite=Lax')


items = client.get_items()

token = "5764203582:AAFVmVIu9ftKRqabrQNr2z-ZIwlYW5eO-VM"
url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": "6494358014", "text": "Hello World"}

for k in items : 
    if k['items_available'] > 0 :
        params = {"chat_id": "6494358014", "text": f"Un panier est disponible à {k['display_name']}"}
        r = requests.get(url + "/sendMessage", params=params)
