import requests
import json
import os
import time

headers = {
	'Tenant': 'default_tenant',
	'Content-Type':'application/json',
	'Authentication-Token': 'WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkYncyQk1BYWcxQnBqakJGQzZGMEx3USQ3QkdxMnhFOTBpeGYvbzhwVUlyaXZicVp6TVVzRDZubGlqM2tzRS5NNC5NIl0.Xpu__g.xdSCwhX41dQKmhxvpiprPkmifPk'
}

def get_all(cfy_host):
    url = 'http://' + cfy_host + '/api/v1/quotas'
    print(url)
    resp = requests.get(url, headers=headers)
    print(resp.text)

get_all('192.168.174.120')

# token for admin
# WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkYncyQk1BYWcxQnBqakJGQzZGMEx3USQ3QkdxMnhFOTBpeGYvbzhwVUlyaXZicVp6TVVzRDZubGlqM2tzRS5NNC5NIl0.Xpu__g.xdSCwhX41dQKmhxvpiprPkmifPk
# token for user
# WyIxIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ05DNk55YWtWQXBCaUZGSzZaMXpiZyRQRThHNlNUTjYuMUdkZFpjZE1VOU9WZFIuLlNsLy50RHRqYjBjYjZHYlNvIl0.XpfSyg.JY3EXl6wKV_FTwmUfndiOES_Wl8
