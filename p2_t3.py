a = int(input('Введите год: '))
if a % 400 == 0:
  print('Високосный')
if a % 100 == 0 and a % 400 !=0:
 print('Невисокосный')
if a % 4 == 0 and a % 100 !=0:
 print('Високосный')
if a % 4 != 0 and a % 400 !=0:
 print('Невисокосный')