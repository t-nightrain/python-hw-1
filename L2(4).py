# Завдання 4
def common_str(str1, str2):
    s1 = set(str1.replace(' ', ''))
    s2 = set(str2.replace(' ', ''))
    common = s1.intersection(s2)
    return ''.join(common)


print(common_str('loli', 'luck') == 'l')
print(common_str('good day', 'good morning') == 'god')
