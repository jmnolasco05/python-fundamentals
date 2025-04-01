user_names = ['john05', 'testUser54', 'admin', 'maria123', 'dropper3342']

for user_name in user_names:
    if(user_name == 'admin'):
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user_name}, thank you for logging in again.')
        
ordinals = [1,2,3,4,5,6,7,8,9]
for ordinal in ordinals:
    if ordinal == 1:
        print('1st')
    elif ordinal == 2:
        print('2nd')
    else:
        print(f'{ordinal}th')