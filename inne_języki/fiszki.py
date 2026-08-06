import numpy as np
import sys

# add new words from terminal:
# echo "tekst" >> nazwa_pliku

if len(sys.argv) > 1 : plik = sys.argv[1]
else: raise Exception('Nie podano nazwy pliku')

if len(sys.argv) > 2: delim = sys.argv[2]
else: delim = '-'


def clear_lines(n):

    for l in range(n):
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")



awers, rewers = np.loadtxt(plik, dtype=str, delimiter=delim, unpack=True)


print('To exit: exit / 出る, to change the mode: flip / ひるがえす, to show the anwser: nie wiem / わからない \n')

words = {'awers':np.strings.strip(awers), 'rewers':np.strings.strip(rewers)}
words_num = len(awers)
tryb = 'awers'

print('\n')


user_input = ''


while user_input != 'exit' and user_input != '出る':

    i = np.random.randint(words_num)

    clear_lines(2)

    print(words[tryb][i])

    user_input = input().strip()


    if user_input == "nie wiem" or user_input == "わからない":

            clear_lines(2)
            print(words['awers'][i], words['rewers'][i])

            user_input = input().strip()


    if user_input == 'flip' or user_input == 'ひるがえす':

        if tryb == 'awers':

            tryb = 'rewers'

        else:

            tryb = 'awers'




