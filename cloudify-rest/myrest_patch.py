import requests
import json
import os
import time

headers = {
	'Tenant': 'default_tenant',
	'Content-Type':'application/json',
	'Authentication-Token': 'WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkNVR4SGFNMTVqekZtREdGc0xhWFVtZyRjR3dKdDVLQm9WSW9RQzJRaGp0YXlFeEtyQkthZFBhaDZDUzJORGpRZjI4Il0.Xp5HbQ.vGV0krC1zEcegFVSqa1VY9-HBVc'
}

data = {
	'MepmInfo': {
		'version': '2.0.0'
	}
}

def add_test(cfy_host, mepm_name):
    url = 'http://' + cfy_host + '/api/v1/mepms/' + mepm_name
    resp = requests.patch(url, headers=headers, json=data)
    print(resp.text)

add_test('192.168.174.120','test2')

# token for admin
# WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkYncyQk1BYWcxQnBqakJGQzZGMEx3USQ3QkdxMnhFOTBpeGYvbzhwVUlyaXZicVp6TVVzRDZubGlqM2tzRS5NNC5NIl0.Xpu__g.xdSCwhX41dQKmhxvpiprPkmifPk
# token for user
# WyIxIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ05DNk55YWtWQXBCaUZGSzZaMXpiZyRQRThHNlNUTjYuMUdkZFpjZE1VOU9WZFIuLlNsLy50RHRqYjBjYjZHYlNvIl0.XpfSyg.JY3EXl6wKV_