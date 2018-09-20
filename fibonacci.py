# CMPT 120
# Bryan Mah
# September 9
# Fibonacci number exercise

def main():
    print("This calculates the nth Fibonacci number.")
    n = int(input("Enter the value of n: "))
    prev, beforePrev = 1, 1
    for i in range(n-2):
        prev, beforePrev = prev+beforePrev, prev
    print("The nth Fibonacci number is", prev)

main()
