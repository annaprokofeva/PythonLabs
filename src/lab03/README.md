# Лабороторная работа 3

## Задание 1

```python
#1_normalize
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    if text is None:
        raise ValueError
    if not isinstance(text, str):
        raise TypeError
    if len(text) == 0:
        return ""
    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize(" двойные пробелы "))
```
![Картинка 1](./images/normalize_output.png)

## Задание 2

```python
#2_tokenize
import re
def tokenize(text: str) -> list[str]:
    reg = r'\w+(?:-\w+)*'
    text = re.findall(reg, text)
    return text

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![Картинка 2](./images/tokenize_output.png)

## Задание 3

```python
#3_count_freq
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    if not tokens:
        return {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) +1
    return freq_dict

print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
```
![Картинка 3](./images/count_freq_output.png)

## Задание 4

```python
#4_top_n
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    items = list(freq.items())
    items.sort(key=lambda x: x[0])           # Сортировка по слову A→Z
    items.sort(key=lambda x: x[1], reverse=True)  # Сортировка по частоте 9→0
    return items[:n]

freq1 = {"a": 3, "b": 2, "c": 1}
print(top_n(freq1, 2))
freq2 = {"bb": 2, "aa": 2, "cc": 1}
print(top_n(freq2, 2))
```
![Картинка 4](./images/top_n_output.png)
# Вывод
В ЛР №3 создана система анализа текста с четырьмя основными модулями: нормализация, токенизация, подсчёт частот и вывод наиболее частых слов. Все функции протестированы и подготовлены для использования в следующих работах.