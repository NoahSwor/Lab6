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

def encode():
    password1 = input('Please enter your password to encode: ')
    print('Your password has been encoded and stored!')
    main()
  # Neils decode
def decode(user_pw):
    key = {
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 0,
            11: 1,
            12: 2
    }
    global encoded_str_pw
    for i in range(8):
        encoded_user_pw.append(key[(int(user_pw[i]) + 3)])
        encoded_digit = str(encoded_user_pw[i])
        encoded_str_pw = encoded_str_pw + encoded_digit
        return encoded_str_pw

    encoded_user_pw = []
    encoded_str_pw = ''

main()
