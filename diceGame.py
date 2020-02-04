import numpy

probabilityOfSumA = 0
probabilityOfSumB = 0
d = 0

def intro_message():
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

    select_mode()


def select_mode():
    valid_response = False
    while not valid_response:
        user_choice = input("Please enter your choice: ")
        if user_choice == "S" or user_choice == "s":
            valid_response = True
            print()
            run_simulations()
        elif user_choice == "P" or user_choice == "p":
            valid_response = True
            print()
            play_game()
        else:
            print("Invalid entry, please try again.")
            print()


def probability_comparison(sum_target_a, sum_target_b, num_of_dice):
    if abs(probabilityOfSumA - probabilityOfSumB) <= 0.001:
        print(str(sum_target_a) + " and " + str(sum_target_b) + " are equally likely to be the sums of a roll")
        print("of " + str(num_of_dice) + " dice.")
    else:
        if probabilityOfSumA > probabilityOfSumB:
            print("Therefore, the probability of obtaining a sum of " + str(sum_target_a) + " is")
            print("greater than the probability of obtaining a sum of " + str(sum_target_b) + ".")
        else:
            print("Therefore, the probability of obtaining a sum of " + str(sum_target_b) + " is")
            print("greater than the probability of obtaining a sum of " + str(sum_target_a) + ".")

    print()


def run_simulations():
    global probabilityOfSumA
    global probabilityOfSumB
    global d
    sum_a_count = 0
    sum_b_count = 0
    simulation_count = 0
    n = 1000000
    dice_sum = 0

    d = int(input("Enter the number of dice you will roll: "))
    a = int(input("Enter a target sum: "))
    b = int(input("Enter another target sum: "))

    print()
    print("Please wait, this may take a while...")
    print()

    while simulation_count < n:
        for roll in range(0, d):
            roll_value = numpy.random.randint(1, 7)
            dice_sum += roll_value
        if dice_sum == a:
            sum_a_count += 1
        if dice_sum == b:
            sum_b_count += 1
        dice_sum = 0
        simulation_count += 1

    probabilityOfSumA = sum_a_count / n
    probabilityOfSumB = sum_b_count / n

    print("Your first target sum, " + str(a) + " was rolled " + str(sum_a_count) + " times.")
    print("Your second target sum, " + str(b) + " was rolled " + str(sum_b_count) + " times.")
    print()
    print("Based on these results, out of " + str(n) + " simulations, the")
    print("probability of obtaining a sum of " + str(a) + " is " + str(probabilityOfSumA) + ", and")
    print("The probability of obtaining a sum of " + str(b) + " is " + str(probabilityOfSumB) + ".")
    print()

    probability_comparison(a, b, d)

    print("Would you like to play the game (P), or do you want to run more simulations (S)?")
    print()

    select_mode()


def play_game():
    possible_num_of_dice = [3, 4, 5, 6, 7, 8]
    dice_num_selection = numpy.random.randint(0, len(possible_num_of_dice) - 1)
    num_of_dice = possible_num_of_dice[dice_num_selection]

    possible_sides_of_dice = [6, 8, 10, 12, 14, 16]
    dice_sides_selection = numpy.random.randint(0, len(possible_sides_of_dice) - 1)
    sides_of_dice = possible_sides_of_dice[dice_sides_selection]

    opponents = ["Mark", "Alice", "Ronan", "Sydney", "John", "Brianna", "Bill", "Taylor", "Joe", "Ashley"]
    opponent_selection = numpy.random.randint(0, len(opponents) - 1)
    opponent = opponents[opponent_selection]

    opponent_traits = ["is feeling confident today", "looks as if sleep wasn't their priority last night",
                      "seems to be having a bad hair day", "gives you a little smirk", "came prepared",
                      "is eating a rich chocolate ice cream", "had a bit too much to drink",
                      "was your high school nemesis", "stares you down"]
    opponent_trait_selection = numpy.random.randint(0, 9)
    opponent_trait = opponent_traits[opponent_trait_selection]

    print("Your opponent, " + opponent + ", " + opponent_trait + ".")
    print()

    print(str(possible_num_of_dice[num_of_dice]) + " dice will be rolled.")
    print("Each die has " + str(sides_of_dice) + " sides.")

    print()
    sum_choice = input("Think Carefully! Choose a sum: ")
    print()

    print(opponent + " chose a sum of ")


def main():
    intro_message()


if __name__ == "__main__":
    main()
