def text_to_boolean(text):
    return text.lower().strip() == 'yes'


is_seattle_sunny = text_to_boolean(input('Is Seattle Sunny today? (yes|no) '))

if is_seattle_sunny:
    print('Hooray!')
else:
    print('Boooooo!')
