'''
Author: Jack Ford
KUID: 3067365
Date: 04/10/2022
Lab: Lab 07
Last modified: 04/11/2022
Purpose: Time various methods from the data structures we've
         made so far, save those times, and plot them to see
         if they match the theoretical expectations.
'''

import time
from stack import Stack
from linkedlist import LinkedList
from q import Queue

#method that converts time from nanoseconds to seconds
def nanosec_to_sec(ns):
        BILLION = 1000000000
        return ns/BILLION

#method that times all of the functions and writes the times to the data file,
#delimited by a comma
def timer(dat_struc, op, file, ind=0):
        #writes the time for the popping of a single item from stack to the file
        if op == 1:
                start_time = time.process_time_ns()

                dat_struc.pop()

                end_time = time.process_time_ns()
                file.write(str(nanosec_to_sec(end_time-start_time)) + ',')

        #writes the time for the popping of a all items from stack to the file
        if op == 2:
                start_time = time.process_time_ns()

                while not dat_struc.is_empty():
                        dat_struc.pop()

                end_time = time.process_time_ns()
                file.write(str(nanosec_to_sec(end_time-start_time)) + ',')

        #writes the time for dequeue's enqueue to the file
        if op == 3:
                start_time = time.process_time_ns()

                for i in range(1000 * (ind + 1)):
                        dat_struc.enqueue(i)

                end_time = time.process_time_ns()

                while not dat_struc.is_empty():
                        dat_struc.dequeue()

                file.write(str(nanosec_to_sec(end_time-start_time)) + ',')

        #writes the time for get_entry at index 0 to the file
        if op == 4:
                start_time = time.process_time_ns()

                dat_struc.get_entry(0)

                end_time = time.process_time_ns()
                file.write(str(nanosec_to_sec(end_time-start_time)) + ',')

        #writes the time for get_entry at the last index to the file
        if op == 5:
                start_time = time.process_time_ns()

                dat_struc.get_entry(dat_struc.length() - 1)

                end_time = time.process_time_ns()
                file.write(str(nanosec_to_sec(end_time-start_time)) + ',')

        #writes the time for printing get_entry of all entries to the file
        if op == 6:
                start_time = time.process_time_ns()

                for i in range(dat_struc.length()):
                        print(dat_struc.get_entry(i))

                end_time = time.process_time_ns()
                file.write(str(nanosec_to_sec(end_time-start_time)) + ',')

#main method that creates the data structures, fills the data structures, and
#calls the timer method
def main():
        my_stack = Stack()
        my_queue = Queue()
        my_list = LinkedList()
        file = open('data.txt', 'w')

        #fill the stack 100 times with 1000 items each time, timing the
        #operations each time it's filled
        for i in range(100):
                for j in range(1000):
                        my_stack.push(j)

                timer(my_stack, 1, file)
                my_stack.push(0)
                timer(my_stack, 2, file)
                file.write('\n')

                for j in range(1000 * (i + 1)):
                        my_stack.push(j)

        #call the timer method for the queue 100 times
        for i in range(100):
                timer(my_queue, 3, file, i)

        file.write('\n')

        #fill the linked list 100 times with 1000 items each time, timing
        #the operations each time it's filled
        for i in range(100):
                for j in range(1000):
                        my_list.insert(j, j)

                timer(my_list, 4, file)
                timer(my_list, 5, file)
                timer(my_list, 6, file)
                file.write('\n')

        file.close()

if __name__ == '__main__':
        main()
