# Noah Swor
def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    operation = input('Please enter an option: ')
    if operation == "1":
        encode()
    # elif operation == 2:
        # decode()
def encode():
    password1 = input('Please enter your password to encode: ')
    print('Your password has been encoded and stored!')
    main()
# def decode():
     #  code for partner to add
main()
