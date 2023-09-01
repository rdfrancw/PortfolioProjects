#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from bs4 import BeautifulSoup
import pandas as pd
import requests
import smtplib
import time
import datetime
import csv


# In[2]:


# Connect to website

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_1?crid=270KQIBTA5KS3&keywords=data+t+shirt&qid=1693494522&sprefix=data+t+shir%2Caps%2C137&sr=8-1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)


# In[9]:


# Pull data

soup1 = BeautifulSoup(page.content, 'html.parser')

title = soup1.find(id = 'productTitle').get_text()

price = soup1.find(id = 'corePriceDisplay_desktop_feature_div').get_text()


print(title)
print(price)


# In[10]:


# Clean up data

title = title.strip()
price = price.strip()[1:6]
print(title)
print(price)


# In[11]:


# Create Timestamp for output to track when data is collected

date = datetime.date.today()

print(date)


# In[12]:


# Create CSV and write data into file

header = ['Title', 'Price', 'Date']
data = [title, price, date]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[13]:


df = pd.read_csv(r'C:\Users\RFran\AmazonWebScraperDataset.csv')

print(df)


# In[14]:


# Appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[15]:


# Combine all above code into one function

def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_1?crid=270KQIBTA5KS3&keywords=data+t+shirt&qid=1693494522&sprefix=data+t+shir%2Caps%2C137&sr=8-1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id = 'productTitle').get_text()

    price = soup2.find(id = 'corePriceDisplay_desktop_feature_div').get_text()

    title = title.strip()
    price = price.strip()[1:6]

    import datetime

    date = datetime.date.today()

    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, date]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[16]:


# Runs check_price after a set time and inputs data into CSV

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


# Function to send email once price hits a certain threshold

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('firstname_lastname@gmail.com', 'xxxxxxxxxxxxx')
    
    subject = "The product you have been tracking is below $15!"
    body = "Don't miss this opportunity to buy this product before the price changes again!"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'firstname_lastname@gmail.com',
        msg
    )

