foods = ('bread', 'coffee', 'coke', 'barfi', 'cake')
# this will raise error: TypeError: 'tuple' object does not support item assignment
# foods[3] = 'water'
foods = tuple(range(0, 3))
print(foods)
print(foods.__hash__)
