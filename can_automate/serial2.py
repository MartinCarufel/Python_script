'''
Created on Jun 5, 2019

@author: martin.carufel
'''

import serial


from time import sleep

ser2 = serial.Serial('COM2',115200)
ser6 = serial.Serial('COM6',115200)
sleep(.1)
print 'COM2: {} {} {} {}' .format(ser2.baudrate, ser2.bytesize, ser2.parity, ser2.stopbits)
print 'COM6: {} {} {} {}' .format(ser6.baudrate, ser6.bytesize, ser6.parity, ser6.stopbits)
ser2.flushInput()
ser6.flushInput()

ser2.write(b'allo\n')
ser2.write(b'allo\n')
ser2.write(b'allo\n')
sleep(.2)
buffCount = ser6.inWaiting()
r = ser6.read(buffCount)
ser2.flushInput()
ser6.flushInput()
# r3 = ser6.readline()
print r
# print r2
# print r3
ser2.close()
ser6.close()

