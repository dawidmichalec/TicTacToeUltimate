def check_win_cross(playground):
    if playground[0][0] == "X" and playground[0][1] == "X" and playground[0][2] == "X":
        return True
    elif playground[1][0] == "X" and playground[1][1] == "X" and playground[1][2] == "X":
        return True
    elif playground[2][0] == "X" and playground[2][1] == "X" and playground[2][2] == "X":
        return True
    elif playground[0][0] == "X" and playground[1][0] == "X" and playground[2][0] == "X":
        return True
    elif playground[0][1] == "X" and playground[1][1] == "X" and playground[2][1] == "X":
        return True
    elif playground[0][2] == "X" and playground[1][2] == "X" and playground[2][2] == "X":
        return True
    elif playground[0][0] == "X" and playground[1][1] == "X" and playground[2][2] == "X":
        return True
    elif playground[0][2] == "X" and playground[1][1] == "X" and playground[2][0] == "X":
        return True
    else:
        return False


def check_win_circle(playground):
    if playground[0][0] == "O" and playground[0][1] == "O" and playground[0][2] == "O":
        return True
    elif playground[1][0] == "O" and playground[1][1] == "O" and playground[1][2] == "O":
        return True
    elif playground[2][0] == "O" and playground[2][1] == "O" and playground[2][2] == "O":
        return True
    elif playground[0][0] == "O" and playground[1][0] == "O" and playground[2][0] == "O":
        return True
    elif playground[0][1] == "O" and playground[1][1] == "O" and playground[2][1] == "O":
        return True
    elif playground[0][2] == "O" and playground[1][2] == "O" and playground[2][2] == "O":
        return True
    elif playground[0][0] == "O" and playground[1][1] == "O" and playground[2][2] == "O":
        return True
    elif playground[0][2] == "O" and playground[1][1] == "O" and playground[2][0] == "O":
        return True
    else:
        return False


def announce_draw(turn_count, check_win_circle, check_win_cross):
    if turn_count == 10 and check_win_cross is not True and check_win_circle is not True:
        return True

    return False


def score(cross_wins, circle_wins):  # Displays score

    print(f"Current score\n\nCircle Player: {circle_wins}\nCross Player: {cross_wins}")


def is_match_over(how_many_rounds, cross_wins, circle_wins):
    if how_many_rounds == 1 and circle_wins == 1 and cross_wins == 1:
        print(f"Match ended with a draw!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 3 and circle_wins == 2 and cross_wins == 2:
        print(f"Match ended with a draw!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 6 and circle_wins == 3 and cross_wins == 3:
        print(f"Match ended with a draw!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 1 and cross_wins == 1:
        print(f"Cross Player won the match!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 1 and circle_wins == 1:
        print(f"Circle Player won the match!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 3 and cross_wins == 2:
        print(f"Cross Player won the match!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 3 and circle_wins == 2:
        print(f"Circle Player won the match!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 6 and cross_wins == 3:
        print(f"Cross Player won the match!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    elif how_many_rounds == 6 and circle_wins == 3:
        print(f"Circle Player won the match!\n\nFinal score:\n"
              f"Circle Player: {circle_wins}\nCross Player: {cross_wins}")
        return True
    else:
        return False


def how_many_rounds():  # Function that allows the user to specify the number of rounds they want to play.

    choice_check = True
    while choice_check:
        try:
            choice = int(input("Specify the number of rounds you want to play (type the right number):\n"
                               "1 - Up to 1 won round\n"
                               "2 - Up to 2 won rounds\n"
                               "3 - Up to 3 won rounds\n"))
        except ValueError:
            print("Enter a numeric value!")
        else:
            if choice > 3 or choice < 1:
                print("Number must be between 1 and 3! Please enter a valid value!")
                choice_check = True
            else:
                choice_check = False

    if choice == 1:
        print(f"You chose to play up to 1 won round. Good luck...")
        return choice
    elif choice == 2:
        print(f"You chose to play up to 2 won rounds. Good luck...")
        choice = 3
        return choice
    else:
        print(f"You chose to play up to 3 won rounds. Good luck...")
        choice = 6
        return choice


def show_playground(playground):
    # Function displays how the playground looks like

    for i in playground:
        print(i)


def replace_symbol(choice, playground, turn):
    match turn:
        case "Circle":
            match choice:
                case 1:
                    playground[2][0] = "O"
                    return playground
                case 2:
                    playground[2][1] = "O"
                    return playground
                case 3:
                    playground[2][2] = "O"
                    return playground
                case 4:
                    playground[1][0] = "O"
                    return playground
                case 5:
                    playground[1][1] = "O"
                    return playground
                case 6:
                    playground[1][2] = "O"
                    return playground
                case 7:
                    playground[0][0] = "O"
                    return playground
                case 8:
                    playground[0][1] = "O"
                    return playground
                case 9:
                    playground[0][2] = "O"
                    return playground
        case "Cross":
            match choice:
                case 1:
                    playground[2][0] = "X"
                    return playground
                case 2:
                    playground[2][1] = "X"
                    return playground
                case 3:
                    playground[2][2] = "X"
                    return playground
                case 4:
                    playground[1][0] = "X"
                    return playground
                case 5:
                    playground[1][1] = "X"
                    return playground
                case 6:
                    playground[1][2] = "X"
                    return playground
                case 7:
                    playground[0][0] = "X"
                    return playground
                case 8:
                    playground[0][1] = "X"
                    return playground
                case 9:
                    playground[0][2] = "X"
                    return playground


def whose_turn_is_it(turn_count):
    if turn_count in [1, 3, 5, 7, 9]:
        print("It's Circle turn.")
    else:
        print("It's Cross turn.")


def turn_define(turn_count):
    if turn_count in [1, 3, 5, 7, 9]:
        turn = "Circle"
    else:
        turn = "Cross"

    return turn


def make_your_choice():
    choice_check = True
    show_playground(playground)
    while choice_check:
        try:
            choice = int(input("Specify where you want to put your symbol:\n"))
        except ValueError:
            print("Enter a numeric value!")
        else:
            if choice > 9 or choice < 1:
                print("Number must be between 1 and 9! Please enter a valid value!")
                choice_check = True
            elif choice == 1 and isinstance(playground[2][0], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 2 and isinstance(playground[2][1], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 3 and isinstance(playground[2][2], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 4 and isinstance(playground[1][0], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 5 and isinstance(playground[1][1], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 6 and isinstance(playground[1][2], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 7 and isinstance(playground[0][0], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 8 and isinstance(playground[0][1], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            elif choice == 9 and isinstance(playground[0][2], str):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check = True
            else:
                choice_check = False

    return choice


number_of_rounds = 0
how_many_rounds = how_many_rounds()  # Determines up to how many wins the match will be played.
circle_wins = 0
cross_wins = 0
start = True  # Starts the main loop with the game
# Main game loop
while start and number_of_rounds < how_many_rounds and is_match_over(how_many_rounds, cross_wins, circle_wins) is False:
    playground = [[7, 8, 9],
                  [4, 5, 6],
                  [1, 2, 3]]
    turn_count = 1
    print(f"Round {(number_of_rounds + 1)}!")
    # Round loop
    while turn_count < 11 and check_win_cross(playground) is not True and check_win_circle(
            playground) is not True and announce_draw(turn_count, check_win_circle(playground),
                                                      check_win_cross(playground)) is False:
        print(f"It's turn number {turn_count}")
        whose_turn_is_it(turn_count)
        replace_symbol(make_your_choice(), playground, turn_define(turn_count))
        show_playground(playground)
        turn_count += 1

    if check_win_cross(playground) is True:
        cross_wins += 1
        print(f"Cross Player won round {number_of_rounds + 1}!")

    if check_win_circle(playground) is True:
        circle_wins += 1
        print(f"Circle Player won round {number_of_rounds + 1}!")

    if announce_draw(turn_count, check_win_circle(playground), check_win_cross(playground)) is True:
        cross_wins += 1
        circle_wins += 1
        print("It's a draw!")

    is_match_over(how_many_rounds, cross_wins, circle_wins)
    score(cross_wins, circle_wins)
    number_of_rounds += 1