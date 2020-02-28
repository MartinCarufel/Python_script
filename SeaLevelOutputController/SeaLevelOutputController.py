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
        self.Text = '8224 controler'
        self.Icon = Icon("hnet.com-image.ico")
        self.Size = Size(350,700)

        B0 = buttonLib.ButtonLib('Ignition', posX=10, posY=10, linkedOutput='ignition')
        b0 = B0.create_button()
        self.Controls.Add(b0)
        B1 = buttonLib.ButtonLib('Door (+)', posX=10, posY=50, linkedOutput='door_pos')
        b1 = B1.create_button()
        self.Controls.Add(b1)
        B2 = buttonLib.ButtonLib('Brake', posX=10, posY=90, linkedOutput='brake')
        b2 = B2.create_button()
        self.Controls.Add(b2)

        B3 = buttonLib.ButtonLib('Instant Alarm', posX=10, posY=130, linkedOutput='instant')
        b3 = B3.create_button()
        self.Controls.Add(b3)

        B4 = buttonLib.ButtonLib('Activation', posX=10, posY=170, linkedOutput='activation_input')
        b4 = B4.create_button()
        self.Controls.Add(b4)

        B5 = buttonLib.ButtonLib('Trigger', posX=10, posY=210, linkedOutput='trigger')
        b5 = B5.create_button()
        self.Controls.Add(b5)

        B6 = buttonLib.ButtonLib('E-Brake', posX=10, posY=250, linkedOutput='e_brake')
        b6 = B6.create_button()
        self.Controls.Add(b6)
        B7 = buttonLib.ButtonLib('Trunk', posX=10, posY=290, linkedOutput='trunk')
        b7 = B7.create_button()
        self.Controls.Add(b7)

        B8 = buttonLib.ButtonLib('Door (-)', posX=10, posY=330, linkedOutput='door')
        b8 = B8.create_button()
        self.Controls.Add(b8)

        B9 = buttonLib.ButtonLib('Hood', posX=10, posY=370, linkedOutput='hood')
        b9 = B9.create_button()
        self.Controls.Add(b9)

        B10 = buttonLib.ButtonLib('Out11', posX=10, posY=410, linkedOutput='out11')
        b10 = B10.create_button()
        self.Controls.Add(b10)

        B11 = buttonLib.ButtonLib('Out 12', posX=10, posY=450, linkedOutput='out12')
        b11 = B11.create_button()
        self.Controls.Add(b11)

        B12 = buttonLib.ButtonLib('Out 13', posX=10, posY=490, linkedOutput='out13')
        b12 = B12.create_button()
        self.Controls.Add(b12)

        B13 = buttonLib.ButtonLib('Out 14', posX=10, posY=530, linkedOutput='out14')
        b13 = B13.create_button()
        self.Controls.Add(b13)

        B14 = buttonLib.ButtonLib('D2D Power', posX=10, posY=570, linkedOutput='d2d_pwr_on')
        b14 = B14.create_button()
        self.Controls.Add(b14)

        B15 = buttonLib.ButtonLib('DS4 PWR OFF set to', posX=10, posY=610, linkedOutput='DS4_pwr_off')
        b15 = B15.create_button()
        self.Controls.Add(b15)

        B16 = buttonLib.ButtonLib('Out 17', posX=170, posY=10, linkedOutput='out17')
        b16 = B16.create_button()
        self.Controls.Add(b16)

        B17= buttonLib.ButtonLib('Out 18', posX=170, posY=50, linkedOutput='out18')
        b17 = B17.create_button()
        self.Controls.Add(b17)

        B18 = buttonLib.ButtonLib('Out 19', posX=170, posY=90, linkedOutput='out19')
        b18 = B18.create_button()
        self.Controls.Add(b18)

        B19 = buttonLib.ButtonLib('Out 20', posX=170, posY=130, linkedOutput='out20')
        b19 = B19.create_button()
        self.Controls.Add(b19)

        B20 = buttonLib.ButtonLib('Out 21', posX=170, posY=170, linkedOutput='out21')
        b20 = B20.create_button()
        self.Controls.Add(b20)

        B21 = buttonLib.ButtonLib('Out 22', posX=170, posY=210, linkedOutput='out22')
        b21 = B21.create_button()
        self.Controls.Add(b21)

        B22 = buttonLib.ButtonLib('Out 23', posX=170, posY=250, linkedOutput='out23')
        b22 = B22.create_button()
        self.Controls.Add(b22)

        B23 = buttonLib.ButtonLib('Out 24', posX=170, posY=290, linkedOutput='out24')
        b23 = B23.create_button()
        self.Controls.Add(b23)

        B24 = buttonLib.ButtonLib('HHU Unlock', posX=170, posY=330, linkedOutput='IVU_unlock')
        b24 = B24.create_button()
        self.Controls.Add(b24)

        B25 = buttonLib.ButtonLib('HHU Lock', posX=170, posY=370, linkedOutput='IVU_lock')
        b25 = B25.create_button()
        self.Controls.Add(b25)

        B26 = buttonLib.ButtonLib('HHU Start', posX=170, posY=410, linkedOutput='IVU_start')
        b26 = B26.create_button()
        self.Controls.Add(b26)

        B27 = buttonLib.ButtonLib('HHU Aux', posX=170, posY=450, linkedOutput='IVU_aux')
        b27 = B27.create_button()
        self.Controls.Add(b27)

        B28 = buttonLib.ButtonLib('Out 29', posX=170, posY=490, linkedOutput='out29')
        b28 = B28.create_button()
        self.Controls.Add(b28)

        B29 = buttonLib.ButtonLib('Out 30', posX=170, posY=530, linkedOutput='out30')
        b29 = B29.create_button()
        self.Controls.Add(b29)

        B30 = buttonLib.ButtonLib('Out 31', posX=170, posY=570, linkedOutput='out31')
        b30 = B30.create_button()
        self.Controls.Add(b30)

        B31 = buttonLib.ButtonLib('Out 32', posX=170, posY=610, linkedOutput='out32')
        b31 = B31.create_button()
        self.Controls.Add(b31)


form = HelloWorldForm()
Application.Run(form)