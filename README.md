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
print(f"{m//60}:{(m-(m//60)*60):02d}")
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
print("Длина(символов):" , len(fullname)+2)
```
![Картинка 5](/images/05_0utput.png)

# Вывод

Практически освоила основы Python: научилась работать с вводом данных, проводить расчеты и обрабатывать строки. На основе этих знаний смогу создавать консольные программы для решения конкретных задач. Освоила Github.

# Лабороторная работа 2

## Задание 1

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return ("ValueError")
    minimum = min(nums)
    maximum = max(nums) 
    return(minimum,maximum)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```
![Картинка 1](/images/min_max_output.png)

## Задание 2

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return(sorted(set(nums)))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![Картинка 2](/images/unique_sorted_output.png)

## Задание 3

```python
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if isinstance(row,(tuple,list)):
            result.extend(row)
        else:
            return ('TypeError')
    return(result)

print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![Картинка 3](/images/flatten_output.png)

## Задание 4

```python
def transpose(mat: list[list[float | int]]):
    if not mat:
        return []
    rows=len(mat)
    cols=len(mat[0])
    for row in mat:
        if len(row)!=cols:
            return ("ValueError")
    new_mat = [[mat[i][j] for i in range(rows)] for j in range(cols)]
    return new_mat
print(transpose([[1, 2, 3]]))
print(transpose([[1],[2], [3]]))
print(transpose([[1,2],[3,4]]))
print(transpose([[1,2],[3]]))
print(transpose([[]]))
```
![Картинка 4](/images/transpose_output.png)

## Задание 5

```python
def row_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            return ("ValueError")
    sums=[sum(row) for row in mat]
    return sums
print(row_sums([[1,2,3], [4,5,6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1,2], [3]]))
```
![Картинка 5](/images/row_sums_output.png)

## Задание 6

```python
def col_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            return ("ValueError")
    sums = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]
    return sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![Картинка 6](/images/col_sums_output.png)

## Задание 7

```python
def format_record(rec: tuple[str, str, float]):
    fio, group, gpa = rec
    parts = fio.strip().split()
    family = parts[0]
    initials = ""
    for part in parts[1:]:
        initials += part[0].upper() + "."
    if not initials:
        initials = ""
    form_gpa=f"{gpa:.2f}"
    return f"{family} {initials}, гр. {group}, GPA {form_gpa}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![Картинка 7](/images/tuples_output.png)

# Вывод
Я освоила базовые операции с данными: поиск минимума и максимума, удаление дубликатов, работу с матрицами и текстом. Теперь я умею работать с данными: убирать повторы, суммировать матрицы и форматировать текст.

