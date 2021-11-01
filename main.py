CLIENT_ID = 'icyWDqKFjJ-yyKmtZpOugQ'
SECRET_KEY = 'Eav5ILz4lmBFnmcQqwsrs0dMEp9Kyw'

import requests
from requests.api import request
import pandas as pd
from gtts import gTTS
from moviepy.editor import *

import os
import time
import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

auth = requests.auth.HTTPBasicAuth(CLIENT_ID,SECRET_KEY)
data = {'grant_type':'password','username':'adzaaDev','password':'Adamko1997'}
headers = {'User-Agent':'MyApi/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth,data=data,headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'
res = requests.get('https://oauth.reddit.com/r/confession/new',headers=headers,params={'limit':'20'})
results_json = res.json()
df = pd.DataFrame()
for post in res.json()['data']['children']:
    df = df.append({
        'subredit':post['data']['subreddit'],
        'title':post['data']['title'],
        'selftext':post['data']['selftext']
        },ignore_index=True)

df.to_csv('reddit_articles.csv')

text = ""
for i in res.json()['data']['children']:
    text = i['data']['title'],



def text_to_speech(text):
    text = ''.join(text)
    mytext = text

    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)

    text  = myobj.save("welcome.mp3")
    audio_text = AudioFileClip("welcome.mp3")
    return audio_text



def make_a_video():
    audio_text = text_to_speech(text)
    img = ['lion.png']

    clips = [ImageClip(m).set_duration(2)
        for m in img]

    concat_clip = concatenate_videoclips(clips, method="compose",)
    concat_clip = concat_clip.set_audio(audio_text)
    concat_clip.write_videofile("test_with_audio2.mp4", fps=24)


text_to_speech(text)
make_a_video()
