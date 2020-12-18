import n_scale_of_notation as nson


# num = 6 * 343**5 + 5 * 49**7 - 50
# radix = 7
# res = ''
# while num:
#     res = str(num % radix) + res
#     num = num // radix
#
# print(res)
# print(res.count('6'))


number = 81**17 + 3**24 -45
number_radix = 9
numerals_to_count = '8'
print(nson.new_radix(number, number_radix).count(numerals_to_count))
