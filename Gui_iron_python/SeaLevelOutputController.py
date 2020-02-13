import sys
import os
from time import sleep
# sys.path.append(r'C:\Python24\Lib')
sys.path.append(r'C:\Users\martin.carufel\AppData\Local\Programs\Python\Python37-32\Lib\site-packages')
sys.path.append('C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out')
from IOWrapper import IOWrapper
import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
from System.Drawing import Point, Size
from System.Windows.Forms import Application, Button, Form, Label
import buttonLib

io_out_port = os.environ['ev_io_out_port']
io_in_port = os.environ['ev_io_in_port']

class HelloWorldForm(Form):

    def __init__(self):
        self.Text = '8224 controler'
        self.Size = Size(350,400)

        B0 = buttonLib.ButtonLib('Ignition', posX=10, posY=10, linkedOutput='ignition')
        b0 = B0.create_button()
        self.Controls.Add(b0)
        B1 = buttonLib.ButtonLib('Door', posX=10, posY=50, linkedOutput='door_pos')
        b1 = B1.create_button()
        self.Controls.Add(b1)
        B2 = buttonLib.ButtonLib('Brake', posX=10, posY=90, linkedOutput='brake')
        b2 = B2.create_button()
        self.Controls.Add(b2)
        B6 = buttonLib.ButtonLib('E-Brake', posX=10, posY=130, linkedOutput='e_brake')
        b6 = B6.create_button()
        self.Controls.Add(b6)
        B7 = buttonLib.ButtonLib('Trunk', posX=10, posY=170, linkedOutput='trunk')
        b7 = B7.create_button()
        self.Controls.Add(b7)
        B9 = buttonLib.ButtonLib('Hood', posX=10, posY=210, linkedOutput='hood')
        b9 = B9.create_button()
        self.Controls.Add(b9)
        B14 = buttonLib.ButtonLib('D2D Power', posX=10, posY=250, linkedOutput='d2d_pwr_on')
        b14 = B14.create_button()
        self.Controls.Add(b14)
        B15 = buttonLib.ButtonLib('DS4 PWR OFF set to', posX=10, posY=290, linkedOutput='DS4_pwr_off')
        b15 = B15.create_button()
        self.Controls.Add(b15)

        B24 = buttonLib.ButtonLib('HHU Unlock', posX=170, posY=10, linkedOutput='IVU_unlock')
        b24 = B24.create_button()
        self.Controls.Add(b24)
        B25 = buttonLib.ButtonLib('HHU Lock', posX=170, posY=50, linkedOutput='IVU_lock')
        b25 = B25.create_button()
        self.Controls.Add(b25)
        B26 = buttonLib.ButtonLib('HHU Start', posX=170, posY=90, linkedOutput='IVU_start')
        b26 = B26.create_button()
        self.Controls.Add(b26)
        B27 = buttonLib.ButtonLib('HHU Aux', posX=170, posY=130, linkedOutput='IVU_aux')
        b27 = B27.create_button()
        self.Controls.Add(b27)


form = HelloWorldForm()
Application.Run(form)