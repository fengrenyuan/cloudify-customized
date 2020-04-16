import requests
import json
import os
from requests.auth import HTTPBasicAuth
import time

headers = {
	'Tenant': 'default_tenant',
	'Content-Type':'application/json'
}
username = 'lzy'
password = 'admin'

def get_token(cfy_host):
    url = 'http://' + cfy_host + '/api/v1/tokens'
    print(url)
    resp = requests.get(url, auth=HTTPBasicAuth(username,password), headers=headers)
    print(resp.text)

get_token('192.168.63.130')