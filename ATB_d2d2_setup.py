import sys
import os
from time import sleep


# sys.path.append('C:/Drive-W/Internal_tools/Libraries/D2D2Tools/')
sys.path.append('C:/Drive-W/Internal_tools/Libraries/D2D2Library/')
from D2D2Wrapper import D2D2Wrapper
D2D2_port = os.environ['ev_d2d2_port']
d2 = D2D2Wrapper()
d2.D2D2_Connect(D2D2_port)

d2.D2D2_Load_Device('c:/devd2d2/ivu')
sleep(1)
d2.D2D2_Claim_Id()
sleep(3)
d2.D2D2_Send_Test_Message()
d2.D2D2_Unlock_And_Disarm()
sleep(2)


d2.D2D2_Disconnect()

d2.D2D2_Answer_To_Pairing_Mode()


d2.D2D2_Send_Test_Message()
sleep(1)
d2.D2D2_Send_Test_Message()
sleep(1)
d2.D2D2_Sensor_bypass_level_user_toggle()



# Create device
combo = d2.D2D2_Create_Device()
combo.D2D2_Set_Uuid(199, 'DEI-NGSS', 0x00, 0x21, 0x00, 0x00)
combo.D2D2_Claim_Id()
sleep(4)
# Enter in pairing and exit without doing anything, this will register the sensor
combo.D2D2_Sens_Set_Temperature(25)
combo.D2D2_Sens_Send_Status('Temp Sensor', 'Normal')
d2.D2D2_Vehicule_Temp_Report_Request()
sleep(1)
combo.D2D2_Get_Vehicule_Temp()




# pair remote

d2.D2D2_Answer_To_Pairing_Mode()
io.IO_Set_Value('ignition', True)
sleep(2)
d2.D2D2_Switch_Pattern_Button(1, True)
sleep(3)
d2.D2D2_Switch_Pattern_Button_Release()
sleep(7)
io.IO_Set_Value('ignition', False)
sleep(1)
d2.D2D2_Unlock_And_Disarm()
sleep(2)


