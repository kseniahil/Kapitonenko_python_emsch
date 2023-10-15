numbers = input('Enter three numbers separated by spaces: ')
sides = list(map(float, numbers.split()))
p = (sides[0] + sides[1] + sides[2]) / 2
area = round((p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** (1 / 2), 3)
print(area)
