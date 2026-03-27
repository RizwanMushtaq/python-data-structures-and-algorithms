# @RizwanMushtaq 20-03-2026
for value in range(0, 5):
    print(value)
print("***************")
for value in range(5):
    print(value)
print("***************")
numbers = list(range(5))
print(numbers)
print("***************")
even_numbers = list(range(0, 11, 2))
print(even_numbers)
print("***************")
squares = []
for value in range(0, 11):
    squares.append(value ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
print("***************")
# list comprehensions
squares = [value**2 for value in range(5, 11)]
print(squares)
print("***************")
numbers = list(range(0, 1000000))
print(sum(numbers))
