import pandas as pd
import re, time, base64, urllib, sys, os, urllib, uuid
import requests, json
import urllib.parse
from requests_oauthlib import OAuth1

fileContent =''
headers = {}

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

def environment():
    sandbox = "https://api-sandbox.tradeshift.com/tradeshift/rest/external/"
    production = "https://api.tradeshift.com/tradeshift/rest/external/"
    environment = input("choose environment to run the script it (0 for Sanbox and 1 for Proudction): ")
    if environment == "0":
        env_url = sandbox
    elif environment == "1":
        env_url = production
    else:
        print('please input 0 or 1 as your choice')
    return env_url

env_url = environment()

def csv_choice():
    choice = False
    while choice == False:
        separator = str(input("Please choose CSV separator (, or ;): "))
        if separator == ',' or separator == ';':
            choice = True
    return separator

separator = csv_choice()

csv_line = 1 #CSV Line counter used for logging responses

f = open("TS_DeleteConnection.txt", "w+")
csv_log = open("TS_DeleteConnection.csv", "w+")

#Attention!! Change filepath to where you have the CSV on your machine
df = pd.read_csv('/Volumes/GoogleDrive/My Drive/GDocuments/Programming/TS_DeleteConnection/RemovePassiveConnections.csv', chunksize=1, sep=';', header='infer', encoding='utf-8', index_col=False)
for chunk in df:
    csv_line += 1
    f.write("\n\nRunning script for CSV line"+str(csv_line))
    ConsumerKey    = 'OwnAccount' #default for all accounts in TS
    ConsumerSecret = 'OwnAccount' #default for all accounts in TS
    TokenKey = str(chunk['BuyerToken'].values[0]) #API Access to Own account
    TokenSecret = str(chunk['BuyerSecret'].values[0]) #API Access to Own account
    Tenant = str(chunk['BuyerTenantID'].values[0]) #Tenant ID for account that created the passive accounts
    PassiveConnectionID = str(chunk['PassiveConnectionID'].values[0]) #Connection ID to search for in Tradeshift
    
    #Get passive connection properties
    headers={}
    headers['X-Tradeshift-TenantId']     = Tenant
    headers['Accept']                    = 'application/json' #'application/json' required for JSON response
    headers['Content-Type']             = 'application/json'

    url_delete_passive_connection =env_url+'network/connections/'+PassiveConnectionID
    call = delete(url_delete_passive_connection)
    f.write(str(call.status_code)+ f'\nHTTP response for Connection {PassiveConnectionID} on line {csv_line}')
    f.write('\n'+call.content.decode('utf-8'))
    print(call.status_code)
    print(call.content.decode('utf-8'))

print('Script is done! Please see the Passive_Accounts_responses.txt for a full overview of API calls. 200 is OK, anything else means there was an error most likely')
#close logging file
f.close()
csv_log.close()