"""
Это программа переводит число из 10чной системы счисления в n-ичную. (до 36ичной включительно)
"""

def new_radix (num, radix):
    print('Исходное число: ', num)
    output = ''
    while num:
        new_number = num % radix

        if radix >= 16:
            if new_number == 10 : new_number = 'A'
            if new_number == 11 : new_number = 'B'
            if new_number == 12 : new_number = 'C'
            if new_number == 13 : new_number = 'D'
            if new_number == 14 : new_number = 'E'
            if new_number == 15 : new_number = 'F'
            if new_number == 16 : new_number = 'G'
            if new_number == 17 : new_number = 'H'
            if new_number == 18 : new_number = 'I'
            if new_number == 19 : new_number = 'J'
            if new_number == 20 : new_number = 'K'
            if new_number == 21 : new_number = 'L'
            if new_number == 22 : new_number = 'M'
            if new_number == 23 : new_number = 'N'
            if new_number == 24 : new_number = 'O'
            if new_number == 25 : new_number = 'P'
            if new_number == 26 : new_number = 'Q'
            if new_number == 27 : new_number = 'R'
            if new_number == 28 : new_number = 'S'
            if new_number == 29 : new_number = 'T'
            if new_number == 30 : new_number = 'U'
            if new_number == 31 : new_number = 'V'
            if new_number == 32 : new_number = 'W'
            if new_number == 33 : new_number = 'X'
            if new_number == 34 : new_number = 'Y'
            if new_number == 35 : new_number = 'Z'

        output = str(new_number) + output
        num = num // radix
    print('Число в ', radix, 'й системе счисления: ', output)
    return output


# print(new_radix(21**555, 36))
