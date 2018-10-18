def main():
    print("PYTHON GUESSING GAME")
    answer = "dog"
    while True:
        print("I'm thinking of an animal.")
        guess = input("What animal am I thinking of?")
        guess = guess.lower()
        guess = guess.strip()
        if guess == answer:
            print("You win!")
            break
        elif guess == "quit":
            break
        else:
            print("Try again. Wrong animal.")

main()
