'''
Author: Jack Ford
KUID: 3067365
Date: 02/15/2022
Lab: Lab 03
Last modified: 02/15/2022
Purpose: Obtain a file name from the user, create
	 a CPU object containing that file, then
	 call run on that CPU object.
'''

from cpu_scheduler import CPU

def main():
	file = input("Please enter a file name: ")
	my_cpu = CPU(file)
	my_cpu.run()

if __name__ == '__main__':
	main()
