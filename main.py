import constant
print(constant.PI)
print(constant.GRAVITY)
drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)

fruits = ["apple", "banana", "orange"]  # list
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple
alphabets = {'a': 'apple', 'b': 'orange', 'c': 'orange'}  # dictionary
vowels = {'a', 'b', 'c', 'd', 'e', 'f'}

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
