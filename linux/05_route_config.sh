#!/bin/bash

echo ========================================
echo `date`
echo ------------------------------
echo "source ~/.bashrc"
source /home/user/.bashrc
echo "route add -net 10.0.0.0/8 gw 10.92.36.1"
route add -net 10.0.0.0/8 gw 10.92.36.1
echo "route add -net 172.0.0.0/8 gw 10.92.36.1"
route add -net 172.0.0.0/8 gw 10.92.36.1
echo "route add -net 123.58.173.0/24 gw 10.92.36.1"
route add -net 123.58.173.0/24 gw 10.92.36.1
echo "route del default"
route del default
echo "route add default gw 192.168.42.129"
route add default gw 192.168.42.129

echo "route add -net 10.92.48.0/24 gw 192.168.42.129"
route add -net 10.92.48.0/24 gw 192.168.42.129
