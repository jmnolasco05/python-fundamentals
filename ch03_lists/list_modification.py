guest_list = ['Michael Jackson', 'Juan Pablo Duarte', 'Mantequilla']
print(f'{guest_list[0]}, would you like to come over for dinner?')
print(f'{guest_list[1]}, would you like to come over for dinner?')
print(f'{guest_list[2]}, would you like to come over for dinner?')

print(f'{guest_list[1]} can not make it.')
guest_list[1] = 'Stephen Curry'
print(f'{guest_list[0]}, would you like to come over for dinner?')
print(f'{guest_list[1]}, would you like to come over for dinner?')
print(f'{guest_list[2]}, would you like to come over for dinner?')

print("I found a bigger table")
guest_list.insert(0, 'Russel M. Nelson')
guest_list.insert(2, 'Elon Musk')
guest_list.append('Bill Gates')
print(f'{guest_list[0]}, would you like to come over for dinner?')
print(f'{guest_list[1]}, would you like to come over for dinner?')
print(f'{guest_list[2]}, would you like to come over for dinner?')
print(f'{guest_list[3]}, would you like to come over for dinner?')
print(f'{guest_list[4]}, would you like to come over for dinner?')
print(f'{guest_list[5]}, would you like to come over for dinner?')

popped_guest = guest_list.pop()
print(f'Sorry, {popped_guest}, I can not invite you to dinner.')
popped_guest = guest_list.pop(3)
print(f'Sorry, {popped_guest}, I can not invite you to dinner.')
popped_guest = guest_list.pop()
print(f'Sorry, {popped_guest}, I can not invite you to dinner.')
popped_guest = guest_list.pop(1)
print(f'Sorry, {popped_guest}, I can not invite you to dinner.')

print(f'{guest_list[0]}, you are still invited.')
print(f'{guest_list[1]}, you are still invited.')

del guest_list[0]
del guest_list[0]

print(guest_list)