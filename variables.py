# Имя куклы
doll_name = input('Как назовете куклу ? ')
print(type(doll_name))

# части тела куклы

hands = int(input('Сколько хотите рук у куклы ? '))
print(type(hands))

foots = int(input('Сколько ног хотите у куклы ? '))
print(type(foots))

# кукла живая или нет
live = input('Ваша кукла живая ? yes / no: ')
if live == 'yes':
    live = False
elif live == 'no':
    live = True


print(live)
print(type(live))
# размер куклы

price = float(input('Какая длина куклы, в сантиметрах? '))
print(price)
print(type(price))
