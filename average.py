#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program finds the average of 10 random numbers

import random


def main():
    # this function uses a list

    list_of_numbers = []
    total = 0

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)  # a number between 1-100
        total = total + random_number
        list_of_numbers.append(random_number)
        print("The random number is : {0}".format(random_number))
        loop_counter += 1

    average = round(total / (len(list_of_numbers)))
    print("\nThe average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
