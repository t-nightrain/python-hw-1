# Завдання 1
def odd_or_even(num):
	try:
		n = int(num)
		if n != num:
			print('Функція працює лише з цілими числами')
		elif n == num and num % 2 == 0:
			print('Число ' + str(num) + ' є парним')
		elif n == num and num % 2 != 0:
			print('Число ' + str(num) + ' є непарним')
	except ValueError:
		print('Функція працює лише з цілими числами')


odd_or_even(12)
odd_or_even(17)
odd_or_even(-8)
odd_or_even(3.14)
odd_or_even('some text')
