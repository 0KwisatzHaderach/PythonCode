import pandas as pd, re, time, base64, urllib, sys, os, urllib, uuid
import requests, json
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

#CSV Line counter used for logging responses
csv_line = 1
#create a file that logs HTTP responses
f = open("TS_ChangeUserMail.txt", "w+")
#Change filepath to where you have the CSV on your machine
df = pd.read_csv('/Volumes/GoogleDrive/My Drive/GDocuments/Programming/TS_Change_User_Email/GroupeAdequatEmailChange.csv', chunksize=1, sep=';', header='infer', encoding='utf-8', index_col=False)
for chunk in df:
    csv_line += 1
    ConsumerKey    = 'OwnAccount' #default for all accounts in TS
    ConsumerSecret = 'OwnAccount' #default for all accounts in TS

    # Supplier API credentials
    TokenKey = str(chunk['TokenKey'].values[0]) 
    TokenSecret = str(chunk['TokenSecret'].values[0]) 
    Tenant = str(chunk['Tenant'].values[0]) 
    
    CurrentEmail = str(chunk['CurrentEmail'].values[0])
    
    UserId = str(chunk['UserId'].values[0])
    NewEmail = str(chunk['NewEmail'].values[0])
    FirstName = str(chunk['first_name'].values[0])
    LastName = str(chunk['last_name'].values[0])

    headers={}
    headers['X-Tradeshift-TenantId']     = Tenant
    headers['Accept']                    = 'application/json'
    headers['Content-Type']             = 'text/xml'

    #Change Email
    try:
        API_url = env_url + 'users/' + UserId
        #print(API_url)
        fileContent ='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                        <tns:UserProfile xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:tns="http://tradeshift.com/api/public/1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                            <tns:PersonParty>
                                <cac:Contact>
                                    <cbc:ElectronicMail>''' +NewEmail+ '''</cbc:ElectronicMail>
                                </cac:Contact>
                                <cac:Person>
                                    <cbc:FirstName>''' +FirstName+ '''</cbc:FirstName>
                                    <cbc:FamilyName>''' +LastName+ '''</cbc:FamilyName>
                                </cac:Person>
                            </tns:PersonParty>
                        </tns:UserProfile>'''
        #print(fileContent)
        call = put(API_url)
        print(call.content.decode('utf-8'))
        f.write(f'\nEmail changed from {CurrentEmail} to {NewEmail} on CSV line {csv_line}')
        print(f'Email changed from {CurrentEmail} to {NewEmail} on CSV line {csv_line}')
    except:
        f.write('\nEmail was not changed')
        print('Email was not changed')
    

