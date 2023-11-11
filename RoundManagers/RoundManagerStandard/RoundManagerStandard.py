class RoundManagerStandard:

    def __init__(self):
        self.number_of_rounds = 0
        self.number_of_turns_limit = 11
        self.how_many_rounds = self.how_many_rounds()
        self.turn_count = 1
        self.circle_wins = 0
        self.cross_wins = 0

    def check_win_cross(self, playground):
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

    def check_win_circle(self, playground):
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

    def announce_draw(self, turn_count, check_win_circle, check_win_cross):

        if turn_count == 10 and check_win_cross is not True and check_win_circle is not True:
            return True

        return False

    def how_many_rounds(self):  # Function that allows the user to specify the number of rounds they want to play.

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

    def whose_turn_is_it(self, turn_count):
        if turn_count in [1, 3, 5, 7, 9]:
            print("It's Circle turn.")
        else:
            print("It's Cross turn.")

    def turn_define(self, turn_count):
        if turn_count in [1, 3, 5, 7, 9]:
            turn = "Circle"
        else:
            turn = "Cross"

        return turn

    def round_result(self, playground):

        if self.check_win_cross(playground) is True:
            self.cross_wins += 1
            print(f"Cross Player won round {self.number_of_rounds + 1}!")

        if self.check_win_circle(playground) is True:
            self.circle_wins += 1
            print(f"Circle Player won round {self.number_of_rounds + 1}!")

        if self.announce_draw(self.turn_count, self.check_win_circle(playground),
                              self.check_win_cross(playground)) is True:
            self.cross_wins += 1
            self.circle_wins += 1
            print("It's a draw!")
