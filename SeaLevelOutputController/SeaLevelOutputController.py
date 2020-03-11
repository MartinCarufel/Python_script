import sys
import os
from time import sleep
# sys.path.append(r'C:\Python24\Lib')
# sys.path.append(r'C:\Users\martin.carufel\AppData\Local\Programs\Python\Python37-32\Lib\site-packages')
sys.path.append('C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out')
from IOWrapper import IOWrapper
import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
from System.Drawing import Point, Size, Icon
from System.Windows.Forms import Application, Button, Form, Label
import buttonLib

io_out_port = os.environ['ev_io_out_port']
io_in_port = os.environ['ev_io_in_port']

class HelloWorldForm(Form):

    def __init__(self):
        self.but_list = []
        self.Text = '8224 controler'
        self.Icon = Icon("hnet.com-image.ico")
        self.Size = Size(350,750)
        io_out_port = os.environ['ev_io_out_port']

        self.io = IOWrapper()
        self.io.IO_Connect_Device(2, io_out_port)
        self.io.IO_Read_Map('DS4-Analog Harness_3.xml')

        B0 = buttonLib.ButtonLib()
        b0 = B0.create_button('Ignition', posX=10, posY=50, linkedOutput='ignition', io=self.io)
        self.but_list.append(b0)
        self.Controls.Add(b0)

        B1 = buttonLib.ButtonLib()
        b1 = B1.create_button('Door (+)', posX=10, posY=90, linkedOutput='door_pos', io=self.io)
        self.but_list.append(b1)
        self.Controls.Add(b1)

        B2 = buttonLib.ButtonLib()
        b2 = B2.create_button('Brake', posX=10, posY=130, linkedOutput='brake', io=self.io)
        self.but_list.append(b2)
        self.Controls.Add(b2)

        B3 = buttonLib.ButtonLib()
        b3 = B3.create_button('Instant Alarm', posX=10, posY=170, linkedOutput='instant', io=self.io)
        self.but_list.append(b3)
        self.Controls.Add(b3)

        B4 = buttonLib.ButtonLib()
        b4 = B4.create_button('Activation', posX=10, posY=210, linkedOutput='activation_input', io=self.io)
        self.but_list.append(b4)
        self.Controls.Add(b4)

        B5 = buttonLib.ButtonLib()
        b5 = B5.create_button('Trigger', posX=10, posY=250, linkedOutput='trigger', io=self.io)
        self.but_list.append(b5)
        self.Controls.Add(b5)

        B6 = buttonLib.ButtonLib()
        b6 = B6.create_button('E-Brake', posX=10, posY=290, linkedOutput='e_brake', io=self.io)
        self.but_list.append(b6)
        self.Controls.Add(b6)

        B7 = buttonLib.ButtonLib()
        b7 = B7.create_button('Trunk', posX=10, posY=330, linkedOutput='trunk', io=self.io)
        self.but_list.append(b7)
        self.Controls.Add(b7)

        B8 = buttonLib.ButtonLib()
        b8 = B8.create_button('Door (-)', posX=10, posY=370, linkedOutput='door', io=self.io)
        self.but_list.append(b8)
        self.Controls.Add(b8)

        B9 = buttonLib.ButtonLib()
        b9 = B9.create_button('Hood', posX=10, posY=410, linkedOutput='hood', io=self.io)
        self.but_list.append(b9)
        self.Controls.Add(b9)

        B10 = buttonLib.ButtonLib()
        b10 = B10.create_button('Out11', posX=10, posY=450, linkedOutput='out11', io=self.io)
        self.but_list.append(b10)
        self.Controls.Add(b10)

        B11 = buttonLib.ButtonLib()
        b11 = B11.create_button('Out 12', posX=10, posY=490, linkedOutput='out12', io=self.io)
        self.but_list.append(b11)
        self.Controls.Add(b11)

        B12 = buttonLib.ButtonLib()
        b12 = B12.create_button('Out 13', posX=10, posY=530, linkedOutput='out13', io=self.io)
        self.but_list.append(b12)
        self.Controls.Add(b12)

        B13 = buttonLib.ButtonLib()
        b13 = B13.create_button('Out 14', posX=10, posY=570, linkedOutput='out14', io=self.io)
        self.but_list.append(b13)
        self.Controls.Add(b13)

        B14 = buttonLib.ButtonLib()
        b14 = B14.create_button('D2D Power', posX=10, posY=610, linkedOutput='d2d_pwr_on', io=self.io)
        self.but_list.append(b14)
        self.Controls.Add(b14)

        B15 = buttonLib.ButtonLib()
        b15 = B15.create_button('DS4 PWR OFF set to', posX=10, posY=650, linkedOutput='DS4_pwr_off', io=self.io)
        self.but_list.append(b15)
        self.Controls.Add(b15)

        B16 = buttonLib.ButtonLib()
        b16 = B16.create_button('Out 17', posX=170, posY=50, linkedOutput='out17', io=self.io)
        self.but_list.append(b16)
        self.Controls.Add(b16)

        B17= buttonLib.ButtonLib()
        b17 = B17.create_button('Out 18', posX=170, posY=90, linkedOutput='out18', io=self.io)
        self.but_list.append(b17)
        self.Controls.Add(b17)

        B18 = buttonLib.ButtonLib()
        b18 = B18.create_button('Out 19', posX=170, posY=130, linkedOutput='out19', io=self.io)
        self.but_list.append(b18)
        self.Controls.Add(b18)

        B19 = buttonLib.ButtonLib()
        b19 = B19.create_button('Out 20', posX=170, posY=170, linkedOutput='out20', io=self.io)
        self.but_list.append(b19)
        self.Controls.Add(b19)

        B20 = buttonLib.ButtonLib()
        b20 = B20.create_button('Out 21', posX=170, posY=210, linkedOutput='out21', io=self.io)
        self.but_list.append(b20)
        self.Controls.Add(b20)

        B21 = buttonLib.ButtonLib()
        b21 = B21.create_button('Out 22', posX=170, posY=250, linkedOutput='out22', io=self.io)
        self.but_list.append(b21)
        self.Controls.Add(b21)

        B22 = buttonLib.ButtonLib()
        b22 = B22.create_button('Out 23', posX=170, posY=290, linkedOutput='out23', io=self.io)
        self.but_list.append(b22)
        self.Controls.Add(b22)

        B23 = buttonLib.ButtonLib()
        b23 = B23.create_button('Out 24', posX=170, posY=330, linkedOutput='out24', io=self.io)
        self.but_list.append(b23)
        self.Controls.Add(b23)

        B24 = buttonLib.ButtonLib()
        b24 = B24.create_button('HHU Unlock', posX=170, posY=370, linkedOutput='IVU_unlock', io=self.io)
        self.but_list.append(b24)
        self.Controls.Add(b24)

        B25 = buttonLib.ButtonLib()
        b25 = B25.create_button('HHU Lock', posX=170, posY=410, linkedOutput='IVU_lock', io=self.io)
        self.but_list.append(b25)
        self.Controls.Add(b25)

        B26 = buttonLib.ButtonLib()
        b26 = B26.create_button('HHU Start', posX=170, posY=450, linkedOutput='IVU_start', io=self.io)
        self.but_list.append(b26)
        self.Controls.Add(b26)

        B27 = buttonLib.ButtonLib()
        b27 = B27.create_button('HHU Aux', posX=170, posY=490, linkedOutput='IVU_aux', io=self.io)
        self.but_list.append(b27)
        self.Controls.Add(b27)

        B28 = buttonLib.ButtonLib()
        b28 = B28.create_button('Out 29', posX=170, posY=530, linkedOutput='out29', io=self.io)
        self.but_list.append(b28)
        self.Controls.Add(b28)

        B29 = buttonLib.ButtonLib()
        b29 = B29.create_button('Out 30', posX=170, posY=570, linkedOutput='out30', io=self.io)
        self.but_list.append(b29)
        self.Controls.Add(b29)

        B30 = buttonLib.ButtonLib()
        b30 = B30.create_button('Out 31', posX=170, posY=610, linkedOutput='out31', io=self.io)
        self.but_list.append(b30)
        self.Controls.Add(b30)

        B31 = buttonLib.ButtonLib()
        b31 = B31.create_button('Out 32', posX=170, posY=650, linkedOutput='out32', io=self.io)
        self.but_list.append(b31)
        self.Controls.Add(b31)

        conn = buttonLib.ButtonLib()
        bconn = conn.create_connect_button(posX=10, posY=10, io=self.io, but_list=self.but_list)
        self.Controls.Add(bconn)


form = HelloWorldForm()
Application.Run(form)