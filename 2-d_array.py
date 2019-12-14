#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program uses a 2-D array


import random


def sum_of_numbers(passed_in_2D_list, count):
    # this function adds up all the elements in  a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element / count

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []
    count = 0

    # input
    rows = int(input("How many rows would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 10)
            count += 1
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    sum = sum_of_numbers(a_2d_list, count)
    print("The Average is of all the numbers is: {0} ".format(sum))


if __name__ == "__main__":
    main()
