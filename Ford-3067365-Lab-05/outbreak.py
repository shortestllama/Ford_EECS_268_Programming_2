'''
Author: Jack Ford
KUID: 3067365
Date: 03/19/2022
Lab: Lab 05
Last modified: 03/27/2022
Purpose: Get a day from the user and return the number of
	 infected patients for that day
'''

#recursive function with three base cases otherwise calls itself
def outbreak(day):
	if day == 1:
		return 6

	elif day == 2:
		return 20

	elif day == 3:
		return 75

	else:
		return outbreak(day - 1) + outbreak(day - 2) + outbreak(day - 3)

#asks the user for a day and if the day is valid, returns the sick
#count, otherwise lets the user know
def main():
	print('OUTBREAK!')
	day = int(input('What day do you want a sick count for? '))

	try:
		print(f'Total people with the flu: {outbreak(day)}')

	except:
		print('Invalid day')

if __name__ == '__main__':
	main()
