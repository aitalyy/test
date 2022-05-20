from classes.institute import *

def addstud(institute):
    inst = Institute()
    fio = input("ФИО: ")
    code = int(input("Номер студки: "))
    stud = Student(code, fio)
    inst.add_stud(stud)
    if (len(inst.students)) == 1:
        print(inst.getStudent(code))
        print("Студент успешно добавлен")
    else:
        Exception("Ошибка добавления студента")