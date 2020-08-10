# -*- coding: utf-8 -*-
import pandas as pd
import re, time, base64, urllib, sys, os, urllib, uuid
import requests, json
import urllib.parse
from requests_oauthlib import OAuth1

###############################################################################################################################
#API Details of the branch that created these passive accounts
#These can be taken from the API access to own account app in Tradeshift.
#
#Please make sure you use the correct API credentials as the api call will fail at the atuthentication/authorization phase
###############################################################################################################################

ConsumerKey    = 'OwnAccount' #default for all accounts in TS
ConsumerSecret = 'OwnAccount' #default for all accounts in TS

TokenKey       = 'Dz28pjQfK2-vxtgQjdB--xjVX6bmrM'                #Best Buy Master
TokenSecret    = 'jF@dTHd+X7DrcaNkXNADvbpGvvmWvhjEAaQUrVZc'        #Best Buy Master
#tenant         = '6dfe11f9-f14d-4c7c-8edf-564c12fcff95'            #Best Buy Master
tenant         = '1524f3f4-dd11-4299-a259-a23765f9e66d'            #Best Buy US

fileContent=''
headers={}
headers['X-Tradeshift-TenantId']     = tenant
headers['Accept']                    = 'text/plain'
headers['Content-Type']             = 'application/json'

def get(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.get(url, headers=headers, auth=auth)
    return response
def delete(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.delete(url, headers=headers, auth=auth)
    return response
def post(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.post(url, headers=headers, auth=auth, data=fileContent)
    return response
def put(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.put(url, headers=headers, auth=auth, data=fileContent)
    return response

#Change filepath to where you have the CSV on your machine
df = pd.read_csv('/Volumes/GoogleDrive/My Drive/GDocuments/Programming/TS_PassiveAccounts/F_BestBuySellers_PassiveUS.csv', chunksize=1, sep=';', header='infer', encoding='utf-8', index_col=False)
for chunk in df:
    email = ''.join(chunk['NewEmail'].values)
    #AccountingID = ''.join(chunk['CompanyAccountId'].values)
    #fileContent = '{"CompanyAccountId":"'+ AccountingID +'"}'
    url = 'https://api.tradeshift.com/tradeshift/rest/external/account/passive/puppet?email='+email
    print(url)
    #x = put(url)
    #print(x.status_code)
    #print(x.content.decode('utf-8'))