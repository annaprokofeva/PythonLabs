def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
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
