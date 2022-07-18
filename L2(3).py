# Завдання 3
def sum_num(num: int):
    num = abs(num)
    s = str(num)
    while len(s) > 1:
        suma = 0
        for digit in s:
            suma += int(digit)
        s = str(suma)
    return int(s)


print(sum_num(38) == 2)
print(sum_num(40) == 4)
print(sum_num(48) == 3)
print(sum_num(2) == 2)
print(sum_num(-88) == 7)
