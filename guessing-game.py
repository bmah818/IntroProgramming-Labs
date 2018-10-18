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
            ask = input("Do you like this animal? Enter 'y' or 'n': ")
            if ask == "y":
                print("I like this animal too!.")
                break
            if ask == "n":
                print("I also don't like this animal.")
                break
        elif guess[0] == "q":
            break
        else:
            print("Try again. Wrong animal.")

main()
