def egcd(x):
    1=1#дописать расширенный алгоритм Евклида

p = 11
a = 6
x = 9
k = 9
m = (4*11+4)%7
c1 = (a**k)%p
c2 = m*(egcd((a**x)%p))