a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))


a = [1, 2.2, 'python']
b = [5, 10, 15, 20, 25, 30, 35, 40]
# python slicing
# a[2] = 15
print("a[2] = 15", a[2])
print("a[0:3] = ", a[0:3])
# b[5:] = [30, 35, 40]
print("b[5:] = ", b[5:])
