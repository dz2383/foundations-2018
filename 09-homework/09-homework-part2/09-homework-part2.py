
# coding: utf-8

# # Using Scraping
# Scrape the front page of some always-updating website, such as
# 
# https://www.slickdeals.net/ (Links to an external site.)Links to an external site.
# https://www.reddit.com (Links to an external site.)Links to an external site./
# https://www.washingtonpost.com (Links to an external site.)Links to an external site./
# https://finance.yahoo.com/industries (Links to an external site.)Links to an external site.
# anything else, really
# Note that some of these won't work with BeautifulSoup!
# 
# Send yourself an email with as much information as possible from the site, such as:
# 
# The title of the thing (the sale, the article, whatever)
# A URL for it
# Upvotes/thumbs ups/subreddits/prices/links to images/etc
# Save this as a CSV, and send it as an attachment to your email address every 6 hours. The email headline should say something like "Here is your 6PM briefing." The CSV file should be timestamped with the current date and time, e.g. briefing-2018-06-18-3PM.csv
# 
# BONUS: Have the content actually be the body of the email, not just an attachment. I don't mean like a CSV or whatever, I mean it should actually look like nice lists and stuff, a real email.

# In[28]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


# # I picked the NY Times

# In[29]:


response = requests.get('http://www.nytimes.com')
doc = BeautifulSoup(response.text, 'html.parser')


# In[30]:


# Testing url

# stories = doc.find_all(class_ ='story')
# print(stories[0].h1.a['href'])
# stories[1].h2.a['href']
# stories[0].a['href']
# stories[2].a['href']
# stories[3].a['href']


# # Put all in one cell:

# In[44]:


stories = doc.find_all(class_ ='story')
list_of_stories = []

for story in stories:
    story_dict = {}
    headline = story.find(class_='story-heading')
    byline = story.find(class_='byline')
    time =story.find(class_="timestamp")
    summary = story.find(class_="summary")
   
    
    if headline:
        story_dict['headline'] = headline.text.strip()
    if byline:
        story_dict['byline'] = byline.text.strip()
    if time:
        story_dict['time']= time.text.strip()
    if summary:
        story_dict['summary']=summary.text.strip()
    # there's a story without the url
    try:
        story_dict['url']= story.a['href']
    except:
        pass

    list_of_stories.append(story_dict)
    
###Test my list:
# list_of_stories

df = pd.DataFrame(list_of_stories)
right_now = datetime.datetime.now()
# This will set sth like NYT-briefing-2018-06-18-3PM.csv
file_date_string = right_now.strftime("%Y-%m-%d-%-I%p")
df.to_csv('NYT-briefing-{}.csv'.format(file_date_string), index=False)

# This set the email subject time: Here is your 6PM briefing
mail_date_string =right_now.strftime("%-I%p")




response = requests.post(
        "https://api.mailgun.net/v3/MY_DOMIAN/messages", 
        auth=("api", "MY_API_KEY"),
        files=[("attachment", open('NYT-briefing-{}.csv'.format(file_date_string)))],
        data={"from": "DIAN ZHANG <dz2383@columbia.edu>",
              "to": ["dz2383@columbia.edu"],
              "subject": 'Here is your {} briefing'.format(mail_date_string),
              "text": "Please check the attachment"}) 
              
response.text

