numbers = input('Enter three numbers separated by spaces: ')
coef = list(map(float, numbers.split()))
a = coef[0]
b = coef[1]
c = coef[2]
dis = b ** 2 - 4 * a * c
x1 = (-b + dis ** (1 / 2)) / 2
x2 = (-b - dis ** (1 / 2)) / 2
print(min(x1, x2), max(x1, x2), sep=' ')
