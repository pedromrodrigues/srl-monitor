import requests
import os
import json
from json import JSONEncoder
import docker
from pygnmi.client import gNMIclient
#from gnmi import get

#r = os.system('curl -X GET --data "{"jsonrpc": "2.0","id":0,"method":"get"}')

class Container:
    def __init__(self, container_id, name, ip_address, ip6_address, image, state):
        self.container_id = container_id
        self.name = name
        self.ip_address = ip_address
        self.ip6_address = ip6_address
        self.image = image
        self.state = state

class Encoder(JSONEncoder):
    def default(self, j):
        return j.__dict__

def outras_cenas():
    url = "http://172.20.20.2/jsonrpc"

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/interface[name=ethernet-1/2]",
                "datastore": "state",
                "recursive": False
                }
            ]
        }
    }

    response = requests.get(url, auth=('admin', 'admin'), json=payload)
    print(response)

    payload2 = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "set",
        "params": {
            "commands": [
            {
                "action": "update",
                "path": "/interface[name=mgmt0]/description:trolololol"
            }
            ]
        }
    }

    url = 'http://localhost:8080/containers/json'

    response = requests.get(url)

    print(response)

    client = docker.from_env()

    client2 = docker.DockerClient(base_url='unix://var/run/docker.sock')

    #test = json.dumps(client2.containers.list())

    #print(test)

    containers_list = {}

    for container in client2.containers.list():

        cont = Container (
            container.short_id,
            container.name,
            container.attrs['NetworkSettings']['Networks']['clab']['IPAddress'],
            container.attrs['NetworkSettings']['Networks']['clab']['GlobalIPv6Address'],
            container.attrs['Config']['Image'],
            container.status
            )
        jsonize = json.dumps(cont, indent=4, cls=Encoder)
        print(jsonize)
        containers_list.append(jsonize)


    print(containers_list)

    aux = json.dumps(containers_list)

    print(aux)

class Interface(object):
    def __init__(self, name, admin_state, oper_state, oper_down_reason):
        self.name = name
        self.admin_state = admin_state
        self.oper_state = oper_state
        self.oper_down_reason = oper_down_reason

class IpVRF():
    def __init__(self, name, vrf_type, admin_state, oper_state, oper_down_reason):
        self.name = name
        self.vrf_type = vrf_type
        self.admin_state = admin_state
        self.oper_state = oper_state
        self.oper_down_reason = oper_down_reason

def main():

    #js = '''{"name":"Pedro", "address":{"street":"Sesame"}}'''
    #j = json.loads(js)
    #print(j)
    host = ('clab-clos01-leaf1', '57400')

    path = ['/interface[name=*]']
    target = "clab-clos10-leaf3:57400"

    url = "https://clab-clos10-leaf3:443/jsonrpc"

    if '10.10.0.2' in '10.10.0.20':
        print("TRUEEEEE")

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "commands": [
                {
                "path": "/ping-test/peer[ip=2.2.2.2-l3-vrf-1]",
                "datastore": "state",
                "recursive": True
                },
            ],
        }
    }

    macaca = ''

    if (macaca):
        print("TRUEEE")
    else:
        print("BOA")

    payload_2 = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "set",
        "params": {
            "commands": [
                {
                "action": "update",
                "path": "/ping-test/targets[IP-FQDN=10.10.0.6]",
                "value": {
                    "admin-state": "disable",
                    "network-instance": "l3-vrf-1",
                    "test-tool": "httping",
                    "number-of-tests": 2,
                    "source-ip": "2.2.2.2",
                }
                }
            ]
        }
    }

    #payload_2['params']['commands'][0]['value'].update(port=80)
    #print(payload_2['params']['commands'][0]['value'])

    certificate = '/home/pedro/Documents/evpn/clab-clos10/ca/leaf3/leaf3.pem'
    pkey = '/home/pedro/Documents/evpn/clab-clos10/ca/leaf3/leaf3-key.pem'

    cert = '/home/pedro/Documents/evpn/clab-clos10/ca/root/root-ca.pem'
    priv = '/home/pedro/Documents/clos01/clab-clos01/ca/root/root-ca-key.pem'

    response = requests.post(url, auth=('admin', 'admin'), json=payload, verify=cert)
    print(response.status_code)
    if (response.status_code == 200):
        print("NUMBER")
    elif (response.status_code == '200'):
        print('STRING')
    print(response)
    #print(response.json())

    x = response.json()
    print(x)
    print(x['result'][0]['targets'])

    for target in x['result'][0]['targets']:
        print('****', target)

    for netinst in x['result'][0]['peer']:
        print(netinst['ip'].split('-')[0])
        #if (netinst['ip'])
        print(x['result'][1]['targets'])

        for target in x['result'][1]['targets']:
            if target['IP-FQDN'] == netinst['ip'].split('-')[0]:
                print(target['admin-state'])
                print(netinst['last-update'])


    #x_object = json.loads(x)

    #x_format = json.dumps(x_object, indent=2)

    #print(x_format)

    #print(x)
    print("lllllllllllllllllllllllll")

    for interface in x['result'][0]['interface']:

        if 'neighbor' in interface.keys():
            for neighbor in interface['neighbor']:
                print("********")
                print(neighbor)
                print(interface['name'])
                print(neighbor['id'])
                print(neighbor['port-id'])
                print(neighbor['first-message'])
                print(neighbor['last-update'])
                print(neighbor['system-name'])
                print('******')

    print('--------------------')
    print(x['result'][0].keys())#['srl_nokia-interfaces:interface'])
    print('**************')
    print(x['result'][0]['neighbor'])
    print(x['result'][0]['interface'][0]['name'])
    print('********************')
    print(x['result'][0]['interface'][0]['neighbor'][0]['id'])
    print('***********************')
    print(x['result'][0]['interface'][0]['neighbor'][0]['port-id'])
    print('********************')
    print(x['result'][0]['interface'][0]['neighbor'][0]['first-message'])
    print('********************')
    print(x['result'][0]['interface'][0]['neighbor'][0]['last-update'])
    print('********************')
    print(x['result'][0]['interface'][0]['neighbor'][0].keys())
    print('********************')
    print(x['result'][0]['interface'][0]['neighbor'][0]['system-name'])




def macaco():
    interfaces = []

    for netinst in x['result'][0]['srl_nokia-network-instance:network-instance']:
        #print(netinst['name'])

        if 'oper-down-reason' in netinst.keys() and netinst['type'] == 'srl_nokia-network-instance:ip-vrf':
            print(netinst['type'])
            iface = IpVRF(
                netinst['name'],
                'ip-vrf',
                netinst['admin-state'],
                netinst['oper-state'],
                netinst['oper-down-reason']
                )
            interfaces.append(iface)
        elif netinst['type'] == 'srl_nokia-network-instance:ip-vrf':
            iface = IpVRF(
                netinst['name'],
                'ip-vrf',
                netinst['admin-state'],
                netinst['oper-state'],
                ' '
                )
            interfaces.append(iface)

    #print(interfaces)
    for iface in interfaces:
        print(iface.name)






    #for pf in x['result'][0]['srl_nokia-interfaces:interface']:
    #    print('***', pf['name'])
    #    if 'subinterface' in pf.keys():
    #        print('YES ', pf.get('subinterface'))

    #print('TESTE ----> ', x['result'][0]['srl_nokia-interfaces:interface']['subinterface'])

    #print(response.json()['result'])

    #print(response.json()['result'][0]['srl_nokia-interfaces:interface'][0])

    #print(macaco)

    #for notif in get(target, path, auth=("admin", "admin"), secure=False):
    #    prefix = notif.prefix
    #    print(prefix)



    #with gNMIclient(target=host, username='admin', password='admin', debug=True, insecure=True) as gc:
    #    result = gc.capabilities()

    #print(result)

if __name__ == "__main__":
    main()
    #normal = "clab-clos10-leaf3"
    #x = normal.split("-")
    #y = f"{x[0]}-{x[1]}"
    #print(x)
    #print(y)

            #- __clabDir__/leaf3/config/appmgr/new-yum/usr/lib/node_modules/npm/lib:/usr/lib/
            #- __clabDir__/leaf3/config/appmgr/new-yum/usr/lib/node_modules/npm/node_modules:/usr/bin/
