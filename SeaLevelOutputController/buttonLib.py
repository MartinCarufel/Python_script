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



class ButtonLib(Form):
    def __init__(self, ):
        pass

    def create_button(self, text='', posX=0, posY=0, linkedOutput='', io=None):
        self.text = text
        self.io = io
        self.button = Button()
        self.posX = posX
        self.posY = posY
        self.linkedOutput = linkedOutput
        self.state = self.io.IO_Get_Value(self.linkedOutput)
        if self.state:
            self.button.Text = self.text + ' ON'
        elif not self.state:
            self.button.Text = self.text + ' OFF'
        self.button.Size = Size(150, 30)
        self.button.Location = Point(self.posX, self.posY)
        self.button.Click += self.buttonPress
        return self.button

    def buttonPress(self, sender, args):
        # print(sender)
        # print(self.linkedOutput)
        if self.state:
            self.io.IO_Set_Value(self.linkedOutput, False)
            self.state = False
            self.button.Text = self.text + ' OFF'
        elif not self.state:
            self.io.IO_Set_Value(self.linkedOutput, True)
            self.state = True
            self.button.Text = self.text + ' ON'
        # print self.linkedOutput

    def create_connect_button(self, posX=0, posY=0, io=None, but_list=None):
        self.io = io
        self.but_list = but_list
        self.io_out_port = os.environ['ev_io_out_port']
        self.button = Button()
        try:
            self.io.IO_Get_Digital_Output(2, 1)
            self.button.Text = 'Disconnect'
            print('Init, get digital work I am connected')
        except:
            self.button.Text = 'Connect'
            print('Init, get digital did NOT work I am Disconnected')
        self.posX = posX
        self.posY = posY
        self.button.Size = Size(150, 30)
        self.button.Location = Point(self.posX, self.posY)
        self.button.Click += self.connect_button_press
        return self.button


    def connect_button_press(self, sender, args):
        try:
            self.io.IO_Get_Digital_Output(2, 1)
            self.io.IO_Disconnect()
            self.button.Text = 'Connect'
            for i in self.but_list:
                i.Enabled = False
            print('PRESS, Get digital work, was connected but now do disconnect')

        except:
            self.io.IO_Connect_Device(2, self.io_out_port)
            self.io.IO_Read_Map('DS4-Analog Harness_3.xml')
            self.button.Text = 'Disconnect'
            for i in self.but_list:
                i.Enabled = True
            print('PRESS, Get digital NOT work, was disconnected but now do Connect')
