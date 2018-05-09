usernames = ['rYan', 'ABBy', '  james  ']

username = input('Username: ')

if username in usernames:
    print('Access Granted')
else:
    sys.stdout.write('Sorry, we do not recognise that username')
