# -*- coding: utf-8 -*-
###############################################################################################################################################################################################################################################################
# Documentation for the script can be found https://tradeshift.atlassian.net/wiki/spaces/SS/pages/1699741764/Script+for+changing+Email+address+on+Passive+accounts+via+API+call
###############################################################################################################################################################################################################################################################
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
    sandbox = "https://api-sandbox.tradeshift.com/tradeshift/rest/external/"
    production = "https://api.tradeshift.com/tradeshift/rest/external/"
    env_choice = False
    while env_choice == False:
        environment = input("choose environment to run the script it (0 for Sanbox and 1 for Proudction): ")
        if environment == "0":
            env_url = sandbox
            env_choice = True
        elif environment == "1":
            env_url = production
            env_choice = True
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
#CSV Line counter used for logging responses
csv_line = 1
#create a file that logs HTTP responses
try:
    f = open("TS_Passive_Accounts_responses.txt", "w+")
    csv_log = open("TS_Passive_Accounts_Results.csv", "w+")
except:
    print("could not create log files")


#Change filepath to where you have the CSV on your machine
df = pd.read_csv(r'/Users/alexandru.marton/Downloads/NHSPS Email Passive Upload 26-5-2020.csv', chunksize=1, sep=separator, header='infer', encoding='utf-8', index_col=False, dtype=str)

for chunk in df:
    csv_line += 1
    ConsumerKey    = 'OwnAccount' #default for all accounts in TS
    ConsumerSecret = 'OwnAccount' #default for all accounts in TS
    TokenKey = str(chunk['BuyerToken'].values[0]) #API Access to Own account
    #print(TokenKey)
    TokenSecret = str(chunk['BuyerSecret'].values[0]) #API Access to Own account
    #print(TokenSecret)
    Tenant = str(chunk['BuyerTenantID'].values[0]) #Tenant ID for account that created the passive accounts
    #print(Tenant)
    NewEmail = str(chunk['InvitationEmail'].values[0])
    #print(NewEmail)
    UserAccessGroup = str(chunk['PassiveSupplierBranchID'].values[0]) #See documentation on where to find this value https://tradeshift.atlassian.net/wiki/spaces/SS/pages/1699741764/Script+for+changing+Email+address+on+Passive+accounts+via+API+call
    
    headers={}
    headers['X-Tradeshift-TenantId']     = Tenant
    headers['Accept']                    = 'text/plain'
    headers['Content-Type']             = 'application/json'

    fileContent = '{"CompanyAccountId":"'+ UserAccessGroup +'"}'

    url = env_url+'account/passive/puppet?email='+NewEmail
    x = put(url)
    try:
        chunk['HTTPCode'].values[0] = x.status_code
    except:
        print("HTTPCode column does not exist in the CSV file")
    try:
        chunk['HTTPResponse'].values[0] = str(x.content.decode('utf-8'))
    except:
        print("HTTPResponse column does not exist in the CSV file")
    try:
        f.write(str(x.status_code)+ 'HTTP response for email '+NewEmail+' on line '+str(csv_line)+'\n')
        f.write(x.content.decode('utf-8')+'\n\n')
        chunk.to_csv('Passive_Accounts_Results.csv',mode='a',index=False, header=False)
    except:
        print("could not write log files")
    print(x.status_code)
    print(x.content.decode('utf-8'))

print('Script is done! Please see the Passive_Accounts_responses.txt for a full overview of API calls. 200 is OK, anything else means there was an error most likely')
#close logging file
f.close()
csv_log.close()