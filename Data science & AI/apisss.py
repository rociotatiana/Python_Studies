#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:31:01 2021

@author: kala
"""
#### LAB




!pip install pycoingecko
!pip install plotly
!pip install mplfinance

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)


df.head()

df.mean()








from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id= 'bitcoin', vs_currency = 'usd', days = 30)

bitcoin_data = bitcoin_data['prices']
data = pd.DataFrame(bitcoin_data, columns =['TimeStamp', 'Price'])

data.max()

data['Date'] = pd.to_datetime(data['TimeStamp'], unit ='ms')

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 
                               'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x = candlestick_data.index, 
                                     open = candlestick_data['Price']['first'],
                                     high = candlestick_data['Price']['max'],
                                     low = candlestick_data['Price']['min'],
                                     close = candlestick_data['Price']['last'])])

fig.update_layout(xaxis_rangeslider_visible = False, xaxis_title = 'Date', 
                  yaxis_title = 'Price (USD $)',
                  title = 'Bitcoin Candlestick Chart Over Past 30 Days')

plot(fig, filename = 'bitcoin_candlestick_graph.html')



# SPEECH TO TEXT

url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"

iam_apikey_s2t = "EOeiZxxxDxV2xxxxxxxxxxxxxxxxxjYen9SKARKW-"

s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t, url = url_s2t) 

filename = "hello_this_is_python.wav"

with open(filename, mode = 'rb') as wav:
    response = s2t.recognize(audio=wav, content_type = 'audio/wav')
    
response.result

recognized_text = response.result['results'][0]['alternatives'][0]['transcript']

from ibm_watson import LanguageTranslatorV3

url_lt = 'https://gateway.watsonplatform.net/language-translator/api'

apikey_lt = 'dU2SaxxxxxxxxxxxxxxxdfCuasdf'

version_lt = '2018-05-01'

language_translator = LanguageTranslatorV3(iam_apikey = apikey_lt, url=url_lt, 
                                           version=version_lt)

language_translator.list_identifiable_languages().get_result()

#traducionedolo

translation_response = language_translator.translate(text=recognized_text, 
                                                     model_id = 'en-es')

translation = translation_response.get_result()

spanish_translation = translation['translations'][0]['translation']

translation_new = language_translator.translate(text=spanish_translation, 
                                                model_id = 'es-en').get_result()
translation_eng = translation_new['translations'][0]['translation']


###########


import requests

import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code

print(r.request.headers)

print("request body:", r.request.body)

header=r.headers
print(r.headers)

header['date']

header['Content-Type']

 r.encoding
 
 r.text[0:100]
 
 r=requests.get(url)
 
 print(r.headers)
 r.headers['Content-Type']
 
 path=os.path.join(os.getcwd(),'image.png')
path

with open(path,'wb') as f:
    f.write(r.content)
    
Image.open(path)



#### WEBSCRAPING

from bs4 import BeautifulSoup

