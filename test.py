#coding:utf-8

import sys
import os
from time import sleep

sys.path.append(r'C:\Drive-W\Internal_tools\Libraries\D2DProjectLibrary\trunk\out')
sys.path.append(r'C:\Drive-W\Internal_tools\Libraries\CANOBDIILibrary\trunk\out')
from D2DWrapper import D2DWrapper
from CANInterface import CANInterface

def test_can():
    canDev = CANInterface()
    canDev.Connected()
    baudRate = canDev.Get_BaudRate()
    print(baudRate[0])
    print(baudRate[1])
    canDev.Set_BaudRate(100000, 100000)
    baudRate = canDev.Get_BaudRate()
    print(baudRate[0])
    print(baudRate[1])
    canDev.Set_BaudRate(500000, 500000)
    canDev.CAN_Disconnected()


def test_d2d():
    d2d_conn = D2DWrapper("COM2")
    sleep(2)
    d2d_conn.Send_D2D_Function('unlock door rem1 on')
    sleep(5)
    extStatus = d2d_conn.D2D_Extended_Status('0', True)
    print(extStatus)
    d2d_conn.Send_Raw_Data('91')
    sleep(5)
    d2d_conn.Send_D2D_Function('unlock door rem1 on')


    d2d_conn.D2D_Disconnected()


#test_can()

test_d2d()
