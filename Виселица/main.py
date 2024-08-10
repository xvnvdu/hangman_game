import random
import time
import sys
from loading import loading_bar

print('Добро пожаловать в игру Виселица !')

while True:
    try:
        tries = int(input('Введите желаемое количество попыток (максимум 20): '))
        while tries <= 0:
            if tries <= 0:
                tries = int(input('\nКоличество попыток не должно быть отрицательным или равным нулю.\nВведите желаемое количество попыток (максимум 20): '))
        if tries > 20:
            print('\nВы ввели число, больше максимального.')
            tries = 20
        break
    except:
        print('\nКоличество попыток должно быть целым числом !')

print(f'\nКоличество ваших попыток равно {tries}')

timer = 3
while timer > 0:
    print(f'\rНачало игры через {timer}...', end='')
    sys.stdout.flush()
    time.sleep(1)
    timer -= 1

word = list(random.choice(open('russian_nouns.txt', encoding='utf-8').read().split()))
unknown_word = '_ ' * len(word)
symbols = len(word)
symbols_guessed = 0
choices = []
eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

print(f'\r \nЗагаданое слово: {unknown_word}')
print(f'Букв отгадано: {symbols_guessed} из {symbols}')
print(f'Осталось попыток: {tries}')

unknown_word_list = list('_' * len(word))

while tries > 1:
    if symbols == symbols_guessed:
        loading_bar()
        print('\r \nПоздравляю, вы выиграли !')
        break

    letter = str(input('\nВведите букву: ').lower())
    found = False

    for i in range(len(word)):
        if letter == word[i]:
            unknown_word_list.pop(i)
            unknown_word_list.insert(i, letter.upper())
            found = True

    if letter.lower() in ru:
        if found:
            if letter not in choices:
                print(f'\nВерно !')
                time.sleep(1)
                print(f'\nЗагаданное слово: {" ".join(unknown_word_list)}')
                symbols_guessed = len(word) - unknown_word_list.count('_')
                print(f'Букв отгадано: {symbols_guessed} из {symbols}')
                print(f'Осталось попыток: {tries}')
                choices.extend(letter)
                print(f'Буквы, которые уже были использованы: {", ".join(choices)}')
                time.sleep(1)
            else:
                print(f'\nБуква {letter.upper()} уже была использована ранее !')
                time.sleep(1)
        else:
            if letter not in choices:
                print(f'\nБуква выбрана неверно, попробуйте еще раз !')
                time.sleep(1)
                print(f'\nЗагаданное слово: {" ".join(unknown_word_list)}')
                tries -= 1
                print(f'Букв отгадано: {symbols_guessed} из {symbols}')
                print(f'Осталось попыток: {tries}')
                choices.extend(letter)
                print(f'Буквы, которые уже были использованы: {", ".join(choices)}')
                time.sleep(1)
            else:
                print(f'\nБуква {letter.upper()} уже была использована ранее !')
                time.sleep(1)
    else:
        if len(letter) > 1:
            print(f'\nВам нужно ввести не более одного символа !')
            time.sleep(1)
        else:
            print('\nВведите букву кириллического алфавита !')
            time.sleep(1)

while tries == 1:
    letter = str(input('\nВведите букву: ').lower())

    found = False

    for i in range(len(word)):
        if letter == word[i]:
            unknown_word_list.pop(i)
            unknown_word_list.insert(i, letter.upper())
            found = True

    if letter.lower() in ru:
        if found:
            if letter not in choices:
                print(f'\nВерно !')
                time.sleep(1)
                print(f'\nЗагаданное слово: {" ".join(unknown_word_list)}')
                symbols_guessed = len(word) - unknown_word_list.count('_')
                print(f'Букв отгадано: {symbols_guessed} из {symbols}')
                print(f'Осталось попыток: {tries}')
                choices.extend(letter)
                print(f'Буквы, которые уже были использованы: {", ".join(choices)}')
                time.sleep(1)
            else:
                print(f'\nБуква {letter.upper()} уже была использована ранее !')
                time.sleep(1)
        else:
            print(f'\nБуква выбрана неверно, к сожалению, вы проиграли !')
            loading_bar()
            print(f'\r \nСлово, которое вы не угадали: {"".join(word)}', end='')
        break
    else:
        if len(letter) > 1:
            print(f'\nВам нужно ввести не более одного символа !')
            time.sleep(1)
        else:
            print('\nВведите букву кириллического алфавита !')
            time.sleep(1)
