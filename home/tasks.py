from __future__ import absolute_import,unicode_literals

from celery import shared_task
from learning.celery import app
import gspread,os
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path




@shared_task
def add(x,y):
    return x+y
@app.task
def dataadd(arr,index):
    BASE_DIR = Path(__file__).resolve().parent.parent


    # use creds to create a client to interact with the Google Drive API
    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name( os.path.join(BASE_DIR, 'Atlan-796bf7f3a01e.json'), scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("edit").sheet1
    sheet.insert_row(arr,index)

@app.task
def coladd(arr):
    BASE_DIR = Path(__file__).resolve().parent.parent


    # use creds to create a client to interact with the Google Drive API
    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name( os.path.join(BASE_DIR, 'Atlan-796bf7f3a01e.json'), scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("edit").sheet1
    sheet.update_cell(1,1,arr[0])
    sheet.update_cell(1,2,arr[1])
    sheet.update_cell(1,3,arr[2])
    sheet.update_cell(1,4,arr[3])
    sheet.update_cell(1,5,arr[4])

