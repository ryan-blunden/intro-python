
def palin(string):
    '''Return True is the string is a palindrome.'''
    string = string.lower().replace(' ', '')
    print(string[:len(string) // 2])
    print(string[round(len(string) / 2 + 0.5):])
    return string[:len(string) // 2] \
        == string[round(len(string) / 2 + 0.1):][::-1]

def palin(string):
    '''Return True is the string is a palindrome.'''
    string = string.lower().replace(' ', '')

    return string == string[::-1]

