import requests
import json
import os
import time

headers = {
	'Tenant': 'default_tenant',
	'Content-Type':'application/json',
	'Authentication-Token': 'WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkYncyQk1BYWcxQnBqakJGQzZGMEx3USQ3QkdxMnhFOTBpeGYvbzhwVUlyaXZicVp6TVVzRDZubGlqM2tzRS5NNC5NIl0.Xpu__g.xdSCwhX41dQKmhxvpiprPkmifPk'
}

# mec-nodes
# data = {
# 	'mec_node_code': '010',
# 	'mepm_id': 'test',
# 	'network_type': 1,
# 	'status': 0,
# 	'address': 'beijing'
# }

# mepms
# data = {
# 	'access_ip': '192.168.1.1',
# 	'access_port': '9090',
# 	'version': '1.0.0',
# 	'provider': 'Chinatelecom',
# 	'area_code': '010',
# 	'address': 'Beijing'
# }

# vims
# data = {
# 	'type': 'openstack',
# 	'area_code': '010',
# 	'access_ip': '192.168.1.1',
# 	'access_port': '8080',
# 	'access_info': '{"end_porint":"test"}',
# 	'mepm_id': 'test',
# 	'properties': 'test'
# }

# resources
# data = {
# 	'all_value': 10,
# 	'alloc_value': 5,
# 	'unit': 'Gb',
# 	'mec_node_id': 'test',
# 	'resource_type': 'mem'
# }

# quotas
data = {
	'resource_id': 'test',
	'value': 10,
	'request_value': 5,
	'unit': 'Gb',
	'mec_node_id': 'test',
	'resource_type': 'mem'
}

def add_test(cfy_host, mepm_name):
	url = 'http://' + cfy_host + '/api/v1/quotas/' + mepm_name
	print(url)
	resp = requests.post(url, headers=headers, json=data)
	print(resp.text)

add_test('192.168.174.120','test')

# token for admin
# WyIwIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkYncyQk1BYWcxQnBqakJGQzZGMEx3USQ3QkdxMnhFOTBpeGYvbzhwVUlyaXZicVp6TVVzRDZubGlqM2tzRS5NNC5NIl0.Xpu__g.xdSCwhX41dQKmhxvpiprPkmifPk
# token for user
# WyIxIiwiJHBia2RmMi1zaGEyNTYkMjkwMDAkZ05DNk55YWtWQXBCaUZGSzZaMXpiZyRQRThHNlNUTjYuMUdkZFpjZE1VOU9WZFIuLlNsLy50RHRqYjBjYjZHYlNvIl0.XpfSyg.JY3EXl6wKV_FTwmUfndiOES_Wl8