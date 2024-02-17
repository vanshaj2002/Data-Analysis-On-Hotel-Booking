#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#loading the data set
df=pd.read_csv('hotel_bookings 2.csv')


# In[3]:


#Exploratory Data Analysis and Data Cleaning 
df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df['reservation_status_date'] =pd.to_datetime(df['reservation_status_date'])


# In[9]:


df.describe(include='object')


# In[10]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[11]:


df.isnull().sum()


# In[12]:


df.drop(['company','agent'],axis=1,inplace=True)
df.dropna(inplace=True)


# In[13]:


df.isnull().sum()


# In[14]:


df.describe()


# In[15]:


#removing this outlier(value>5000)
df['adr'].plot(kind='box')


# In[16]:


#take values less than 5000 only
df= df[df['adr']<5000]


# In[17]:


df['adr'].plot(kind='box')


# In[18]:


#DATA ANALYSIS AND VISUALIZATIONS ON CLEAN DATA


# In[19]:


cancelled_perc= df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)

plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
plt.show()


# In[20]:


plt.figure(figsize=(8,4))
axl=sns.countplot(x='hotel',hue='is_canceled',data =df,palette='Blues')
legend_labels,_ = axl.get_legend_handles_labels()
axl.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels',size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[21]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[22]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[23]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[24]:


plt.figure(figsize=(20,8))
plt.title('Average Daily Rate in City and Resort Hotel',fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label='Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label='City Hotel')
plt.legend(fontsize=20)
plt.show()


# In[25]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
axl=sns.countplot(x='month',hue='is_canceled',data =df,palette='bright')
legend_labels,_ = axl.get_legend_handles_labels()
axl.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month',size=20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[26]:


#Average Daily Rate for each Month
plt.figure(figsize=(15,8))
plt.title('ADR per month',fontsize=30)
sns.barplot('month','adr',data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[27]:


cancelled_data=df[df['is_canceled']==1]
top_10_country=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('Top 10 contries with resrvation canceled')
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()


# In[28]:


df['market_segment'].value_counts()


# In[29]:


df['market_segment'].value_counts(normalize=True)


# In[30]:


cancelled_data['market_segment'].value_counts(normalize=True)


# In[33]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date' , inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[34]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[35]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate', fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)


# In[ ]:




