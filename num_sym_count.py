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


number = 81**15 + 3**22 - 27
number_radix = 9

print(nson.new_radix(number, number_radix).count('8'))
