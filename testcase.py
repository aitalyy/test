import unittest
from subject import getSubject
from main import Student, Group, Subject, ExamPoints, Exam, Specialization

class TestClass(unittest.TestCase):
    def test_class_student(self):
        student = Student(172527, "Егоров Айтал Никитич")
        self.assertEqual("Егоров Айтал Никитич", student.fio)
        self.assertEqual(172527, student.code)

    def test_class_specialization(self):
        specialization = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", specialization.name)

    def test_class_group(self):
        specialization = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, specialization)
        self.assertEqual("М-ФИИТ-21", group.name)
        self.assertEqual(2021, group.year)
        self.assertEqual(specialization, group.specialization)

    def test_class_examPoints(self):
        student = Student(172527, "Егоров Айтал Никитич")
        examPoints = ExamPoints(student, 40.1, 22.5)
        self.assertEqual(student, examPoints.student)
        self.assertEqual(40.1, examPoints.inPoints)
        self.assertEqual(22.5, examPoints.examPoints)

    def test_class_Subject(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, specialization)
        self.assertEqual("Б1.В.02", subject.code)
        self.assertEqual("Методы тестирования и верификации программных продуктов", subject.name)
        self.assertEqual(2, subject.semester)
        self.assertEqual(108, subject.hours)
        self.assertEqual(specialization, subject.specialization)

    def test_class_Exam(self):
        date = "25.05.2022"
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, specialization)
        exam = Exam(subject, date, "2021-2022", "Эверстов Владимир Васильевич")
        self.assertEqual(subject, exam.subject)
        self.assertEqual(date, exam.examDate)
        self.assertEqual("2021-2022", exam.year)
        self.assertEqual("Эверстов Владимир Васильевич", exam.lecturer_fio)

    def test_class_getsubject(self):
        subject = getSubject("./res/Object.xlsx", "Основы программирования")
        self.assertEqual("Б1.Б.22", subject.code)
        self.assertEqual("Основы программирования", subject.name)
        self.assertEqual("ФИИТ", subject.specialization.name)
        self.assertEqual(1, subject.semester)
        self.assertEqual(144, subject.hours)

if __name__ == '__main__':
    unittest.main()