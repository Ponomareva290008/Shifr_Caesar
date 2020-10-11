# -*- coding: utf-8 -*-
name = input('Как вас зовут?')
print('Привет,', name)
ABC = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = input('Введите слово, которое хотите зашифровать: ')
word = word.lower()
num = 0
try:
   num = int(input('Введите число от 1 до 10 (ключ шифра): '))
   if int(num) > 10:
        print('Вы ввели число больше 10.Шифр выведется неверный.Попробуйте еще раз!')
   elif int(num) < 1:
        print('Вы ввели число меньше 1.Шифр выведется неверный.Попробуйте еще раз!')
except ValueError:
    print('Это не число. Попробуйте еще раз.')
words = ''
for letter in word:
    a = ABC.find(letter)
    b = a + num
    words += ABC[b]
print('Ваш шифр: ', words)

shif = input('Введите слово, которое хотите расшифровать: ')
shif = shif.lower()
num_1 = 0
try:
   num_1 = int(input('Введите число от 1 до 10 (ключ шифра): '))
   if int(num_1) > 10:
        print('Вы ввели число больше 10.Шифр выведется неверный.Попробуйте еще раз!')
   elif int(num_1) < 1:
        print('Вы ввели число меньше 1.Шифр выведется неверный.Попробуйте еще раз!')
except ValueError:
    print('Это не число. Попробуйте еще раз.')
shifr = ''
for letter in shif:
    c = ABC.find(letter)
    d = c - num
    shifr += ABC[d]
print('Расшифровка: ', shifr)


