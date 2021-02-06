from fractions import Fraction

[left, right] = input().split(' + ')
[a, b] = left.split('/')
[c, d] = right.split('/')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

frac = Fraction(a, b) + Fraction(c, d)
first = f"{frac.numerator // frac.denominator}"
second = f"{frac.numerator % frac.denominator}/{frac.denominator}"

if first != "0":
    print(first, end='')
    if second.split("/")[0] != "0":
        print(" ", end='')

if second.split("/")[0] != "0":
    print(second)



