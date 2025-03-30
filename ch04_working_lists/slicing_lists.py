friend_list = ['Juan', 'Pedro', 'Santiago', 'Lucas', 'Pablo', 'Mateo', 'Stuart']

print(f'The first three items in the list are: {friend_list[:3]}')
print(f'Three items from the middle of the list are: {friend_list[2:5]}')
print(f'The last three items in the list are: {friend_list[-3:]}')

pizzas = ['ham', 'pepperoni', 'corn']
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('pineapple')

print(f'My favorite pizzas are {pizzas}')
print(f'My friends favorite pizzas are {friend_pizzas}')