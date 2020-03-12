import sys
import os
from time import sleep

sys.path.append('C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out')
from IOWrapper import IOWrapper
io_out_port = os.environ['ev_io_out_port']
io_in_port = os.environ['ev_io_in_port']
# io_8227_port = os.environ['ev_io_8227_port']

io = IOWrapper()
io.IO_Connect_Device(1, io_in_port)
io.IO_Connect_Device(2, io_out_port)
# io.IO_Connect_Device(3, io_8227_port)


io.IO_Read_Map('C:/Drive-W/atb_dev/RobotFW_common/lib/DS4-Analog Harness_3.xml')
# io.IO_Read_Map('C:/Users/martin.carufel/Documents/Python_script/io_dev_mapping.xml')


# #Arduino D2D2
# sys.path.append('C:/Drive-W/Internal_tools/Libraries/D2D2Library/trunk/out')
# from D2D2Wrapper import D2D2Wrapper
# D2D2_port = os.environ['ev_d2d2_port']
# d2 = D2D2Wrapper()
# d2.D2D2_Connect(D2D2_port)


# XKloader d2d2
sys.path.append('C:/Drive-W/Internal_tools/Libraries/D2D2Library')
from D2D2Wrapper import D2D2Wrapper
D2D2_port = os.environ['ev_d2d2_port']
d2 = D2D2Wrapper()
d2.D2D2_Connect(D2D2_port)

d2.D2D2_Load_Device('c:/devd2d2/ivu')
d2.D2D2_Claim_Id()



d2.D2D2_Set_Uuid(111, 'DEI-NGSS ', 0X00, 0X21, 0X00, 0X00)
d2.D2D2_Set_Device_Id(0X11)

d2.D2D2_Set_Uuid(133, 'DEI-IVx ', 0X00, 0X01, 0X00, 0X00)
d2.D2D2_Set_Device_Id(0X33)

d2.D2D2_Answer_To_Pairing_Mode()

d2.D2D2_Set_Uuid(135, 'DEI-IVx ', 0X00, 0X01, 0X00, 0X00)


d2.D2D2_Get_Vehicule_Temp()
d2.D2D2_Sens_Send_Status('Temp Sensor', '')



sys.path.append('C:/Drive-W/Internal_tools/Libraries/PSULibrary/trunk/out')
from PSUInterface import PSUInterface
PSU_port = os.environ['ev_psu_port']
ps=PSUInterface()
ps.psu_connect(PSU_port)

