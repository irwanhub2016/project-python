#!/bin/bash

c=$(python read_sensor.py)
b=$(cat /sys/class/net/eth0/address)

echo -e "{\"mac_address\":$b,\"sensor_value\":$c}"

