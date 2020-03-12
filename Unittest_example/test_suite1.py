import unittest


class test_suite_1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.var = 10
        print 'Do class setup, set var = 10'
    
    @classmethod
    def tearDownClass(cls):
        cls.var = None
        print 'Do class teardown, set var = None'
    
    def setUp(self):
        self.var2 = 10
        print 'Do test (method) setup, set var2 = 10'
    
    def tearDown(self):
        self.var2 = None
        print 'Do test (method) teardown, set var2 = None'
        
    
    def test_1(self):
        print 'Enter in test 1'
        a = 2
        b = 3
        self.assertEqual(a, b, 'Pas egal')

    def test_2(self):
        print 'Enter in test 1'
        self.assertEqual(self.var, self.var2, 'Pas egal')
    
    def test_3(self):
        print 'Enter in test 1'
        a = 2
        b = 2
        self.assertEqual(a, b, 'Pas egal')
        
    def test_4(self):
        self.assertEqual(self.var, self.var2)