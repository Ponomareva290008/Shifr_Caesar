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




