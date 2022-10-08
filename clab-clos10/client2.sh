#!/bin/bash

ip link add link eth1 name eth1.1 type vlan id 1
ip link set eth1.1 up
ip a add 10.10.0.2/24 dev eth1.1
ip route add 1.1.1.1/32 via 10.10.0.254
ip route add 1.1.1.2/32 via 10.10.0.254
ip route add 2.2.2.2/32 via 10.10.0.254
ip route add 1.1.1.3/32 via 10.10.0.254
