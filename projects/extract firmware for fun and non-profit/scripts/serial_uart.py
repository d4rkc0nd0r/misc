#!/usr/bin/python3

import serial

# this script works in linux as well as windows
# for serial port, check /dev/ttyUSB* in linux and device manager in windows
# this script automates to read from bootloader rather than doing it manually

baud_rate = 115200 # baud rate
serial_port = 'COM5' # you have to change this serial port
s = serial.Serial(serial_port, baud_rate)
data = s.readline(1000)

print(data)
