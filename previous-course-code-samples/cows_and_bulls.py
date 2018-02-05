def generate_code():
    '''generate a string which represents a random 4-digit code with no dupes'''
    import random

    while True:
        num = random.randint(1023, 9999)
        if len(set(str(num))) == 4:
            break
        print(num, 'rejected')
    return str(num)

def find_bulls(code_str, guess_str):
    bulls = 0
    for index in range(0, 4):
        if code_str[index] == guess_str[index]:
            #print(code_str[index], 'is a bull')
            bulls += 1
    return bulls

def find_cows(code_str, guess_str):
    cows = 0
    for index1 in range(0, 4): # in code_str
        for index2 in range(0, 4):
            if index1 != index2: # don't compare [0] with [0]
                if code_str[index1] == guess_str[index2]:
                    #print(code_str[index1], 'is a cow')
                    cows += 1
    return cows

cows = 0
bulls = 0
num_guesses = 0
code = generate_code()
print('code is', code)

while bulls != 4:
    guess = input('Enter a 4-digit number not starting with zero (or "quit"): ')
    num_guesses += 1
    if guess == 'quit':
        break
    if len(guess) != 4 or not guess.isdigit():
        print('I said 4 digits.')
        continue
    if len(set(guess)) != 4:
        print('Your 4 digits must not have duplicates')
        continue
    cows = find_cows(code, guess)
    bulls = find_bulls(code, guess)
    if bulls < 4:
        print(cows, 'cows')
        print(bulls, 'bulls')
else:
    print('You got it in', num_guesses, 'guesses!')
