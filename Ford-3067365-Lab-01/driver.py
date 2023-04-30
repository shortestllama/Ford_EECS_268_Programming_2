'''
Author: Jack Ford
KUID: 3067365
Date: 1/24/2022
Lab: Lab 01
Last modified: 1/26/2022
Purpose: Obtain the file to run, then create and run an Executive object.
'''

from executive import Executive

def main():
	file_name = input("Enter the name of the input file: ")
	my_exec = Executive(file_name)
	my_exec.run()

if __name__ == '__main__':
	main()

