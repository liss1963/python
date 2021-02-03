side_a = float(input('Please, enter side A: '))
side_b = float(input('Please, enter side B: '))
side_c = float(input('Please, enter side C: '))
half_p = (side_a+side_b+side_c)/2
print(half_p)
square = (half_p*(half_p-side_a)*(half_p-side_b)*(half_p-side_c))**0.5
print(square)
side_a, side_b, side_c = input('Please, enter sides: ').split()
print(float(side_a))
print(float(side_b))
print(float(side_c))
a, b, c, d = 1, 'hello', True, 4.25
print(a)
print(b)
print(c)
print(d)


