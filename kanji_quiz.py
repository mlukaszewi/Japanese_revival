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


print('To exit: exit / 出る, to skip a word: skip / スキップ, to show the anwser: nie wiem / わからない \n')


words = {'kanji':np.strings.strip(kanji), 'hiragana':np.strings.strip(reading), 'tłumaczenie':np.strings.strip(meaning)}
words_num = len(kanji)
tryb = 'tłumaczenie'

user_input = ''


while user_input != 'exit' and user_input != '出る':

    i = np.random.randint(words_num)

    print(words[tryb][i], '\n')


    user_input = input().strip()


    while user_input != kanji[i].strip() and user_input != 'exit' and user_input != '出る' and user_input != 'skip' and user_input != 'スキップ':

        if user_input == "nie wiem" or user_input == "わからない":
            clear_lines(3)
            print(words[tryb][i], words['kanji'][i], words['hiragana'][i], '\n')
            #print(words['kanji'][i], words['hiragana'][i])
            user_input = input().strip()
            if user_input != 'exit' and user_input != '出る': user_input = words['kanji'][i]

        else:
            clear_lines(1)
            user_input = input().strip()


    clear_lines(3)


