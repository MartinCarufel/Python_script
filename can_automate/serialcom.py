'''
Created on Jun 5, 2019

@author: martin.carufel
'''
import serial
from time import sleep

ser = serial.Serial('COM13',115200)

sleep(2)
ser.write(b'freq=10\r\n')
sleep(3)
ser.write(b'freq=0\r\n')
sleep(1)
ser.flushInput()
ser.write(b'version?\r\n')
sleep(1)
r = ser.readline()
print r
ser.close()

