def sum(a, b): return a + b


print(sum(1, 3))

# sum = lambda a , b : a + b
# print(sum(1, 3))


# numbers = [item for item in range(0, 1001) if item % 2 == 0 ]
numbers = [item if item % 2 == 0 else "odd" for item in range(0, 1001)]

# print(numbers)
