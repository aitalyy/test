from main import Specialization
from classes.institute import Institute
from classes.spec import getSpecialization
import unittest

class TestAddSpec(unittest.TestCase):
    def test_one(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        inst = Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_two(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Информатика и вычислительная техника')
        inst = Institute()
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)




    def test_three(self):
        sp = Specialization('')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_four(self):
        sp = Specialization('')
        inst = Institute('')
        with self.assertRaises(Exception):
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_five(self):
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Фундаментальная информатика и информационные технологии')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
            inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 0)

    def test_six(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec('')
        self.assertEqual(len(inst.specs), 1)




class TestGetSpec(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()
        self.institute.specs = [
            Specialization('Информатика и вычислительная техника'),
            Specialization('Фундамельная информатика и информационные технологии')
        ]
        super(TestGetSpec, self).__init__(*args, **kwargs)

    def test_1(self): #correct
        g_spec = self.institute.getSpec('Информатика и вычислительная техника')
        self.assertEqual('Информатика и вычислительная техника', g_spec.name)
'''
    def test_2(self):
        g_spec = self.institute.getSpec(None)
        with self.assertRaises(Exception):
            self.institute.getSpec(g_spec)

    def test_3(self):
        g_spec = self.institute.getSpec("")
        with self.assertRaises(Exception):
            self.institute.getSpec(g_spec)

    def test_4(self):
        g_spec = self.institute.getSpec(354652)
        with self.assertRaises(Exception):
            self.institute.getSpec(g_spec)

    def test_5(self):
        g_spec = self.institute.getSpec('Информатика и вычислительная техника')
        with self.assertRaises(Exception):
            self.institute.getSpec(g_spec)
'''
if __name__ == "__main__":
    unittest.main()