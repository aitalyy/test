from main import Student
from classes.institute import Institute
from classes.student import getStudent
import unittest

class TestAddStudent(unittest.TestCase):
    def test_one(self): #correct
        stud = Student('777777','Егоров Айтал Никитич')
        inst = Institute()
        inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_two(self): #correct
        stud = Student('777777', 'Егоров Айтал Никитич')
        stud1 = Student('199995', 'Иванов Иван Иванович')
        inst = Institute()
        inst.add_stud(stud)
        inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 2)



    def test_three(self):
        stud = Student('','')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_four(self):
        stud = Student('Егоров Айтал Никитич', '777777')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_five(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(123)
        self.assertEqual(len(inst.students), 0)

    def test_six(self):
        stud = Student('777777','Егоров Айтал Никитич')
        stud1 = Student('777777','Егоров Айтал Никитич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)

    def test_seven(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(123)
        self.assertEqual(len(inst.students), 0)

    def test_eight(self):
        stud = Student('777777','777777')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_nine(self):
        stud = Student('Егоров Айтал Никитич','сто')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_ten(self):
        stud = Student('Егоров Айтал Никитич', '777777')
        stud1 = Student('Иванов Иван Иванович', '777777')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)

    def test_eleven(self):
        stud = Student('Егоров Айтал Никитич', '777777')
        stud1 = Student('Егоров Айтал Никитич', '666666')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)


class TestGetStudent(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()
        self.institute.students = [
            Student(888444, 'Егоров Айтал Никитич'),
            Student(100001, "Иван Иванович Иванов")
        ]
        super(TestGetStudent, self).__init__(*args, **kwargs)


    def test_1(self): #correct
        g_student = self.institute.getStudent(888444)
        self.assertEqual("Егоров Айтал Никитич", g_student.fio)
        self.assertEqual(888444, g_student.code)

'''
    def test_2(self):
        g_student = self.institute.getStudent(-888444)
        with self.assertRaises(Exception):
            self.institute.getStudent(g_student)

    def test_3(self):
        g_student = self.institute.getStudent(12345)
        with self.assertRaises(Exception):
            self.institute.getStudent(g_student)

    def test_4(self):
        g_student = self.institute.getStudent(8798721)
        with self.assertRaises(Exception):
            self.institute.getStudent(g_student)

    def test_5(self):
        g_student = self.institute.getStudent(152.451)
        with self.assertRaises(Exception):
            self.institute.getStudent(g_student)

    def test_6(self):
        g_student = self.institute.getStudent("asd")
        with self.assertRaises(Exception):
            self.institute.getStudent(g_student)

    def test_7(self):
        g_student = self.institute.getStudent(None)
        with self.assertRaises(Exception):
            self.institute.getStudent(g_student)
'''


if __name__ == "__main__":
    unittest.main()