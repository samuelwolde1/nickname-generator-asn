import random
loop = True

first_name = input('Please enter first name: ')
last_name = input('Please enter last name: ')

nicknames = ['Crusher', 'the Scientist', 'Twinkle-toes', 'the Coder', 'the Jester', 'the Sloth', 'Quick-Silver']

while loop == True:
    print('\nMain Menu (' + first_name + " " + last_name + ")")
    print('1. Change Name')
    print('2. Display a Random Nickname')
    print('3. Display all Nicknames')
    print('4. Add a Nickname')
    print('5. Remove a Nickname')
    print('6. Exit')
    selection = input('Enter menu option #: ')

    if selection == '1':
        print('Change Name')
        first_name = input('Please enter first name: ')
        last_name = input('Please enter last name: ')
        print('Name has been changed to ' + first_name + " " + last_name + ".")
    elif selection == '2':
        print('Random Nickname')
        print(first_name + " " + random.choice(nicknames) + " " + last_name)
    elif selection == '3':
        print('All Nicknames')
        for name in nicknames:
            print(first_name + " '" + name + "' " + last_name)
    
    elif selection == '4':
        print('Add a Nickname')
        new_nickname = input('Please enter a nickname to add: ')
        if new_nickname in nicknames:
            print(new_nickname + " is already in the nickname list")
        else:
            nicknames.append(new_nickname)
            print(new_nickname + " added to the nickname list")
    elif selection == '5':
        print('Remove a Nickname')
        removed_nickname = input("Please enter a nickname to remove: ")
        if removed_nickname in nicknames:
             nicknames.remove(removed_nickname)
             print(removed_nickname + " removed from the nickname list")
        else:
            print(removed_nickname + " was not found in the nickname list.")
    else:
        exit()