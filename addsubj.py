from classes.institute import *

def addsubject(institute):
    inst = Institute()
    code = input("Введите код предмета: ")
    name = input("Введите имя предмета: ")
    semestr = int(input("Введите семестр: "))
    hours = int(input("Общее кол-во часов: "))
    specialization = Specialization(input("Специализация: "))
    subj = Subject(code, name, semestr, hours, specialization)
    inst.add_subject(subj)
    if (len(inst.subjects)) == 1:
        print(inst.getSubject(name))
        print("Предмет успешно добавлен")
    else:
        Exception("Ошибка добавления группы")