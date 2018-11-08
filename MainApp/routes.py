# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:05:40 2018

@author: Prem Sharma
"""

from MainApp import app
from MainApp import scraping
from flask import render_template
import datetime



@app.route('/')
def index():
    nw = datetime.datetime.now()
    nw1 = nw.strftime('%H %p')
    pm_25,pm_10 = scraping.get_aqi()
    return render_template('index.html',pm25=pm_25,pm10=pm_10,dt=nw1)
    