# Fermat's Last Theorem Near Miss Finder

## Description

This Python program is designed to find "near misses" for Fermat's Last Theorem. Fermat's Last Theorem states that no three positive integers \( a, b, c \) can satisfy the equation \( a^n + b^n = c^n \) for any integer value of \( n \) greater than 2. This program aims to find values that almost satisfy the equation.

## Getting Started

### Dependencies

- Python 3.x

### How to clone

To clone the repository, run the following command:

```bash
git clone <your-repository-url>
```

### Installing and Running

1. Clone the repository or download the `fermat_near_miss.py` file.
2. Open a terminal and navigate to the folder where `fermat_near_miss.py` is located.
3. Run the command `python fermat_near_miss.py`.
4. Follow the on-screen instructions to provide input values for \( n \) and \( k \).

## Usage

The program will prompt the user for two inputs:

1. \( n \) - The exponent value, which should be greater than 2 and less than 12.
2. \( k \) - The upper limit for \( x \) and \( y \), which should be greater than 9.

After receiving these inputs, the program will search for near-miss values of \( x, y, \) and \( z \) such that \( x^n + y^n \approx z^n \).

## Output

The program will display new optimal combinations as it finds them, including:

- \( x \), \( y \), and \( z \) values
- The absolute miss
- The relative miss as a percentage

The final output will show the optimal combination with the smallest relative miss.
