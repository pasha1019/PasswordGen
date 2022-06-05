# Генерация пароля и передача его в буфер обмена
import random
import pyperclip

print("Выберите из списка сложность пароля")
print('1. Простой пароль\n'
      '2. Средняя стойкость\n'
      '3. Высокая стойкость\n')
level_pass = input() # Ввод уровня сложности
passW=''
chars1 = 'abcdefghijklnopqrstuvwxyz' \
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars2 = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyz' \
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
if int(level_pass) == 1:
    for i in range(8):
        passW += str(random.randint(0,9)) # Генерация простого пароля
elif int(level_pass) == 2:
    for i in range(8):
        passW += random.choice(chars1) # Генерация пароля средней сложности
elif int(level_pass) == 3:
    while True:
        print('Уточните длину пароля:')
        length = input()
        try: # Защита от "дурака"
            if int(length) < 9:
                print('Пароль должен содержать минимум 9 символов')
            else:
                break
        except:
            print('Введите число')
    for i in range(int(length)):
        passW += random.choice(chars2) # Генерация пароля высокой сложности
print(passW)
pyperclip.copy(passW)
