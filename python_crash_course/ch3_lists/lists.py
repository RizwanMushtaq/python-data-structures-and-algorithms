names = ["rizwan", "ali", "ahsan"]
print(names)
print("****************")
for name in names:
    print(name)
print("****************")
names.sort()
for name in names:
    print(f'hello {name}!')
print("****************")
places = ['pakistan', 'azerbeijan', 'germany', 'austria']
for place in places:
    print(f'hello {place}!')
print("****************")
sorted_places = sorted(places)
sorted_places.reverse()
for place in sorted_places:
    print(f'hello {place}!')
print("****************")
print(f"The no of places is {len(places)}")
