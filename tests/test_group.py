from main import Group, Specialization
from classes.institute import Institute
from classes.group import getGroup
import unittest

class TestAddGroup(unittest.TestCase):
    def test_one(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('М-ФИИТ-21', '2021', spec)
        inst = Institute()
        inst.add_group(group)
        self.assertEqual(len(inst.groups), 1)

    def test_two(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('М-ФИИТ-21', '2021', spec)
        spec1 = Specialization('Информатика и вычислительная техника')
        group1 = Group('М-ИВТ-21', '2021', spec1)
        inst = Institute()
        inst.add_group(group)
        inst.add_group(group1)
        self.assertEqual(len(inst.groups), 2)




    def test_three(self):
        spec = Specialization('')
        group = Group('М-ФИИТ-21', '2021', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_four(self):
        group = Group('М-ФИИТ-21', '2021', 12)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_five(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('2021', 'М-ФИИТ-21', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_six(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('', '', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_seven(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(12)
        self.assertEqual(len(inst.groups), 0)
    def test_eight(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('21', '2021', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_nine(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('двадцать один', 'дветысячидвадцатьпервый', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_ten(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('М-ФИИТ-21', '2021', spec)
        spec1 = Specialization('Фундаментальная информатика и информационные технологии')
        group1 = Group('М-ФИИТ-21', '2021', spec1)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
            inst.add_group(group1)
        self.assertEqual(len(inst.groups), 0)
    def test_eleven(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('М-ИВТ-21', '2021', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_twelve(self):
        spec = Specialization('Информатика и вычислительная техника')
        group = Group('М-ФИИТ-21', '2021', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_thirteen(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('ФИИТ-21', '2021', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_group(group)
        self.assertEqual(len(inst.groups), 0)
    def test_fourteen(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        group = Group('М-ФИИТ-21', '2021', spec)
        group1 = Group('Б-ФИИТ-17', '2017', spec)
        inst = Institute()
        inst.add_group(group)
        inst.add_group(group1)
        self.assertEqual(len(inst.groups), 2)




class TestGetGroup(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()
        self.institute.groups = [
            Group('М-ИВТ-20', 2020, 'Информатика и вычислительная техника'),
            Group('М-ФИИТ-21', 2021, 'Фундамельная информатика и информационные технологии')
        ]
        super(TestGetGroup, self).__init__(*args, **kwargs)


    def test_1(self): #correct
        g_group = self.institute.getGroup('М-ИВТ-20')
        self.assertEqual('М-ИВТ-20', g_group.name)
        self.assertEqual(2020, g_group.year)
        self.assertEqual('Информатика и вычислительная техника', g_group.specialization)
'''
    def test_2(self):
        g_group = self.institute.getGroup("М-ФИИТ-17")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_3(self):
        g_group = self.institute.getGroup("Б-ФИИТ-17")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_4(self):
        g_group = self.institute.getGroup("ФИИТ-17")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_5(self):
        g_group = self.institute.getGroup("М-ФИИТ-99")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_6(self):
        g_group = self.institute.getGroup(None)
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_7(self):
        g_group = self.institute.getGroup("123123")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_8(self):
        g_group = self.institute.getGroup("М-фывфывдл-21")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)

    def test_9(self):
        g_group = self.institute.getGroup("")
        with self.assertRaises(Exception):
            self.institute.getGroup(g_group)
'''
if __name__ == "__main__":
    unittest.main()