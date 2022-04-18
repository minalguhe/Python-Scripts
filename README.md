# Python-Scripts

#!/usr/bin/python
import csv
import requests
import time
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin

edgerc = EdgeRc('~/.edgerc')
section = 'default' # Section in edgerc file
baseurl = 'https://%s' % edgerc.get(section, 'host') # Extracting hostname from edgerc file

with open('<filename.csv>', 'r') as f: #Replace <filename.csv> with path+filename
	reader = csv.reader(f)
	data = list(reader) # creating the initial list of all URLs from the CSV

total_count = len(data) # checking the length of the list created
new_data = []

# Creating list of comma separated URLs
for n in range(0, total_count):
	obj_data = data[n]
	new_data.append(obj_data[0])

# Function to purge using URLs (200 at a time)
def purge(): 
	N = 0
	if N <= total_count:
		for i in range(N, N + 200): # creating for loop to purge 200 URLs at once
			payload = {"objects": new_data[N:N+200]}
			headers = {
    			"Accept": "application/json",
    			"Content-Type": "application/json"
			}
			s = requests.Session()
			s.auth = EdgeGridAuth.from_edgerc(edgerc, section)
			result = s.post(urljoin(baseurl, '/ccu/v3/delete/url/<network>'), json=payload, headers=headers) #Replace <network> with 'staging' or 'production'
			N = N + 200
			print(result.text)
		print(payload) 

purge() # Function call
