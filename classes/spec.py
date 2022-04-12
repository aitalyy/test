from main import Specialization
import openpyxl

def getSpecialization(file, name):
    subject = openpyxl.load_workbook(file)
    sheet = subject.active

    for row in range(1, sheet.max_row + 1):
        if sheet[row][0].value == name:
            name = sheet[row][0].value
            fullname = sheet[row][1].value
            return (Specialization(fullname))