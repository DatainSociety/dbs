#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os 
import numpy as np
import datetime
import sqlite3


# In[14]:



conn = sqlite3.connect('Test1.db')
c = conn.cursor()
# c.execute('''CREATE TABLE CLIENTS
#              ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')

# c.execute('''CREATE TABLE COUNTRY
#         ([generated_id] INTEGER PRIMARY KEY,[Country_ID] integer, [Country_Name] text)''')
        
# # Create table - DAILY_STATUS
# c.execute('''CREATE TABLE DAILY_STATUS
#              ([Client_Name] text, [Country_Name] text, [Date] date)''')

c.execute('''CREATE TABLE TEST_LEADS
             ([company] text,[job_title] text, [salary] text, [date_posted] text ,[job_details] text, [url] text)''')

                 
conn.commit()


# In[26]:


df = pd.read_csv('leads.csv', index_col=0)
# Depositing data into test_leads 
df.to_sql('TEST_LEADS', conn, if_exists='replace', index=False )


# In[27]:


df


# In[28]:


c.execute('''
SELECT DISTINCT *
FROM TEST_LEADS
          ''')


# In[29]:



sql_df = pd.DataFrame(c.fetchall(), columns = df.columns)


# In[31]:


pd.set_option('display.max_columns',None)


# In[32]:


sql_df


# In[33]:


[db for db in os.listdir() if '.db' in db]


# In[34]:


conn.close()


# In[36]:


l_conn = sqlite3.connect('Test1.db')

x = l_conn.cursor()


# In[39]:


x.execute('SELECT * FROM TEST_LEADS')
x.fetchall()

