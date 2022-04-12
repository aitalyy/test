from main import Group, Specialization
import openpyxl

def getGroup(file, name):
    subject = openpyxl.load_workbook(file)
    sheet = subject.active

    for row in range(1, sheet.max_row + 1):
        if sheet[row][0].value == name:
            name = sheet[row][0].value
            year = int(sheet[row][1].value)
            Specialization = sheet[row][2].value
            return (Group(name, year, Specialization))