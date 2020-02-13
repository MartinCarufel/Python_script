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

io_out_port = os.environ['ev_io_out_port']
io_in_port = os.environ['ev_io_in_port']

class HelloWorldForm(Form):

    def __init__(self):
        self.Text = 'Hello World'
        self.ign_state = False
        self.button = Button()
        self.button.Text = "Click Me"
        self.button.Size = Size(200,30)
        self.button.Location = Point(10, 10)
        self.button.Click += self.buttonPress
        self.Controls.Add(self.button)
        self.io = IOWrapper()
        self.io.IO_Connect_Device(1, io_in_port)
        self.io.IO_Connect_Device(2, io_out_port)
        self.io.IO_Read_Map('C:/Drive-W/atb_dev/RobotFW_common/lib/DS4-Analog Harness_3.xml')
        print(type(self.button))

    def buttonPress(self, sender, args):
        if self.ign_state:
            self.io.IO_Set_Value('ignition', False)
            self.ign_state = False
            self.button.Text = "ignition OFF"
           
        elif not self.ign_state:
            self.io.IO_Set_Value('ignition', True)
            self.ign_state = True
            self.button.Text = "ignition ON"
        print('ignition')

form = HelloWorldForm()
Application.Run(form)