# This is a python script for creating unique links as described on the Trustpilot website below:
# https://support.trustpilot.com/hc/en-us/articles/204953148-Send-invitations-with-Unique-Links
# The ULGen function will generate the unique links and print them to the console as well as return the unique link
# A CSV file can be setup to contain the necessary columns and have the unique link written in the last column 

import urllib.request
import base64
import hashlib
import pandas as pd


def ULGen(TPS: str,CDN: str,SecretKey: str,Mail: str, UName: str, Refnr: str, ):

	
	B64_EMail = base64.urlsafe_b64encode(bytes(Mail, "utf-8")).decode('ASCII')
	url_UName = str(urllib.request.pathname2url(UName))
	SHA_url = str((hashlib.sha1((SecretKey+Mail+Refnr).encode("utf-8"))).hexdigest())

	UniqueLink = f"https://{TPS}/evaluate/{CDN}?a = {Refnr}&b = {B64_EMail}&c = {url_UName}&e = {SHA_url}"
	print(f"Unique link generated for {Mail} is {UniqueLink}")
	return UniqueLink

#print (ULGen('mail@customer.com', 'Customer Name', 'OID-123')) #Print sample link

