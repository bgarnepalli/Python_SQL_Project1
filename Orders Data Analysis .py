#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import libraries
#!pip install kaggle
import kaggle
get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[ ]:


#extract file from zip file

#import zipfile
#zip_ref = zipfile.ZipFile('orders.csv.zip') 
#zip_ref.extractall() # extract file to dir
#zip_ref.close() # close file


# In[4]:


#read data from the file and handle null values

#!pip install pandas
import pandas as pd
df = pd.read_csv('orders.csv', encoding='latin1', na_values=['Not Available', 'unknown'])
df['Ship Mode'].unique()


# In[50]:


#rename columns names ..make them lower case and replace space with underscore

df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[52]:


#derive new columns discount , sale price and profit


df['discount']=(df['list_price']*df['discount_percent'])/100
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df.head(5)


# In[54]:


#convert order date from object data type to datetime
df.dtypes
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[56]:


#drop cost price list price and discount percent columns

df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
df.head(5)


# In[58]:


#load the data into sql server using replace option

import sqlalchemy as sal
engine = sal.create_engine('mssql://Bhanuprasad\\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[60]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'replace')


# In[ ]:




