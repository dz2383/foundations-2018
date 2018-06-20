
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

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


# # I picked the NY Times

# In[2]:


response = requests.get('http://www.nytimes.com')
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


# url works here but doesn't work well in for loop

stories = doc.find_all(class_ ='story')
print(stories[0].h2.a['href'])
print(stories[1].h2.a['href'])


# # Put all in one cell:

# In[4]:


stories = doc.find_all(class_ ='story')
list_of_stories = []

for story in stories:
    story_dict = {}
    headline = story.find(class_='story-heading')
    byline = story.find(class_='byline')
    time =story.find(class_="timestamp")
    summary = story.find(class_="summary")
    # previous cell shows it should work but it doesn't
    # url = story.h2.a['href']
    if headline:
        story_dict['headline'] = headline.text.strip()
    if byline:
        story_dict['byline'] = byline.text.strip()
    if time:
        story_dict['time']= time.text.strip()
    if summary:
        story_dict['summary']=summary.text.strip()

    list_of_stories.append(story_dict)
    
###Test my list:
# list_of_stories

df = pd.DataFrame(list_of_stories)
right_now = datetime.datetime.now()
file_date_string = right_now.strftime("%Y-%b-%d_%-I%p")
df.to_csv('NYT_story_list{}.csv'.format(file_date_string), index=False)


mail_date_string =right_now.strftime()


response = requests.post(
        "https://api.mailgun.net/v3/MY_DOMAIN.mailgun.org/messages",
        auth=("api", "MY_API_KEY"),
        data={"from": "DIAN ZHANG <dz2383@columbia.edu>",
              "to": ["dz2383@columbia.edu"],
              "subject": "Here is your {} briefing".format,
              "text": "Please check the attachment"}) 
response.text

