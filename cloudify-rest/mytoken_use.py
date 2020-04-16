import requests
import json
import os
import time

headers = {
	'Tenant': 'default_tenant',
	'Content-Type':'application/json',
	'Authentication-Token': 'WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ1hDT1VZcFJpdEhhLnguRGNPNGRJdyRUdUp3b1NwVTdQQlJSemo4V1pvT1kueC5GM2ZONjFsWGs5cjVpSmZjTTRvIl0.XpfP4Q.hmJzZmKsE_XKRGH7laR7GQjBaxk'
}

def use_token(cfy_host):
    url = 'http://' + cfy_host + '/api/v3/secrets'
    print(url)
    resp = requests.get(url, headers=headers)
    print(resp.text)

use_token('192.168.63.130')

# token for admin
# WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ1hDT1VZcFJpdEhhLnguRGNPNGRJdyRUdUp3b1NwVTdQQlJSemo4V1pvT1kueC5GM2ZONjFsWGs5cjVpSmZjTTRvIl0.XpfP4Q.hmJzZmKsE_XKRGH7laR7GQjBaxk
# token for user
# WyIxIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ05DNk55YWtWQXBCaUZGSzZaMXpiZyRQRThHNlNUTjYuMUdkZFpjZE1VOU9WZFIuLlNsLy50RHRqYjBjYjZHYlNvIl0.XpfSyg.JY3EXl6wKV_FTwmUfndiOES_Wl8