'''
Author: Jack Ford
KUID: 3067365
Date: 03/19/2022
Lab: Lab 05
Last modified: 03/27/2022
Purpose: Get a power and base from the user and output the result
	 of raising the base to the power.
'''

#recursive function with a base case that returns 1 if the power
#is 0 otherwise calls itself
def exponent(base, power):
	if power > 0:
		ans = exponent(base, power - 1) * base
		return ans

	return 1

def main():
	base = 0.0
	power = 0.0

#asks the user for a base until they give an integer
	while type(base) != int:
		try:
			base = int(input("Please enter a base: "))

		except:
			print('Input must be an integer')

#asks the user for a power until they give an integer greater than
#or equal to 0
	while type(power) != int or power < 0:
		if type(power) != int:
			try:
				power = int(input("Please enter a power: "))

			except:
				print('Input must be an integer')

		elif power < 0:
			print('Sorry, your exponent must be zero or larger.')
			power = int(input("Please enter a power: "))

	print(f'Answer: {exponent(base, power)}')

if __name__ == '__main__':
	main()
