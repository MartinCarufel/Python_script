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

io = IOWrapper()
# io.IO_Connect_Device(1, io_in_port)
io.IO_Connect_Device(2, io_out_port)
io.IO_Read_Map('DS4-Analog Harness_3.xml')

class ButtonLib(Form):
    def __init__(self, text='', posX=0, posY=0, linkedOutput=''):
        self.text = text
        self.button = Button()
        self.posX = posX
        self.posY = posY
        self.linkedOutput = linkedOutput
        self.state = io.IO_Get_Value(self.linkedOutput)
        if self.state:
            self.button.Text = self.text + ' ON'
        elif not self.state:
            self.button.Text = self.text + ' OFF'
        self.button.Size = Size(150, 30)
        self.button.Location = Point(self.posX, self.posY)
        self.button.Click += self.buttonPress


    def create_button(self):
        # self.button = Button()
        # self.posX = posX
        # self.posY = posY
        # self.linkedOutput = linkedOutput
        # self.button.Text = text
        # self.button.Size = Size(200, 30)
        # self.button.Location = Point(self.posX, self.posY)
        # self.button.Click += self.buttonPress
        return self.button

    def buttonPress(self, sender, args):
        # print(sender)
        # print(self.linkedOutput)
        if self.state:
            io.IO_Set_Value(self.linkedOutput, False)
            self.state = False
            self.button.Text = self.text + ' OFF'
        elif not self.state:
            io.IO_Set_Value(self.linkedOutput, True)
            self.state = True
            self.button.Text = self.text + ' ON'
        # print self.linkedOutput
