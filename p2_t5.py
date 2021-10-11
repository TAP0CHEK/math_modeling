a = int(input('Введите число: '))
b = int(input('Введите число: '))
if b == 0:
  print('Делитель равен нулю')
  d = a / b
print(d)
if a % b == 0:
  print('Делится')
else:
 c = a % b
 print(c)