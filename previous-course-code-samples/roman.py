roman = { 
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

numeral = input('Enter a Roman numeral: ')
arabic_list = []

for digit in numeral:
    if digit not in roman:
        print('invalid Roman numeral')
        break
    arabic_list.append(roman[digit])

print(arabic_list)
for index in range(0, len(arabic_list) - 1):
    if arabic_list[index] < arabic_list[index + 1]:
        arabic_list[index + 1] = arabic_list[index + 1] - arabic_list[index]
        arabic_list[index] = 0
    sum = 0
    print(arabic_list)
    for num in arabic_list:
        sum = sum + num
    print(sum)
