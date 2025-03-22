import unittest
from teacher import Teacher

class TeacherTestCase(unittest.TestCase):
    def setUp(self)-> None:
        self.bush = Teacher("George", "Bush")
        self.clinton = Teacher("Bill", "Clinton", 1001)
        
    def test_from_dict(self):
        dict_arg = {"firstname": "George", "surname": "Bush",
                "teacherID":-1}
                
        t = Teacher()
        t.from_dict(dict_arg)
        self.assertEqual(self.bush.firstname, t.firstname)
        self.assertEqual(self.bush.surname, t.surname)
        self.assertEqual(self.bush.teacherID, t.teacherID)
        
    def test_to_dict(self):
        dict_arg = {"firstname": "Bill", "surname": "Clinton",
                "teacherID":-1}
                
        self.assertEqual(self.bush.to_dict()["firstname"], dict_arg["firstname"])
        self.assertEqual(self.bush.to_dict()["surname"], dict_arg["surname"])
        self.assertEqual(self.bush.to_dict()["teacherID"], dict_arg["teacherID"])
