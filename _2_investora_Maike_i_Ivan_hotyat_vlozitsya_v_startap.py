
x = int(input("Минимальная сумма инвестиции: "))
a = int(input("Cумма инвестиции Майкла: ")) # Mike
b = int(input("Cумма инвестиции Ивана: ")) # Ivan
if (a >= x) and (b >= x):
    print(2)
elif (a >= x):
    print("Mike")
elif (b >= x):
    print("Ivan")
elif(a + b >= x):
    print(1)
else:
    print(0)