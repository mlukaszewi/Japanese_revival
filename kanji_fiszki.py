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


print('To exit: exit / 出る \n')

words = {'kanji':np.strings.strip(kanji), 'hiragana':np.strings.strip(reading), 'tłumaczenie':np.strings.strip(meaning)}
skroty = {'k': 'kanji', 'h':'hiragana', 't':'tłumaczenie'}
words_num = len(kanji)
tryb = None


print(f"Wybierz tryb: {', '.join(words.keys())} ({', '.join(skroty.keys())})\n")

while tryb not in words.keys() and tryb not in skroty.keys() and tryb != 'exit' and tryb != "出る":

    tryb = input().strip()

    clear_lines(1)


print('\n')


user_input = tryb

if tryb in skroty.keys(): tryb = skroty[tryb]


while user_input != 'exit' and user_input != '出る':

    i = np.random.randint(words_num)

    clear_lines(2)

    print(words[tryb][i])


    user_input = input().strip()

    while user_input in words.keys() or user_input in skroty.keys():

        if user_input in skroty.keys(): user_input = skroty[user_input]

        if user_input != tryb:

            clear_lines(2)
            print(words[tryb][i], f' ({words[user_input][i].strip()})')

            user_input = input().strip()

        else:

            clear_lines(2)
            print(words[tryb][i])

            user_input = input().strip()


