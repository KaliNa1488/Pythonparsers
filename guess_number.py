number = 54
while True :
	your_number = int(input('Угадай целое число:'))
	if your_number == number :
		print('GG')
		input()
		break
	elif your_number > number and your_number < number + 10 :
		print('тепло')
		print('Попробуй ещё раз')
	elif your_number < number and your_number > number - 10 :
		print('тепло')
		print('Попробуй ещё раз')
	else:
		print('холодно')
		print('Попробуй ещё раз')