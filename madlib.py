# CMPT 120L 113
# Madlib Program
# Author: Bryan Mah
# Created 13 Sep 2018

def promptForWords():
    global noun, verb, adjective, place
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

def makeAndPrintSentence():
    print("The "+ adjective + " " + noun + " " + verb + " to the" + place + " today.")
    
def main():
    promptForWords()
    makeAndPrintSentence()

main()
