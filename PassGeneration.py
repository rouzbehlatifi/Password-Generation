import string,random

while True:
    length = int(input('please enter your password length: '))
    charc = string.ascii_letters + string.digits + '!@#$%^&*()-+'
    password = ''.join([random.choice(charc) for i in range(length)])

    print('your pass is : {}'.format(password))


    while True:
        answer = input('Do you want another password (Y/N) : ').lower()

        if answer == 'n' or answer == 'y':
            break
    
    if answer == 'n':
        break
    
