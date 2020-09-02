import unittest
import hello_world as hw

class TestHelloWorld(unittest.TestCase):

    objMessage = "Hello World!"

    obj = hw.HelloWorld()
    obj.set_message(objMessage)
    
    def test_get_message(self):
        self.assertEqual(self.obj.get_message(), self.objMessage)

if __name__ == '__main__':
    unittest.main()