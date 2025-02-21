import unittest
from waiter import Waiter, Barista

class WaiterTestCase(unittest.TestCase):
    def setUp(self):
        self.baristaObj = Barista("John", 1000)
    
    def test_init(self):
        w = Waiter("Bob", 700)
        self.assertEqual(w.fullname, "Tom")
        self.assertEqual(w.salary, 700)
        self.assertEqual(w.custServed, 0)
        
    def test_serve(self):
        w = Waiter("Bob", 700)
        w.serve(50, self.barista)
        self.assertEqual(w.custServed, 50)
