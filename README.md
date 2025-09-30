# PythonLabs

# Лабороторная работа 1

## Задание 1

```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.") 
```
![Картинка 1](/images/01_output.png)

## Задание 2

```python
a = input(("a: "))
b = input(("b: "))

a = str(a)
b = str(b)

a = a.replace(",", ".")
b = b.replace(",", ".")

a = float(a)
b = float(b)
print(f"sum={a+b}; avg={'%.2f'%((a+b)/2)}")
```
![Картинка 2](/images/02_output.png)

## Задание 3

```python
price = int(input("price="))
discount = int(input("discount=" ))
vat = int(input("vat="))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {'%.2f'%base} ₽')
print(f'НДС: {'%.2f'%vat_amount} ₽')
print(f'Итого к оплате: {'%.2f'%total} ₽')
```
![Картинка 3](/images/03_output.png)

## Задание 4

```python
m = int(input('Минуты: '))
print(f"{m//60}:{m-(m//60)*60}")
```
![Картинка 4](/images/04_output.png)

## Задание 5

```python
fullname = str(input(("Введите ФИО: ")))
fullname = " ".join(fullname.split())
fullname1 = fullname.split()

fullname = fullname.replace(' ', "")

if len(fullname1)==3:
    surname, name, secondname = fullname1
initials=f"{surname[0]}{name[0]}{secondname[0]}."

print("Инициалы:" , initials)
print("Длина(символов):" , len(fullname))
```
![Картинка 5](/images/05_0utput.png)

# Вывод

Практически освоила основы Python: научилась работать с вводом данных, проводить расчеты и обрабатывать строки. На основе этих знаний смогу создавать консольные программы для решения конкретных задач. Освоила Github.
