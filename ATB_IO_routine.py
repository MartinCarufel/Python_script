
#Following set port to listen (default siren) the start recording. Stop recording and extract data.
port = 'siren'
io.IO_Start_Reading_Port(port)
#do you stuff
d2.D2D2_Unlock_And_Disarm()
sleep(1)

recording = io.IO_Stop_Reading_Ports()
portRecord = io.IO_Get_Port_Recordings(recording, port)


# Following script print on console the recorded signal
for i in range(io.IO_Get_Record_Item_Count(portRecord)):
    print('The signal index {} is {} for {} sec.'. format(i, io.IO_Get_Record_Item_Value(portRecord, i),io.IO_Get_Record_Item_Duration(portRecord, i)))



ports = ['siren', 'unlock']
io.IO_Start_Reading_Ports(ports)
#do you stuff
d2.D2D2_Unlock_And_Disarm()
sleep(3)

recording = io.IO_Stop_Reading_Ports()


# Following script print on console the recorded signal
for j in ports:
    portRecord = io.IO_Get_Port_Recordings(recording, j)
    for i in range(io.IO_Get_Record_Item_Count(portRecord)):
        print('The port {} signal index {} is {} for {} sec.'. format(j, i, io.IO_Get_Record_Item_Value(portRecord, i),io.IO_Get_Record_Item_Duration(portRecord, i)))
        
