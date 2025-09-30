fullname = str(input(("Введите ФИО: ")))
fullname = " ".join(fullname.split())
fullname1 = fullname.split()

if len(fullname1)==3:
    surname, name, secondname = fullname1
initials=f"{surname[0]}{name[0]}{secondname[0]}."

print("Инициалы:" , initials)
print("Длина(символов):" , len(fullname))
