import serial


from time import sleep

ser2 = serial.Serial('COM2',1200)
ser2.flushInput()
input = b'\x92'     # unlock
ser2.write(input)
sleep(0.5)
