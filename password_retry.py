password = 'a123456'
x = 3
while x > 0:
	answer = input('Please input the password:')
	if answer == password:
		print('You login the system successfully!!')
		break
	else:
		x = x -1
		print('Wrong password!, you still have ', x, 'x time!!')
		if x == 0:
			print('No chances fucker!!!!')