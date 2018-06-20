
# coding: utf-8

# # Using APIs/Data Structures
# Using the Dark Sky Forecast API at https://developer.forecast.io (Links to an external site.)Links to an external site./, generate a sentence that describes the weather that day.
# 
# Right now it is TEMPERATURE degrees out and SUMMARY. Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.
# 
# TEMPERATURE is the current temperature
# SUMMARY is what it currently looks like (partly cloudy, etc - it's "summary" in the dictionary). Lowercase, please.
# TEMP_FEELING is whether it will be hot, warm, cold, or moderate. You will probably use HIGH_TEMP and your own thoughts and feelings to determine this.
# HIGH_TEMP is the high temperature for the day.
# LOW_TEMP is the low temperature for the day.
# RAIN_WARNING is something like "bring your umbrella!" if it is going to rain at some point during the day.
# You can take a look at the documentation, but "current" contains the current conditions and the first element of "daily" is for the current day. But you knew that, right?!
# 
# Feel free to steal your old code! I bet that trying to read it will make you depressed and teaches you the value of naming variables.
# 
# Once you've accomplished that part, use Mailgun to send yourself an email every morning at 8AM telling you the sentence. The subject line of the email should be something like "8AM Weather forecast: January 1, 1970."
# 
# Dates are obtained by doing something like this, using http://strftime.org/ as a reference:
# 
# import datetime
# right_now = datetime.datetime.now()
# date_string = right_now.strftime("%Y-%M")
# BONUS: List the forecasted temperatures as the day goes on.
# 
# 

# In[ ]:


import requests


# # Send Via API

# In[2]:


### Will use these code later!


# response = requests.post(
#         "https://api.mailgun.net/v3/MY_DOMAIN/messages",
#         auth=("api", "MYAPIKEY"),
#         data={"from": "DIAN ZHANG <dz2383@columbia.edu>",
#               "to": ["dz2383@columbia.edu"],
#               "subject": "Hello",
#               "text": "Testing some Mailgun awesomness!"}) 
# response.text


# # Dark Sky API

# In[3]:


url ='https://api.darksky.net/forecast/MY_API_KEY/40.785091,-73.968285'
response = requests.get(url)
response


# In[4]:


# make it look like a dictionary
data = response.json()
data


# In[5]:


data.keys()


# In[6]:


data['currently']


# In[7]:


data['daily'].keys()


# In[8]:


# Right now it is TEMPERATURE degrees out and SUMMARY. 
# TEMPERATURE:
temperature = (data['currently']['apparentTemperature'])
print(temperature)
# SUMMARY:
summary = data['currently']['summary']
summary


# In[9]:


# I defined: 
# Cold: 55 degrees and below

# Cool: 56 to 65 degrees

# Mild: 66 to  75 degrees

# Warm: 75 to 85 degrees

# Hot: Above 85 degrees


# In[10]:


high_temp = data['daily']['data'][0]['temperatureHigh']
high_temp


# In[11]:


low_temp = data['daily']['data'][0]['temperatureLow']
low_temp


# In[12]:


if high_temp >= 85:
    temp_feeling = "hot"
elif 75<= high_temp <85:
    temp_feeling ="warm"
elif 66 <= high_temp <75:
    temp_feeling="mild"
elif 56<= high_temp<66:
    temp_feeling="cool"
elif high_temp <56:
    temp_feeling="cold"

temp_feeling


# In[13]:


data['daily']['data'][0]['icon']


# In[48]:


daily_summary = data['daily']['data'][0]['icon']

if daily_summary =="rain":
    rain_warning = "Bring your umberalla!"
else:
    rain_warning = "It won't rain today!"
    


# In[49]:


rain_warning


# In[36]:


# Right now it is TEMPERATURE degrees out and SUMMARY. 
# Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.

# TEMPERATURE is the current temperature
# SUMMARY is what it currently looks like (partly cloudy, etc - it's "summary" in the dictionary). Lowercase, please.
# TEMP_FEELING is whether it will be hot, warm, cold, or moderate. You will probably use HIGH_TEMP and your own thoughts and feelings to determine this.
# HIGH_TEMP is the high temperature for the day.
# LOW_TEMP is the low temperature for the day.
# RAIN_WARNING is something like "bring your umbrella!" if it is going to rain at some point during the day.


# # This is the final sentences I generated:

# In[61]:


# I want to generate sentences:

weather_text = "Right now it is {} F degrees out and {}. Today will be {} with a high of {} and a low of {} F degree. {}".format(temperature,summary,temp_feeling,high_temp,low_temp,rain_warning)
print(weather_text)


# # Set time

# In[63]:


# %B month
# %d day
#% Y
### useful website: http://strftime.org/

import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B-%d-%Y")


# # Send the actual weather email!

# In[66]:


subject_text = "8AM Weather forecast: {}".format(date_string)


# In[67]:


response = requests.post(
        "https://api.mailgun.net/v3/mysandbox.mailgun.org/messages",
        auth=("api", "MY_API"),
        data={"from": "DIAN ZHANG <dz2383@columbia.edu>",
              "to": ["dz2383@columbia.edu"],
              "subject": subject_text,
              "text": weather_text}) 
response.text


# In[ ]:


# Because of submitting it online, I removed the API key and my sandbox domain 

