#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This calculate the average of user input

import random

# Defining the function that calculates the average
def calc_average(list):
    total_sum = 0
    divisor = len(list)
    for a_num in list:
        total_sum += a_num
    average = total_sum / divisor
    return average


def main():
    # Creating empty list
    nums = []
    while True:
        # Get user input
        user_input = input("Enter a mark: ")
        if user_input == "-1":
            break
        else:
            try:
                user_int = int(user_input)
                nums.append(user_int)
            except:
                print("Invalid input. Please enter a real number or -1")

    # Calling the function
    average = calc_average(nums)

    # Displaying the average
    print()
    print("The average is {}".format(average))


if __name__ == "__main__":
    main()
