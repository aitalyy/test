from dataclasses import dataclass
from datetime import date

@dataclass
class Student:
    code:int
    fio:str

    def __init__(self, code:int, fio:str):
        self.code = code
        self.fio = fio

@dataclass
class Specialization:
    name:str

    def __init__(self, name:str):
        self.name = name

@dataclass
class Group:
    name:str
    year:int
    specialization:Specialization

    def __init__(self, name:str, year:int, specialization:Specialization):
        self.name = name
        self.year = year
        self.specialization = specialization

@dataclass
class ExamPoints:
    student:Student
    inPoints:float
    examPoints:float

    def __init__(self, student:Student, inPoints:float, examPoints:float):
        self.student = student
        self.inPoints = inPoints
        self.examPoints = examPoints

@dataclass
class Subject:
    code:str
    name:str
    semester:int
    hours:int
    specialization:Specialization

    def __init__(self, code:str, name:str, semester:int, hours:int, specialization:Specialization):
        self.code = code
        self.name = name
        self.semester = semester
        self.hours = hours
        self.specialization = specialization

@dataclass 
class Exam:
    subject:Subject
    examDate:date
    year:str
    lecturer_fio:str

    def __init__(self, subject:Subject, examDate:date, year:str, lecturer_fio:int):
        self.subject = subject
        self.examDate = examDate
        self.year = year
        self.lecturer_fio = lecturer_fio
