from math import sqrt
a=int(input('Введите коэффициент a: '))
b=int(input('Введите коэффициент b: '))
c=int(input('Введите коэффициент c: '))
d=b*b-(4*a*c)
if d < 0:
  print('Решений нет')
if d == 0:
  x = -1*b/2*a
  print(x)
if d>0:
  x1=(-1*b+sqrt(d))/2*a
  x2=(-1*b-sqrt(d))/2*a
  print(x1)
  print(x2)