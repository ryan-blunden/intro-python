# Block examples

temp = int(input('What is the temperature today? '))
wear_gloves = None

# If block
if temp >= 40:
    print('That is not too cold...')
    wear_gloves = False

# else block
else:
    print('The weather is freezing')
    wear_gloves = True

print('Are we going to wear gloves? {}'.format(wear_gloves))


print('block_scope_var = {}'.format(block_scope_var))
