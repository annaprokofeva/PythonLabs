import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab09.group import Group
from src.lab08.models import Student

def print_students(title, students):
    print("\n" + title)
    for s in students:
        print(f"{s.fio} | {s.birthdate} | {s.group} | {s.gpa}")
        

g = Group("src/lab09/students.csv")

print_students("Изначальный CSV:", g.list())

new_st = Student("Прокофьева Анна Александровна", "2007-08-14", "БИВТ-25-8", 4.7)
g.add(new_st)
print_students("После добавления:", g.list())

found = g.find("те")  # ищем по подстроке
print_students("Поиск 'те':", found)

g.update("Петров Петр Петрович", gpa=4.1, group="БИВТ-21-5")
print_students("После обновления данных Петрова:", g.list())

g.remove("Сидорова Милана Сергеевна")
print_students("После удаления Сидоровой:", g.list())