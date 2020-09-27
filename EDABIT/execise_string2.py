string = input('Enter a string: ')
if string >='A' and string <='Z' and string >= '0' and string <= '9':
    print('This is what I found about that string:')
    print("The string is alphanumeric.")
    print('The letters in the string are all upprecase.')
elif string >='a' and string <='z' and string >= '0' and string <= '9':
     print('This is what I found about that string:')
     print("The string is alphanumeric.")
     print('The letters in the string are all lowercase.')
elif string >='a' and string <='z':
    print('This is what I found about that string:')
    print("The string is alphanumeric.")
    print('The string contains only alphabetic characters.')
    print('The letters in the string are all lowercase.')
elif string >='A' and string <='Z':
    print('This is what I found about that string:')
    print("The string is alphanumeric.")
    print('The string contains only alphabetic characters')
    print('The letters in the string are all uppercase.')
elif string >='0' and string <='9':
    print('This is what I found about that string:')
    print("The string is alphanumeric.")
    print('The string contains only digits.')
    