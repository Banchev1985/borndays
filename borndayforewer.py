bornyaer = input('В каком году родился А.С Пушкин? ')
bornday = input('В какой день родился А.С Пушкин? ')
while bornyaer != '1799':
    bornyaer = input('В каком году родился А.С Пушкин? ')
    if bornyaer == '1799':
        bornday = input('В какой день родился А.С Пушкин? ')
while bornday != '26 мая':
    bornday = input('В какой день родился А.С Пушкин? ')
    if bornday == '26 мая':
        print('Верно')
