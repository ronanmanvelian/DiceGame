import numpy

probabilityOfSumA = 0
probabilityOfSumB = 0
d = 0

def introMessage():

    print()
    print("Welcome to the Dice Gamble Game! Your goal is to predict a sum")
    print("that is most likely to be rolled from a certain number of dice.")
    print()
    print("You can either play now or run some simulations to get a feel")
    print("for which sums are most likely to occur.")
    print()
    print("If you want to play now, enter P. If you first want to run some")
    print("simulations, enter S.")
    print()

    selectMode()

def selectMode():

    validResponse = False
    while validResponse == False:
        userChoice = input("Please enter your choice: ")
        if userChoice == "S" or userChoice == "s":
            validResponse = True
            print()
            runSimulations()
        elif userChoice == "P" or userChoice == "p":
            validResponse = True
            print()
            playGame()
        else:
            print("Invalid entry, please try again.")
            print()

def probabilityComparison(sumTargetA, sumTargetB, numOfDice):
     
    if abs(probabilityOfSumA - probabilityOfSumB) <= (1/ 6**d): 
        print(str(sumTargetA) + " and " + str(sumTargetB) + " are equally likely to be the sums of a roll")
        print("of " + str(numOfDice) + " dice.")
    else:    
        if probabilityOfSumA > probabilityOfSumB:
            print("Therefore, the probability of obtaining a sum of " + str(sumTargetA) + " is")
            print("greater than the probability of obtaining a sum of " + str(sumTargetB) + ".")
        else:
            print("Therefore, the probability of obtaining a sum of " + str(sumTargetB) + " is")
            print("greater than the probability of obtaining a sum of " + str(sumTargetA) + ".")

    print()    
           
def runSimulations():

    global probabilityOfSumA
    global probabilityOfSumB
    global d
    sumACount = 0
    sumBCount = 0
    simulationCount = 0         
    n = 1000000                 
    diceSum = 0                 

    print()

    d = int(input("Enter the number of dice you will roll: ")) 
    a = int(input("Enter a target sum: ")) 
    b = int(input("Enter another target sum: "))

    print()
    print("Please wait, this may take a while...")
    print()

    while simulationCount < n:
        for roll in range(0, d):
            rollValue = numpy.random.randint(1, 7)
            diceSum += rollValue
        if diceSum == a:
            sumACount += 1
        if diceSum == b:
            sumBCount += 1
        diceSum = 0
        simulationCount += 1

    probabilityOfSumA = sumACount / n
    probabilityOfSumB = sumBCount / n

    print("Your first target sum, " + str(a) + " was rolled " + str(sumACount) + " times.")
    print("Your second target sum, " + str(b) + " was rolled " + str(sumBCount) + " times.")
    print()
    print("Based on these results, out of " + str(n) + " simulations, the")
    print("probability of obtaining a sum of " + str(a) + " is " + str(probabilityOfSumA) + ", and")
    print("The probability of obtaining a sum of " + str(b) + " is " + str(probabilityOfSumB) + ".")
    print()

    probabilityComparison(a, b, d)

    print("Would you like to play the game (P), or do you want to run more simulations (S)?")
    print()

    selectMode()

def playGame():

    possibleNumOfDice = [3, 4, 5, 6, 7, 8]
    diceNumSelection = numpy.random.randint(0, len(possibleNumOfDice) - 1)
    numOfDice = possibleNumOfDice[diceNumSelection]

    opponents = ["Mark", "Alice", "Bill", "Sydney", "John", "Brianna", "Ronan", "Taylor", "Joe", "Ashley"]
    opponentSelection = numpy.random.randint(0, len(opponents) - 1)
    opponent = opponents[opponentSelection]

    opponentTraits = ["is feeling confident today", "looks as if sleep wasn't their priority last night",
                     "seems to be having a bad hair day", "gives you a little smirk", "came prepared",
                     "is eating a rich chocolate ice cream", "had a bit too much to drink",
                     "was your high school nemesis", "stares you down"]
    opponentTraitSelection = numpy.random.randint(0, 9)
    opponentTrait = opponentTraits[opponentTraitSelection]
    
    print("Your opponent, " + opponent + ", " + opponentTrait + ".")

def main():

    introMessage()
    runSimulations()

if __name__ == "__main__":
    main()
