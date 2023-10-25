"""
Author: Cindy Jiang
"""

def encode(original):
    code = ''
    for i in range(len(original)):
        new = int(original[i]) + 3
        if new >= 10:
            new = new % 10
        code += str(new)
    return code


def output_menu():
    print('Menu')
    print('-'*13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')


def main():
    cont = True
    code = ''
    pw = ''
    while cont:
        output_menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            pw = input('Please enter your password to encode: ')
            code = encode(pw)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            print(f'The encoded password is {code}, and the original password is {pw}.')
        else:
            cont = False


main()
