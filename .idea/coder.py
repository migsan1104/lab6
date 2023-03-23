def menu():
    print("Menu")
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
def encoder(code):
    string = ''
    for i in code:
        i = int(i)
        i += 3
        string += str(i)
        return string

a = 0
while a == 0:
    menu()
    op = int('Please enter an option: ')
    if op == 3:
        break
    if op == 1:
        code = input("Please enter your password to encode: ")
        encoder(code)
        print("Your password has been encoded and stored")
        string1 = string
    if op == 2:
        decode = ''
        for i in string1:
            i = int(i)
            i = i + 3
            decode += str(i)
        print(f'The encoded password is {string1}, and the original password is {decode}.')





