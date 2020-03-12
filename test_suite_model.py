import unittest
from time import sleep
from System import *
from symbol import except_clause
import sys





class Test_Suite_1(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    
    def test_1(self):
        self.o.set_can1_filter(555)
        print 'play log file'
        sleep(1)
        self.can.CAN_Play_Log_File('can_log.csv')
        
