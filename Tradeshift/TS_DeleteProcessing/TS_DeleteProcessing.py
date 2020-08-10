# -*- coding: utf-8 -*-
###############################################################################################################################################################################################################################################################
# Documentation for the script can be found https://tradeshift.atlassian.net/wiki/spaces/SS/pages/1699741764/Script+for+changing+Email+address+on+Passive+accounts+via+API+call
###############################################################################################################################################################################################################################################################
import pandas as pd
import re, time, base64, urllib, sys, os, urllib, uuid
import requests, json
import urllib.parse
from requests_oauthlib import OAuth1

ConsumerKey    = 'OwnAccount'
ConsumerSecret = 'OwnAccount'

TokenKey       = '87aDDyNQ5SGKkT+5GnzBZT6t5xuC5f'
TokenSecret    = 'T-phd+b3pZCz9w7YgMH59gha-Frac8MNj2v5m3jn'
tenant         = '29c3fe9b-f40b-46f3-a3d0-b045be255bab'

headers        = {'Accept' : 'application/json',
				'X-Tradeshift-TenantId' : tenant,
				'Content-Type' : 'text/xml'}

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
        return env_url
    elif environment == "1":
        env_url = production
        return env_url
    else:
        print('please input 0 or 1 as your choice')
    return env_url

env_url = environment()

def deleteAll():
	stuck = ''
	count = 0
	pageLimit = 0
	currentPage = 0
	url = env_url + 'documentfiles?directory=processing&limit=100&page='+str(pageLimit)
	for i in re.findall(r'"numPages" : (.*?),', str(get(env_url + 'documentfiles?directory=processing&limit=100&page=0'))):
		pageLimit = int(i)-1
	while currentPage <= pageLimit:
		url = env_url + 'documentfiles?directory=processing&limit=100&page='+str(currentPage)
		stuck += str(get(url))
		currentPage +=1
	howMany = len(re.findall(r'"FileName" : "(.*?)",', stuck))
	for i in re.findall(r'"FileName" : "(.*?)",', stuck):
		url = env_url + 'documentfiles/'+str(i)+'/file?directory=processing'
		count +=1
		if delete(url) == 204:
			print(str(count)+'/'+str(howMany), i)
		else:
			print(i, 'deleting failed')
def deleteOne(fileName):
	url = env_url + 'external/documentfiles/'+str(fileName)+'/file?directory=processing'
	if delete(url) == 204:
		print('Deleting', fileName, 'was successful.')
	else:
		print('Deleting', fileName, 'failed.')



files_to_delete = str(input("do you want to delete all files in processing folder? Y/N "))

if files_to_delete.upper() == "Y":
    deleteAll()
elif files_to_delete.upper() == "N":
    my_file = input("input filename: ")
    deleteOne(my_file)
else:
    print("must input Y or N")