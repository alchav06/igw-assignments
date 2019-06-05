# WPS Execute Operation

import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\intersection_wps_template.xml").read()

wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s6037054/igw_wps_assignment/wps.py?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)