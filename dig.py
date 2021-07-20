#!/usr/bin/python
import csv
import os

with open('/Users/mguhe/Desktop/Oly Hostname WAF.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

domains = []
result = []
dns ={}

#create clean list of input domain names
for i in data:
	item = str(i)
	item = (item.replace("\\xef\\xbb\\xbf", ""))
	item = (item.replace('[', ''))
	item = (item.replace(']', ''))
	item = (item.replace('\'', '', 2))
	domains.append(item)

#create DNS result output list
for d in domains:
	output = os.popen('dig '+ d + ' +short').read()
	# print (type(output))
	result.append(output)

#create dictionary
for key in domains:
    for value in result:
        dns[key] = value
        result.remove(value)
        break

#write to csv
with open('/Users/mguhe/Desktop/dig_output.csv', 'wb') as f:
    writer = csv.writer(f)
    for key, value in dns.items():
    	writer.writerow([key, value])

    f.close()
    
	





