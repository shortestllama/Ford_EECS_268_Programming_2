'''
Author: Jack Ford
KUID: 3067365
Date: 03/19/2022
Lab: Lab 05
Last modified: 03/27/2022
Purpose: Gets a mode and input from the user and returns
	 either the number in the sequence at the input
	 if mode i or if the input is in the sequence if
	 mode v
'''

#recursive function that has a base case for 1 and 0,
#otherwise calls itself
def fibonacci(i):
	if i == 0:
		return 0

	elif i == 1:
		return 1

	else:
		return fibonacci(i - 1) + fibonacci(i - 2)

def main():
#gets the mode and input from the user and stores them in
#variables if they're both valid
	entry = input("Enter mode and value: ")
	entry = entry.replace(" ", "")
	mode = entry[1:2:]
	try:
		value = int(entry[2::])

	except:
		raise RuntimeError('Entry must be an integer')

#if the mode is i and the input is valid, returns the number in
#the sequence at the input
	if mode == 'i':
		if value < 0:
			raise RuntimeError("Value is invalid.")

		else:
			print(fibonacci(value))

#if the mode is v and the input is valid, returns whether or not
#the input is in the sequence
	elif mode == 'v':
		i = 0
		fib = fibonacci(i)

		while value >= fib:
			i += 1

			if fib < value:
				fib = fibonacci(i)

			if fib == value:
				print(f'{value} is in the sequence')
				break

		if fib != value:
			print(f'{value} is not in the sequence')

#if the mode is not i or v, raises a runtime error
	else:
		raise RuntimeError('Invalid mode')

if __name__ == '__main__':
	main()
