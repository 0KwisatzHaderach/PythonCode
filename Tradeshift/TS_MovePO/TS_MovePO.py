import pandas as pd
import csv
import re, time, base64, urllib, sys, os, urllib, uuid
import requests, json
import urllib.parse
from requests_oauthlib import OAuth1


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
    f_env_url = ''
    sandbox = "https://api-sandbox.tradeshift.com/tradeshift/rest/external/"
    production = "https://api.tradeshift.com/tradeshift/rest/external/"
    env_choice = False
    while env_choice == False:
        environment = input("choose environment to run the script it (0 for Sanbox and 1 for Proudction): ")
        if environment == "0":
            f_env_url = sandbox
            env_choice = True
        elif environment == "1":
            f_env_url = production
            env_choice = True
    return f_env_url


env_url = environment()

def csv_choice():
    f_separator = ''
    choice = False
    while choice == False:
        f_separator = str(input("Please choose CSV separator (, or ;): "))
        if f_separator == ',' or f_separator == ';':
            choice = True
    return f_separator

separator = csv_choice()
#CSV Line counter used for logging responses
csv_line = 1
#create a file that logs HTTP responses
f = open("TS_MovePO.txt", "w+")
csv_log = open("TS_MovePO.csv", "w+")


#Change filepath to where you have the CSV on your machine
df = pd.read_csv('/Users/alexandru.marton/Downloads/NHSPS-Email Amends.csv', chunksize=1, sep=separator, header='infer', encoding='utf-8', index_col=False, dtype=str)

for chunk in df:
    csv_line += 1
    ConsumerKey    = 'OwnAccount' #default for all accounts in TS
    ConsumerSecret = 'OwnAccount' #default for all accounts in TS
    TokenKey = str(chunk['BuyerToken'].values[0]) #API Access to Own account

    TokenSecret = str(chunk['BuyerSecret'].values[0]) #API Access to Own account

    Tenant = str(chunk['BuyerTenantID'].values[0]) #Tenant ID for account that created the passive accounts

    BuyerDocUUID = str(chunk['BuyerDocUUID'].values[0])
    DispatchID = str(chunk['DispatchID'].values[0])
    ActiveConnectionID = str(chunk['ActiveConnectionID'].values[0])
    
    headers={}
    headers['X-Tradeshift-TenantId']     = Tenant
    headers['Accept']                    = 'text/plain'
    headers['Content-Type']             = 'application/json'

    fileContent = '{"ConnectionId":"'+ ActiveConnectionID +'"}'

    url = env_url+'documents/'+BuyerDocUUID+'/dispatches/'+DispatchID
    x = put(url)
    chunk['HTTPCode'].values[0] = x.status_code
    chunk['HTTPResponse'].values[0] = str(x.content.decode('utf-8'))

    f.write(str(x.status_code)+ 'HTTP response for Document '+BuyerDocUUID+' on line '+str(csv_line)+'\n')
    f.write(x.content.decode('utf-8')+'\n\n')
    print(x.status_code)
    print(x.content.decode('utf-8'))
    chunk.to_csv('TS_MovePO.csv',mode='a',index=False, header=False)

print('Script is done! Please see the TS_MovePO.txt for a full overview of API calls. 200 is OK, anything else means there was an error most likely')
#close logging file
f.close()
csv_log.close()