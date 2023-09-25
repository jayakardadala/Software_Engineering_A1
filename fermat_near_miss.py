"""
==============================================================================
                       Fermat's Last Theorem Near Miss Finder
==============================================================================
- Assignment: Software Engineering, Assignment 1 - Looking for Fermat’s Last Theorem Near Misses
- Filename: fermat_near_miss.py

------------------------------------------------------------------------------
                                  Metadata
------------------------------------------------------------------------------
- Author1: Vishnu Vardhan Reddy Ravu
- Email: VishnuVardhanReddy123@lewisu.edu
- Author2: Jayakar Dadala
- Email: jayakardadala@lewisu.edu
- Course: Software Engineering- 001
- Submission Date: September 19, 2023

------------------------------------------------------------------------------
                               Program Details
------------------------------------------------------------------------------
- Description: 
    This program allows the user to search for near misses to Fermat's Last Theorem.
  
- Dependencies: 
    None

- Output Files: 
    None

------------------------------------------------------------------------------
                                 References
------------------------------------------------------------------------------
- Fermat's Last Theorem Wikipedia: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem
- Additional Info: https://people.math.harvard.edu/~elkies/ferm.html

==============================================================================
"""
import math  # Importing math library for power and root calculations

# Constants for minimum values of n and k
MIN_N = 3
MIN_K = 10


def get_user_input():
    """
    This function gets the user input for n and k.
    It validates the input to ensure they are integers within the specified range.
    """
    while True:
        try:
            n = int(input(f"Enter the power n (should be > {MIN_N - 1} and < 12): "))
            if n < MIN_N or n >= 12:
                print(f"Invalid input! n should be > {MIN_N - 1} and < 12.")
                continue

            k = int(input(f"Enter the upper limit k for x and y (should be > {MIN_K - 1}): "))
            if k < MIN_K:
                print(f"Invalid input! k should be > {MIN_K - 1}.")
                continue

            return n, k
        except ValueError:
            print("Invalid input! Please enter integers.")


def find_near_misses(n, k):
    """
    This function finds and prints the near misses for Fermat's Last Theorem for given n and k.
    It returns the best x, y, z, and the smallest relative miss.
    """
    smallest_relative_miss = float('inf')  # Initialize smallest relative miss to infinity
    best_x, best_y, best_z = 0, 0, 0  # Initialize best x, y, z to 0

    # Loop through all possible x and y combinations
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            target = math.pow(x, n) + math.pow(y, n)  # Calculate x^n + y^n
            
            z = int(math.pow(target, 1/n))  # Find z that brackets target
            lower_bound = math.pow(z, n)  # Calculate z^n
            upper_bound = math.pow(z + 1, n)  # Calculate (z+1)^n

            # Find the closest bound and calculate the absolute miss
            if abs(target - lower_bound) < abs(upper_bound - target):
                closest_bound = lower_bound
                z_value = z
            else:
                closest_bound = upper_bound
                z_value = z + 1

            absolute_miss = abs(target - closest_bound)  # Calculate the absolute miss
            relative_miss = absolute_miss / target  # Calculate the relative miss

            # Update smallest relative miss if this one is smaller
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, z_value

                print(f"New smallest relative miss found:")
                print(f"x = {best_x}, y = {best_y}, z = {best_z}")
                print(f"Absolute miss: {absolute_miss}")
                print(f"Relative miss: {smallest_relative_miss * 100:.10f}%")
                print("------")

    return best_x, best_y, best_z, smallest_relative_miss


n, k = get_user_input()

print()

best_x, best_y, best_z, smallest_relative_miss = find_near_misses(n, k)

print(f"Final smallest relative miss: {smallest_relative_miss * 100:.10f}%")
print(f"Best x = {best_x}, Best y = {best_y}, Best z = {best_z}")

print()
print()
input("Press enter to exit...")
