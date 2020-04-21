import requests
import json
import os
import time

headers = {
	'Tenant': 'default_tenant',
	'Content-Type':'application/json',
	'Authentication-Token': 'WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkNVR4SGFNMTVqekZtREdGc0xhWFVtZyRjR3dKdDVLQm9WSW9RQzJRaGp0YXlFeEtyQkthZFBhaDZDUzJORGpRZjI4Il0.Xp5HbQ.vGV0krC1zEcegFVSqa1VY9-HBVc'
}

def get_all(cfy_host):
    url = 'http://' + cfy_host + '/meo/v1/quotas?_offset=1&_size=9'
    print(url)
    resp = requests.get(url, headers=headers)
    print(resp.text)

get_all('192.168.174.120')

# token for admin
# WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkM1p1emRpNmxWT3JkLjEuTGtiS1drZyRUajltWk04SVNRcTd6ZDNGa09xQ29Jamk3MWJrbDdzZ0liRWJqUW5RZFgwIl0.Xp2IOw.rIMPRbitwBrvUszDp3kXAqA6b9Y
# token for user
# WyIxIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ05DNk55YWtWQXBCaUZGSzZaMXpiZyRQRThHNlNUTjYuMUdkZFpjZE1VOU9WZFIuLlNsLy50RHRqYjBjYjZHYlNvIl0.XpfSyg.JY3EXl6wKV_FTwmUfndiOES_Wl8
