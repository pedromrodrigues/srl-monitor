#!/bin/bash

ip link add bond0 type bond
ip link set bond0 up
ip a add 10.10.0.1/24 dev bond0
ifenslave bond0 eth1 eth2
ip route add 1.1.1.1/32 via 10.10.0.254
ip route add 1.1.1.2/32 via 10.10.0.254
ip route add 2.2.2.2/32 via 10.10.0.254
ip route add 1.1.1.3/32 via 10.10.0.254
