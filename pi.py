# CMPT 120
# Bryan Mah
# September 9
# Pi exercise using math module

import math

def main():
    print("This program approximates the value of pi by summing a fixed")
    print("number of terms in a series.")
    
    n = int(input("How many terms do you want to use? "))

    total = 0.0
    sgn = 1.0   
    for denom in range(1, 2*n, 2):
        total = total + sgn * 4.0/denom
        sgn = -sgn 

    print("Approximated value to pi is", total)
    print("Difference from math.pi is", math.pi - total)

main()
        
