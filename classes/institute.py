import datetime

from main import *

class Institute:
    def __init__(self):
        self.students = []
        self.groups = []
        self.subjects = []
        self.specs = []
        self.exams = []
        self.exam_results = []

    def add_spec(self, spec: Specialization):
        if type(spec) != Specialization:
            raise Exception('Type error')
        if len(str(spec.name)) <= 1:
            raise Exception("Enter name")
        for i in self.specs:
            if i == spec:
                raise Exception('error')
        self.specs.append(spec)

    def getSpec(self, name: str):
        if type(name) != str:
            raise Exception('Type error')
        if str(name) == '':
            raise Exception('Enter name')
        if str(name) == None:
            raise Exception('Enter name')
        for spec in self.specs:
            if spec.name == name:
                return spec
        else:
            raise Exception('Специализация не найдена')

    def add_stud(self, stud: Student):
        if type(stud.code) != int or \
                type(stud.fio) != str:
            raise Exception('Type error')
        if type(stud) != Student:
            raise Exception('Type error')
        if len(str(stud.code)) != 6:
            raise Exception('Номер зачетки должен быть 6-тизначным')
        for i in self.students:
            if i == stud.code:
                raise Exception('Такой студент уже сущ')
        self.students.append(stud)

    def getStudent(self, studcode: int):
        if studcode < 0:
            raise Exception('Номер зачетки отрицательным быть не может')
        if type(studcode) != int:
            raise Exception('Номер зачетки должен числовым')
        if studcode == None:
            raise Exception('Введите номер зачетки')
        if len(str(studcode)) != 6:
            raise Exception('Номер зачетки должен быть 6-тизначным')
        for student in self.students:
            if student.code == studcode:
                return student
        else:
            raise Exception('Студент не найден')

    def add_group(self, group: Group):
        if type(group.year) != int or \
                type(group.name) != str:
            raise Exception('Group type error')
        if type(group) != Group:
            raise Exception('Type error')
        if type(group.specialization) != Specialization:
            raise Exception('Specialization type error')
        if group.specialization.name == '':
            raise Exception('Enter Specialization name')
        for i in self.groups:
            if i == group:
                raise Exception('error')
        self.groups.append(group)

    def getGroup(self, name: str):
        for group in self.groups:
            if group.name == name:
                return group
        else:
            raise Exception('Группа не найдена')

    def add_subject(self, subject: Subject):
        if type(subject.name) != str or \
                type(subject.code) != str or \
                type(subject.hours) != int or \
                type(subject.semester) != int or \
                type(subject.specialization) != Specialization:
            raise Exception('Type error')
        if subject.name == '' or \
                subject.specialization == '' or \
                subject.code == '' or \
                subject.hours == '' or \
                subject.semester == '':
            raise Exception("Enter subject!")
        if subject.specialization.name == '':
            raise Exception('Enter specialization name')
        if type(subject) != Subject:
            raise Exception('Type error')
        for i in self.subjects:
            if i == subject:
                raise Exception('error')
        self.subjects.append(subject)

    def getSubject(self, name_sub: str):
        for subject in self.subjects:
            if subject.name == name_sub:
                return subject
        else:
            raise Exception('Предмет не найден')

    def add_exam(self, exam: Exam):
        if type(exam) != Exam:
            raise Exception('Type error')
        if type(exam.subject.name) != str or \
                type(exam.subject.specialization) != Specialization or \
                type(exam.subject.code) != str or \
                type(exam.subject.hours) != int or \
                type(exam.subject.semester) != int:
            raise Exception("Error type!")
        if exam.subject.name == '' or \
                exam.subject.specialization == '' or \
                exam.subject.code == '' or \
                exam.subject.hours == '' or \
                exam.subject.semester == '':
            raise Exception("Enter subject!")
        if exam.examDate.year > datetime.datetime.now().year:
            raise Exception('The year cannot be greater than the current year')
        if exam.year == '':
            raise Exception('Enter date')
        if exam.subject.specialization.name == '':
            raise Exception('Enter specialization')
        if type(exam.examDate) != date:
            raise Exception('Exam date type error')
        for i in self.exams:
            if i == exam:
                raise Exception('error')
        self.exams.append(exam)

    def add_exam_marks(self, exam_points:ExamPoints):
        if type(exam_points.student.code) != int or \
                type(exam_points.student.fio) != str or \
                type(exam_points.student) != Student or \
                type(exam_points.examPoints) != float or \
                type(exam_points.inPoints) != float:
            raise Exception('Type error')
        if type(exam_points.student.code) == '' or \
                type(exam_points.student.fio) == '' or \
                type(exam_points.examPoints) == '' or \
                type(exam_points.inPoints) == '':
            raise Exception('Check values for emptiness')
        for i in self.exam_results:
            if i == exam_points:
                raise Exception('error')
        self.exams.append(exam_points)

    def get_exam_result(self, spec, subject_name, date):
        if spec == "" or spec == None:
            raise Exception('Введите spec')
        if subject_name == "" or subject_name == None:
            raise Exception('Введите subject_name')
        if date == "" or date == None:
            raise Exception('Введите date')
        for exam in self.exams:
            if exam.subject.specialization.name == spec and exam.subject.name == subject_name and exam.examDate == date:
                return exam
        else:
            raise Exception('Экзамен не найден')

    def get_exam_marks(self, exam_result: int):
        if type(exam_result) != int:
            raise Exception('Error type')
        if type(exam_result) == '':
            raise Exception('Enter studcode')
        if type(exam_result) == None:
            raise Exception('Enter studcode')
        for examRes in self.exam_results:
            if examRes.student == exam_result:
                return examRes
        else:
            raise Exception('Exam не найден')
