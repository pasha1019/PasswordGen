# Генерация пароля и передача его в буфер обмена
import secrets
import random
import string
import pyperclip

list_symbol = string.ascii_letters + string.digits
passW = ''
print("Выберите из списка сложность пароля")
print('1. Простой пароль\n'
      '2. Средняя стойкость\n'
      '3. Высокая стойкость\n')
level_pass = input()
if int(level_pass) == 1:
    for i in range(8):
        passW += str(random.randint(0,9)) # Генерация простого пароля
elif int(level_pass) == 2:
    passW = ''.join(secrets.choice(list_symbol) for i in range(9))
elif int(level_pass) == 3:
    while True:
        print('Уточните длину пароля:')
        length = input()
        try: # Защита от "дурака"
            if int(length) < 9:
                print('Пароль должен содержать минимум 9 символов')
            elif int(length) > 99:
                print('Зачем Вам такой длинный пароль?')
            else:
                break
        except:
            print('Введите число')
    while True:
        passW = ''.join(secrets.choice(list_symbol) for i in range(int(length)))
        if (any(c.islower() for c in passW)
            and any(c.isupper() for c in passW)
            and sum(c.isdigit() for c in passW) >= 3):
                break
print(passW)
pyperclip.copy(passW)
