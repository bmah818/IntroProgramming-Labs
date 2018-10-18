def main():
    print("PYTHON GUESSING GAME")
    answer = "dog"
    while True:
        print("I'm thinking of an animal.")
        guess = input("What animal am I thinking of?")
        if guess == answer:
            break
        else:
            print("Try again. Wrong animal.")

main()
print("You win!")
