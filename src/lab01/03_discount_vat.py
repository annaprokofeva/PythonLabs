price = int(input("price="))
discount = int(input("discount=" ))
vat = int(input("vat="))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {'%.2f'%base} ₽')
print(f'НДС: {'%.2f'%vat_amount} ₽')
print(f'Итого к оплате: {'%.2f'%total} ₽')