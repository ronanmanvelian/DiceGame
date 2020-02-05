import numpy

probability_of_sum_a = 0
probability_of_sum_b = 0
d = 0


def intro_message():
    print()
    print("Welcome to the Dice Game! Your goal is to predict a sum")
    print("that is most likely to be rolled from a certain number of dice.")
    print()
    print("You can either play now or run some simulations to get a feel")
    print("for which sums are most likely to occur.")
    print()
    print("If you want to play now, enter P. If you want to first run some")
    print("simulations, enter S.")
    print()

    select_mode()


def select_mode():
    valid_response = False

    while not valid_response:
        user_choice = input("Please enter your choice: ")
        if user_choice == "S" or user_choice == "s":
            print()
            valid_response = True
            run_simulations()
        elif user_choice == "P" or user_choice == "p":
            print()
            valid_response = True
            play_game()
        elif user_choice == "Q" or user_choice == "q":
            print()
            print("Thanks for playing!")
            print()
            valid_response = True
        else:
            print("Invalid entry, please try again.")
            print()


def roll_dice(dice_count, sides_count):
    largest_possible_roll = dice_count * sides_count
    sum_rolled = numpy.random.randint(dice_count, largest_possible_roll + 1)
    p_pressed = False

    while not p_pressed:
        prompt = input("Enter R to roll the " + str(dice_count) + " dice: ")
        print()
        if prompt == "R" or prompt == "r":
            print("A sum of " + str(sum_rolled) + " was rolled.")
            print()
            return sum_rolled
        else:
            print("Invalid entry, please try again.")
            print()


def play_again():
    valid_response = False

    while not valid_response:
        choice = input("Enter P to play again, S to run simulations, or Q to quit: ")
        if choice == "P" or choice == "p":
            valid_response = True
            print()
            play_game()
        elif choice == "S" or choice == "s":
            valid_response = True
            print()
            run_simulations()
        elif choice == "Q" or choice == "q":
            print()
            print("Thanks for playing!")
            print()
            valid_response = True
        else:
            print("Invalid entry, please try again.")


def probability_comparison(sum_target_a, sum_target_b, num_of_dice):
    if abs(probability_of_sum_a - probability_of_sum_b) <= 0.001:
        print(str(sum_target_a) + " and " + str(sum_target_b) + " are equally likely to be the sums of a roll")
        print("of " + str(num_of_dice) + " dice.")
    else:
        if probability_of_sum_a > probability_of_sum_b:
            print("Therefore, the probability of obtaining a sum of " + str(sum_target_a) + " is")
            print("greater than the probability of obtaining a sum of " + str(sum_target_b) + ".")
        else:
            print("Therefore, the probability of obtaining a sum of " + str(sum_target_b) + " is")
            print("greater than the probability of obtaining a sum of " + str(sum_target_a) + ".")

    print()


def run_simulations():
    global probability_of_sum_a
    global probability_of_sum_b
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

    probability_of_sum_a = sum_a_count / n
    probability_of_sum_b = sum_b_count / n

    print("Your first target sum, " + str(a) + " was rolled " + str(sum_a_count) + " times.")
    print("Your second target sum, " + str(b) + " was rolled " + str(sum_b_count) + " times.")
    print()
    print("Based on these results, out of " + str(n) + " simulations, the")
    print("probability of obtaining a sum of " + str(a) + " is " + str(probability_of_sum_a) + ", and")
    print("The probability of obtaining a sum of " + str(b) + " is " + str(probability_of_sum_b) + ".")
    print()

    probability_comparison(a, b, d)

    print("Would you like to play the game (P), run more simulations (S), or quit (Q)?")
    print()

    select_mode()


def play_game():
    possible_num_of_dice = [3, 4, 5, 6, 7, 8]
    dice_num_selection = numpy.random.randint(0, len(possible_num_of_dice))
    num_of_dice = possible_num_of_dice[dice_num_selection]

    possible_sides_of_dice = [6, 8, 10, 12, 14, 16]
    dice_sides_selection = numpy.random.randint(0, len(possible_sides_of_dice))
    sides_of_dice = possible_sides_of_dice[dice_sides_selection]

    opponents = ["Mark", "Alice", "Ronan", "Sydney", "John", "Brianna", "Bill", "Taylor", "Joe", "Ashley"]
    opponent_selection = numpy.random.randint(0, len(opponents))
    opponent = opponents[opponent_selection]

    opponent_traits = ["is feeling confident today", "looks as if sleep wasn't their priority last night",
                       "seems to be having a bad hair day", "gives you a little smirk", "came prepared",
                       "is eating a rich chocolate ice cream", "seems to be listening to music",
                       "was your high school nemesis", "stares you down", "yawns loudly"]
    opponent_trait_selection = numpy.random.randint(0, len(opponent_traits))
    opponent_trait = opponent_traits[opponent_trait_selection]

    print("Your opponent, " + opponent + ", " + opponent_trait + ".")
    print()

    print(str(num_of_dice) + " dice will be rolled.")
    print("Each die has " + str(sides_of_dice) + " sides.")

    print()
    sum_choice = int(input("Think Carefully! Choose a sum: "))
    print()

    largest_possible_sum = num_of_dice * sides_of_dice
    third_of_largest_possible_sum = largest_possible_sum // 3

    champ_sum = numpy.random.randint((largest_possible_sum // 2), ((largest_possible_sum // 2) + num_of_dice + 1))
    star_player_sum = numpy.random.randint(largest_possible_sum // 2, ((largest_possible_sum + num_of_dice) // 2) + 2)
    good_player_sum = numpy.random.randint(third_of_largest_possible_sum, (third_of_largest_possible_sum * 2) + 1)
    average_player_sum = numpy.random.randint(num_of_dice, largest_possible_sum + 1)

    if opponent_trait == "came prepared":
        opponent_sum_choice = champ_sum
    elif opponent_trait == "gives you a little smirk":
        opponent_sum_choice = star_player_sum
    elif opponent_trait == "is feeling confident today":
        opponent_sum_choice = star_player_sum
    elif opponent_trait == "was your high school nemesis":
        opponent_sum_choice = good_player_sum
    elif opponent_trait == "stares you down":
        opponent_sum_choice = good_player_sum
    else:
        opponent_sum_choice = average_player_sum

    print(opponent + " chose a sum of " + str(opponent_sum_choice) + ".")
    print()

    dice_sum = roll_dice(num_of_dice, sides_of_dice)

    if abs(sum_choice - dice_sum) < abs(opponent_sum_choice - dice_sum):
        print("You won the game!")
        print()
    elif abs(sum_choice - dice_sum) > abs(opponent_sum_choice - dice_sum):
        print(opponent + " won the game...")
        print()
    else:
        print("It's a tie!")
        print()

    play_again()


def main():
    intro_message()


if __name__ == "__main__":
    main()
