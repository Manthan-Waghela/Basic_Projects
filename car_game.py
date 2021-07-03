user_input =''
started = True
while True:
    user_input = input('>').lower()
    if user_input == 'help':
        print('''
        start - To start the car.
        stop - to stop the car.
        quit - to exit the game.
        ''')
    elif user_input == 'start':
        if started:
            print('car has already started')
        else:
            started = True
            print('car started...')
    elif user_input == 'stop':
        if started:
            started = False
            print('car stopped.')
        else:
            print('car has already stopped!')
    elif user_input == 'quit':
        break
    else:
        print('enter proper commands!')