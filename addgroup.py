from classes.institute import *

def addgroup(institute):
    inst = Institute()
    name = input("Введите название группы: ")
    year = int(input("Введите год группы: "))
    spec = Specialization(input("Введите специализацию: "))
    group = Group(name, year, spec)
    inst.add_group(group)
    if (len(inst.groups)) == 1:
        print(inst.getGroup(name))
        print("Группа успешно добавлена")
    else:
        Exception("Ошибка добавления группы")