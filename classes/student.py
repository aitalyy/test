from main import Student
import openpyxl

def getStudent(file, studcode):
    if studcode < 0:
        raise Exception('Номер зачетки отрицательным быть не может')
    if type(studcode) != int:
        raise Exception('Номер зачетки должен числовым')
    if studcode == None:
        raise Exception('Введите номер зачетки')
    subject = openpyxl.load_workbook(file)
    sheet = subject.active

    for row in range(1, sheet.max_row + 1):
        if sheet[row][1].value == studcode:
            fio = sheet[row][0].value
            code = int(sheet[row][1].value)
            return (Student(code, fio))
