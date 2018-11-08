# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:17:34 2018

@author: Prem Sharma
"""

from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


def get_aqi():
    url = "http://aqicn.org/city/delhi/punjabi-bagh/"
    cont = requests.get(url, headers=headers, timeout=10)    
    soup = BeautifulSoup(cont.text,'lxml')
    pm25=soup.find(id='cur_pm25').get_text()
    pm10=soup.find(id='cur_pm10').get_text()
    
    return pm25,pm10
