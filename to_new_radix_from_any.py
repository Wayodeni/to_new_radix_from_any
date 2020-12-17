'''
This program translates numbers between different scales of notation.
From any scale of notaion.
'''




def new_radix_from_any (num, radix, new_radix):
    res = ''
    number_10 = 0
    new_number = ''
    number = list(str(num))
    power_of_radix = 0

    for i in range(len(number) - 1, -1, -1):
        if number[i] == 'A' : number[i] = 10
        if number[i] == 'B' : number[i] = 11
        if number[i] == 'C' : number[i] = 12
        if number[i] == 'D' : number[i] = 13
        if number[i] == 'E' : number[i] = 14
        if number[i] == 'F' : number[i] = 15
        if number[i] == 'G' : number[i] = 16
        if number[i] == 'H' : number[i] = 17
        if number[i] == 'I' : number[i] = 18
        if number[i] == 'J' : number[i] = 19
        if number[i] == 'K' : number[i] = 20
        if number[i] == 'L' : number[i] = 21
        if number[i] == 'M' : number[i] = 22
        if number[i] == 'N' : number[i] = 23
        if number[i] == 'O' : number[i] = 24
        if number[i] == 'P' : number[i] = 25
        if number[i] == 'Q' : number[i] = 26
        if number[i] == 'R' : number[i] = 27
        if number[i] == 'S' : number[i] = 28
        if number[i] == 'T' : number[i] = 29
        if number[i] == 'U' : number[i] = 30
        if number[i] == 'V' : number[i] = 31
        if number[i] == 'W' : number[i] = 32
        if number[i] == 'X' : number[i] = 33
        if number[i] == 'Y' : number[i] = 34
        if number[i] == 'Z' : number[i] = 35

        number_10 = number_10 + (int(number[i]) * radix**power_of_radix)
        power_of_radix += 1

    if new_radix != 10 and new_radix != 1:
        while number_10:
            new_number = int(number_10 % new_radix)
            if new_radix >= 16:
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

            res = str(new_number) + res
            number_10 = number_10 // new_radix

        return res

    elif new_radix == 10:
        return number_10
    elif new_radix == 1:
        return '|' * number_10




print(new_radix_from_any('1A3F', 16, 36))
