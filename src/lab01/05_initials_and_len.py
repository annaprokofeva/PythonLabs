fullname = input("ФИО: ")
name, second_name, last_name = [str(x) for x in fullname if x in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"]
fullname1 = "".join([name, second_name, last_name])

print(f'Инициалы: {fullname1}')
print(f'Длина (символов): {len(fullname)}')