#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 01:45:51 2022

@author: nhinguyen
"""

import requests
import json
import boto3
import decimal
import schedule

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ds3002project2')
url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"

def insert(factor, pi, time):
    response = table.put_item(
        Item= {
            'factor': factor,
            'time': time,
            'pi': pi,
        }
    )


minute = 0   

def get():
    global minute   # so can access it locally
    minute += 1   # adds 1 every time it runs
    call = requests.get(url)
    info = json.loads(call.text, parse_float=decimal.Decimal)
    print(info)
    insert(info['factor'],info['pi'],info['time'])
        
get()

schedule.every(1).minute.do(get)  # scheduling to run get() once every minute

while True and minute < 60: # stop after 60 minutes
    schedule.run_pending()
    
    
    