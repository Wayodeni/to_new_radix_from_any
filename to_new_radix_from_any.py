'''
This program translate number from any scale of notation to any other scale of
notation. (from 1th to 36th)
'''
import argparse
import sys


def error_message():
    print('What are you doing man? You have entered THE WRONG RADIX!!!!! >:E')
    sys.exit()


def get_key(dict, val):  # Function to get dictionary key by its value
    for k, v in dict.items():
        if v == val:
            return k


def new_radix_from_any(num, radix, new_radix):
    res = ''  # Resulting number if radix >= 16
    number_10 = 0  # Resulting number in 10th radix
    new_number = ''  # Numeral in radix >= 16 to make up number from it
    number = list(str(num))
    power_of_radix = 0
    num_alphabet = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
        18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
        26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
        34: 'Y', 35: 'Z'
    }

    for i in range(len(number) - 1, -1, -1):
        # Getting key by its value, to acquire number to letter, in radix that >= 16th.
        for j, k in num_alphabet.items():
            if number[i] == k:
                number[i] = get_key(num_alphabet, k)

        number_10 = number_10 + (int(number[i]) * radix**power_of_radix)
        power_of_radix += 1

    if new_radix != 10 and new_radix != 1:
        while number_10:  # Translating number in 10th radix to any other radix.
            new_number = int(number_10 % new_radix)
            if new_radix > 10:
                for j, k in num_alphabet.items():
                    if new_number == j:
                        new_number = k
            res = str(new_number) + res
            number_10 = number_10 // new_radix
        return res
    elif new_radix == 10:
        return number_10
    elif new_radix == 1:
        return '|' * number_10


parser = argparse.ArgumentParser(description='This is to_new_radix_from_any help.')
parser.add_argument('--n',
                    default=1,
                    type=str,
                    help='This argument requires number to translate.')
parser.add_argument('--r', type=int,
                    required=True,
                    help='This argument requires number radix.')
parser.add_argument('--tr',
                    default=1,
                    type=int,
                    help='This argument requires radix to translate into.')
args = parser.parse_args()
n = args.n.upper()
r = args.r
tr = args.tr
alphabet = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
    18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
    26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
    34: 'Y', 35: 'Z'
}

if n.isalnum() and str(r).isalnum() and str(tr).isalnum():
    if tr > 36 or r > 36:
        error_message()

    if not n.isdigit():  # Checking if number exceeds entered radix
        literals = n
        for i in literals:
            if i in '0123456789':
                literals = literals.replace(i, '')
        literals = list(''.join(sorted(literals)))
        max_literal = literals[-1]
        max_litnum = get_key(alphabet, max_literal)
        if r > max_litnum:
            print(new_radix_from_any(n, r, tr))
        else:
            error_message()
    else:
        print(new_radix_from_any(n, r, tr))

else:
    print('Please delete redundant symbols!')
    sys.exit()
