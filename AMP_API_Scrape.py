import sys
import re
import time
import urllib.request as urllib
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

Links = ('https://azuremarketplace.microsoft.com/api/v2.0/apps?api-version=2017-04-24', 'https://macwfe-prod-wus.mac-ase-prod-wus.p.azurewebsites.net/api/v2.0/apps?%24skiptoken=0_1&api-version=2017-04-24', 'https://macwfe-prod-wus.mac-ase-prod-wus.p.azurewebsites.net/api/v2.0/apps?%24skiptoken=0_2&api-version=2017-04-24', 'https://macwfe-prod-wus.mac-ase-prod-wus.p.azurewebsites.net/api/v2.0/apps?%24skiptoken=0_3&api-version=2017-04-24',
'https://macwfe-prod-wus.mac-ase-prod-wus.p.azurewebsites.net/api/v2.0/apps?%24skiptoken=0_4&api-version=2017-04-24',
'https://macwfe-prod-we.mac-ase-prod-we.p.azurewebsites.net/api/v2.0/apps?%24skiptoken=0_5&api-version=2017-04-24',
'https://macwfe-prod-we.mac-ase-prod-we.p.azurewebsites.net/api/v2.0/apps?%24skiptoken=0_6&api-version=2017-04-24')

Exit_F = open("ExportAMP with API 20180701.txt", 'w',encoding='utf-8')

for link in Links:

	r = urllib.urlopen(link).read().decode('utf-8','ignore')

	print(len(r))
	
	L = re.findall('{"ApplicationId":(.*?)"_attachments":"attachments/"',str(r))

	
	for l in range(0,len(L)):
		print(l)
					
		TI = re.findall('"Title":"(.*?)","',str(L[l]))
		if len(TI)==0:
			TI = ["N/A"]	
			
		PU = re.findall('"Publisher":"(.*?)","',str(L[l]))
		if len(PU)==0:
			PU = ["N/A"]
			
		PR = re.findall('"Product":"(.*?)","',str(L[l]))
		if len(PR)==0:
			PR = ["N/A"]	
	
		DA = re.findall('"ReleaseDate":"(.*?)","',str(L[l]))
		if len(DA)==0:
			DA = ["N/A"]
	
		ID = re.findall('"partitionKey":"(.*?)","',str(L[l]))
		if len(ID)==0:
			ID = ["N/A"]
			
		APPID = re.findall('^"(.*?)","',str(L[l]))
		if len(APPID)==0:
			APPID = ["N/A"]
			
		Exit_F.write(str(APPID[0])+"^"+str(TI[0])+"^"+str(PU[0])+"^"+str(PR[0])+"^"+str(DA[0])+"^"+str(ID[0]))
		Exit_F.write("\n")
		
		
	
Exit_F.close()