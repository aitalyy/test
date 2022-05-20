from classes.institute import Institute
from addstud import addstud
from addspec import addspec
from addgroup import addgroup
from addsubj import addsubject
import sys


def main(*args):
    inst = Institute()
    if len(args[0]) == 1:
        print('Ошибка: доступные команды add + [stud, spec, group, subj]')
        quit()
    if len(args[0]) == 3:
        if args[0][1] + ' ' + args[0][2] == 'add stud':
            addstud(inst)
        if args[0][1] + ' ' + args[0][2] == 'add spec':
            addspec(inst)
        if args[0][1] + ' ' + args[0][2] == 'add group':
            addgroup(inst)
        if args[0][1] + ' ' + args[0][2] == 'add subj':
            addsubject(inst)

if __name__ == "__main__":
    main(sys.argv)