def get_password(number):
    password = ''
    
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

while True:
    try:
        n = int(input('Введите целое число от 3 до 20: '))
        if n.is_integer() and 2 < n < 21:
            break
        else:
            print('Ваше число слишком маленькое или очень большое. Нужно другое.')
    except ValueError:
        print('Это либо дробное число, либо строка. Совсем не то.')

result = get_password(n)
print('Пароль:', result)
