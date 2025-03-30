for number in range(1,21):
    print(number)
    
million_list = range(1, 1_000_001)
    
print(min(million_list))
print(max(million_list))
print(sum(million_list))

for odd in range(1, 21, 2):
    print(odd)
    
for multiples in range(3, 31, 3):
    print(odd)


cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)