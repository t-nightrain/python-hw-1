# Завдання 2
def transform_str(s):
    try:
        s = str(s)
        if len(s) > 5:
            s = s[0:5] + '...'
        if s[0] == 'U' or s[0] == 'u':
            s = s.upper()
        elif s[0] == 'L' or s[0] == 'l':
            s = s.lower()
        print(s)
    except ValueError:
        print('Error')


transform_str('Testing string')
transform_str('Lux')
transform_str('up')
transform_str('Luxery')
transform_str(5)
