# День рождения
# Гагарина 9 марта 1934 года,
# Нагиева 4 апреля 1967,
# Путина 7 октября 1952,
# Тесла 10 июля 1856,
# Эйнштейна 14 марта 1879.
correct = 0
incorrect = 0

by_1 = input('В каком году родился  Юрий Гагарин? ')
if by_1 == '1934':
    correct += 1
else:
    incorrect += 1

by_2 = input('В каком году родился  Дмитрий Нагиев? ')
if by_2 == '1967':
    correct += 1
else:
    incorrect += 1

by_3 = input('В каком году родился  Владимир Путин? ')
if by_3 == '1952':
    correct += 1
else:
    incorrect += 1

by_4 = input('В каком году родился  Никола Тесла? ')
if by_4 == '1856':
    correct += 1
else:
    incorrect += 1

by_5 = input('В каком году родился  Альберт Эйнштейн? ')
if by_5 == '1879':
    correct += 1
else:
    incorrect += 1
vol = correct / 5 * 100
vol_2 = incorrect / 5 * 100
print('У вас', correct, 'правильных ответов.')
print('У вас', incorrect, 'неправильных ответов.')
print('У Вас', vol, '% правильных ответов.')
print('У Вас', vol_2, '% неправильных ответов.')
restsrt = input('Вы хотите начать заново?' 'Да/Нет ')
while restsrt == 'Да':
    correct = 0
    incorrect = 0

    by_1 = input('В каком году родился  Юрий Гагарин? ')
    if by_1 == '1934':
        correct += 1
    else:
        incorrect += 1

    by_2 = input('В каком году родился  Дмитрий Нагиев? ')
    if by_2 == '1967':
        correct += 1
    else:
        incorrect += 1

    by_3 = input('В каком году родился  Владимир Путин? ')
    if by_3 == '1952':
        correct += 1
    else:
        incorrect += 1

    by_4 = input('В каком году родился  Никола Тесла? ')
    if by_4 == '1856':
        correct += 1
    else:
        incorrect += 1

    by_5 = input('В каком году родился  Альберт Эйнштейн? ')
    if by_5 == '1879':
        correct += 1
    else:
        incorrect += 1
    vol = correct / 5 * 100
    vol_2 = incorrect / 5 * 100
    print('У вас', correct, 'правильных ответов.')
    print('У вас', incorrect, 'неправильных ответов.')
    print('У Вас', vol, '% правильных ответов.')
    print('У Вас', vol_2, '% неправильных ответов.')
    restsrt = input('Вы хотите начать заново?' 'Да/Нет ')