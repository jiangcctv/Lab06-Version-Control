"""
Author: Cindy Jiang
"""

def encode(original):
    code = ''
    # decodes by adding three to each int
    for i in range(len(original)):
        new = int(original[i]) + 3
        # checks if int is within range, else gets only the ones digit
        if new >= 10:
            new = new % 10
        code += str(new)
    return code

def decode(code):
    originalPass = ""
    decodedNum = 0

    for x in code: 
        decodedNum = (int(x) - 3)
        if decodedNum < 0:
            decodedNum = ((int(x) + 10) - 3)
            # if the decoded number is less than 1, it means that, when encoded, the original number was two digits
            # we need to combat this by turning it back into its two digit form, and then subtracting 3 to get the original number in the password
            originalPass += str(decodedNum)
        else:
            originalPass += str(decodedNum)
    
    return originalPass


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
            print(f'The encoded password is {code}, and the original password is {decode(code)}.\n')
        else:
            cont = False


main()
