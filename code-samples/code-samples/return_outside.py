starbucks_employee_id = input('id: ')
starbucks_employee_id = int(starbucks_employee_id)

employees = [1, 2, 3, 123]

print('starbucks_employee_id is {}'.format(starbucks_employee_id))

if starbucks_employee_id not in employees:
    print('Sorry, we could not find your ID')
    exit(1)


print('Do employee operations here...')
