# -*- coding: utf-8 -*-
ABC = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
word = input('Введите слово, которое хотите зашифровать(на английском): ')
word = word.lower()
num = int(input('Введите число от 1 до 10 (ключ шифра): '))
words = ''
for letter in word:
    a = ABC.find(letter)
    b = a + num
    words += ABC[b]
print('Ваш шифр: ', words)

shif = input('Введите слово, которое хотите расшифровать(на английском): ')
shif = shif.lower()
num_1 = int(input('Введите число от 1 до 10: '))
shifr = ''
for letter in shif:
    c = ABC.find(letter)
    d = c - num
    shifr += ABC[d]
print('Расшифровка: ', shifr)


