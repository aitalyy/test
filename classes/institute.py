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
        for i in self.specs:
            if i == spec:
                raise Exception('error')
        self.specs.append(spec)

    def getSpec(self, name: str):
        for spec in self.specs:
            if spec.name == name:
                return spec
        else:
            raise Exception('Специализация не найдена')

    def add_stud(self, stud: Student):
        if type(stud) != Student:
            raise Exception('Type error')
        for i in self.students:
            if i == stud:
                raise Exception('error')
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
        if type(group) != Group:
            raise Exception('Type error')
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
            type(exam.subject.code) != int or \
            type(exam.subject.hours) != int or \
            type(exam.subject.semester) != int:
            raise Exception("Error type!")
        for i in self.exams:
            if i == exam:
                raise Exception('error')
        self.exams.append(exam)

    def add_exam_result(self, exam_points):
        t = (exam_points.exam.group.name, exam_points.exam.subject.name, exam_points.examDate)
        if t in self.exam_points.keys():
            self.exam_points[(exam_points.exam.group.name, exam_points.exam.subject.name, exam_points.examDate)].append(
                exam_points)
        else:
            self.exam_points[(exam_points.exam.group.name, exam_points.exam.subject.name, exam_points.examDate)] = [
                exam_points]

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

    def add_exam_marks(self, exam_result: ExamPoints):
        if type(exam_result) != ExamPoints:
            raise Exception('Type error')
        for i in self.exam_results:
            if i == exam_result:
                raise Exception('error')
        self.exam_results.append(exam_result)