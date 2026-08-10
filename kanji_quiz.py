import numpy as np
import sys

# add new words from terminal:
# echo "tekst" >> nazwa_pliku

if len(sys.argv) > 1 : plik = sys.argv[1]
else: plik = '漢字.txt'

if len(sys.argv) > 2: delim = sys.argv[2]
else: delim = '-'


def clear_lines(n):

    for l in range(n):
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")



kanji, reading, meaning = np.loadtxt(plik, dtype=str, delimiter=delim, unpack=True)


print('To exit: exit / 出る, to skip a word: skip / スキップ, to show the anwser: nie wiem / わからない, to get each word once: all / 全部 \n')


words = {'kanji':np.strings.strip(kanji), 'hiragana':np.strings.strip(reading), 'tłumaczenie':np.strings.strip(meaning)}
words_num = len(kanji)
words_total = len(kanji)
tryb = 'tłumaczenie'
countdown = False
licznik = ''

user_input = ''
correct_guess = True

while user_input != 'exit' and user_input != '出る' and words_num != 0:

    i = np.random.randint(words_num)

    print(words[tryb][i], licznik, '\n')

    user_input = input().strip()

    if user_input == 'all' or user_input == '全部':
        countdown = True
        licznik = '\t' + '0 / ' + str(words_total)
        user_input = 'skip'


    while user_input != words['kanji'][i].strip() and user_input != 'exit' and user_input != '出る' and user_input != 'skip' and user_input != 'スキップ':

        if user_input == "nie wiem" or user_input == "わからない":
            correct_guess = False
            clear_lines(3)
            print(words[tryb][i], words['kanji'][i], words['hiragana'][i], licznik, '\n')
            #print(words['kanji'][i], words['hiragana'][i])
            user_input = input().strip()

            if user_input == 'all' or user_input == '全部':
                countdown = True
                licznik = '\t' + '0 / ' + str(words_total)
                pass

            if user_input != 'exit' and user_input != '出る': user_input = words['kanji'][i]

        else:
            clear_lines(1)
            user_input = input().strip()

            if user_input == 'all' or user_input == '全部':
                countdown = True
                licznik = '\t' + '0 / ' + str(words_total)
                pass


    if user_input == 'skip' or user_input == 'スキップ': correct_guess = False

    if countdown and correct_guess:
        for key in words.keys():
            words[key] = np.delete(words[key], i)

        words_num -= 1

        licznik = '\t' + str(words_total - words_num) + ' / ' + str(words_total)

    correct_guess = True

    clear_lines(3)


if words_num == 0:
    print('終わった!')
