num_float = 2.1

if num_float > 0:
    print("положительное число")
elif num_float == 0:
    print('ноль')
else:
    print("отрицательное число")


permit_print = True
num = -5
if num > 0 and permit_print:
    print('num - положительное')
elif not permit_print:
    print("печать запрещена")



