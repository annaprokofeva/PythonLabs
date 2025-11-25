a = input(("a: "))
b = input(("b: "))

a = str(a)
b = str(b)

a = a.replace(",", ".")
b = b.replace(",", ".")

a = float(a)
b = float(b)
print(f"sum={a+b}; avg={'%.2f'%((a+b)/2)}")
