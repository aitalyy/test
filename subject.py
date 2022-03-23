from main import Subject, Specialization
import openpyxl

def getSubject(file, name_sub):
    subject = openpyxl.load_workbook(file)
    sheet = subject.active

    for row in range(1, sheet.max_row):
        if sheet[row][1].value == name_sub:
            code = sheet[row][0].value
            name = sheet[row][1].value
            specialization = Specialization(sheet[row][2].value)
            semester = int(sheet[row][3].value)
            hours = int(sheet[row][4].value)
            return (Subject(code, name, semester, hours, specialization))