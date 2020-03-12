import sys
import os
from time import sleep

# sys.path.append('C:/Drive-W/Internal_tools/Libraries/D2D2Tools/')

sys.path.append('C:/Drive-W/Internal_tools/Libraries/D2D2Tools/out/D2D2Library/')
sys.path.append('C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out/IOWrapper.py')

from D2D2Wrapper import D2D2Wrapper
from IOWrapper import IOWrapper

io_out_port = os.environ['ev_io_out_port']
io_in_port = os.environ['ev_io_in_port']

D2D2_port = os.environ['ev_d2d2_port']
d2 = D2D2Wrapper()
d2.D2D2_Connect(D2D2_port)
# d2.D2D2_Load_Device('c:/TEMP/ivu')
d2.D2D2_Set_Uuid(99, 'DEI-IVx ', 0x04, 0x01, 0x00, 0x00)
sleep(0.250)
d2.D2D2_Claim_Id()
sleep(2)
iodev = IOWrapper()
iodev.IO_Connect_Device(1, io_in_port)
iodev.IO_Connect_Device(2, io_out_port)
iodev.IO_Read_Map('C:/Drive-W/atb_dev/RobotFW_common/lib/DS4-Analog Harness_3.xml')

d2.D2D2_Answer_To_Pairing_Mode()
iodev.IO_Set_Value('ignition', True)
sleep(4)
d2.D2D2_Switch_Pattern_Button(1, True)
sleep(3)
d2.D2D2_Switch_Pattern_Button_Release()

sleep(10)
iodev.IO_Set_Value('ignition', False)
sleep(1)
d2.D2D2_Save_Device('c:/TEMP/ivu')
d2.D2D2_Send_Test_Message()
sleep(1)
d2.D2D2_Send_Test_Message()
sleep(1)
d2.D2D2_Unlock_And_Disarm()

d2.D2D2_Disconnect()
iodev.IO_Disconnect()

