'''
Created on Jun 4, 2019

@author: martin.carufel
'''

import sys
import os
from time import sleep
from CANInterface import CANInterface
sys.path.append('C:/Drive-W/Internal_tools/Libraries/CANOBDIILibrary/trunk/out/')
can_port = os.environ['ev_can_port']
can = CANInterface()

can.CAN_Connect()
can.CAN_Set_BaudRate(500000, 100000)
for i in range(0x111):
    print str(hex(i))
    
    can.CAN_Transmit_Message('CAN1', str(hex(i)), '0x10', '0x20', '0x30', '0x40', '0x50', '0x60', '0x70', '0x80')
    sleep(0.005)
