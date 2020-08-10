# -*- coding: utf-8 -*-
###############################################################################################################################################################################################################################################################
# Documentation for the script in progress
###############################################################################################################################################################################################################################################################
import pandas as pd
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

csv_choice()

#CSV Line counter used for logging responses
csv_line = 1
#create a file that logs HTTP responses
f = open("TS_DeleteDocuments.txt", "w+")
#Change filepath to where you have the CSV on your machine
df = pd.read_csv(r'C:\Users\Offline\Downloads\Bulk delete LOREAL -SZAIDEL 2.csv', chunksize=1, sep=',', header='infer', encoding='utf-8', index_col=False)
for chunk in df:
    csv_line += 1
    ConsumerKey    = 'OwnAccount' #default for all accounts in TS
    ConsumerSecret = 'OwnAccount' #default for all accounts in TS


    # Supplier API credentials and file deletion
    TokenKey = str(chunk['SupplierTokenKey'].values[0]) #API Access to Own account
    #print(TokenKey)
    TokenSecret = str(chunk['SupplierTokenSecret'].values[0]) #API Access to Own account
    #print(TokenSecret)
    Tenant = str(chunk['SupplierTenant'].values[0]) #Tenant ID for account that created the passive accounts
    #print(Tenant)
    DocNr = str(chunk['DocNr'].values[0]) #INV/CRN document number as it is in Tradeshift.
    #print(DocNr)

    headers={}
    headers['X-Tradeshift-TenantId']     = Tenant
    headers['Accept']                    = 'application/json'
    headers['Content-Type']             = 'application/json'

    
    url = f'{env_url}documents?businessId={DocNr}'
    x = get(url) #Make API call

    f.write(f'Supplier HTTP (200 expected) response for DocNr {DocNr} on line {csv_line} was {x.status_code}\n\n')
    #f.write(x.content.decode('utf-8')+'\n\n')
    # print(x.status_code)
    # print(x.content.decode('utf-8'))

    response = x.json() #convert response to scriptable JSON
    try:
        DocumentId = response['Document'][0]['DocumentId'] #Get DocumentId from response
        url = env_url + f'documents/{DocumentId}/content'
        x = delete(url)
        f.write(f'Supplier HTTP (204 expected) response for DocumentId {DocumentId} on line {csv_line} was {x.status_code}\n\n')
        print(f"Document {DocNr} was deleted from supplier account")
    except:
        print(f"Document {DocNr} not in supplier account")
        f.write(f"Document {DocNr} not in supplier account")
    #Buyer API credentials and document removal
    TokenKey = str(chunk['BuyerTokenKey'].values[0]) #API Access to Own account
    #print(TokenKey)
    TokenSecret = str(chunk['BuyerTokenSecret'].values[0]) #API Access to Own account
    #print(TokenSecret)
    Tenant = str(chunk['BuyerTenant'].values[0]) #Tenant ID for account that created the passive accounts
    #print(Tenant)
    DocNr = str(chunk['DocNr'].values[0]) #INV/CRN document number as it is in Tradeshift.
    #print(DocNr)

    headers={}
    headers['X-Tradeshift-TenantId']     = Tenant
    headers['Accept']                    = 'application/json'
    headers['Content-Type']             = 'application/json'

    url = env_url+'documents?businessId='+DocNr
    #+'&sentBy='+str(chunk['SupplierTenant'].values[0])
    x = get(url)
    f.write(f'Buyer HTTP (200 expeected) response for DocNr {DocNr} on line {csv_line} was {x.status_code}\n' )
    

    response = x.json() #convert response to scriptable JSON
    try: 
        DocumentId = response['Document'][0]['DocumentId'] #Get DocumentId from response
        url = f'{env_url}documents/{DocumentId}/content'
        x = delete(url)
        f.write(f'Buyer HTTP (204 expected) response for DocumentId {DocumentId} on line {csv_line} was {x.status_code}\n\n\n')
        print(f"Document {DocNr} was deleted from buyer account")
    except:
        print(f"Document {DocNr} not in buyer account")
        f.write(f"Document {DocNr} not in buyer account")
    
    
print('Script is done! Please see the Passive_Accounts_responses.txt for a full overview of API calls.')
f.close() #close logging file
