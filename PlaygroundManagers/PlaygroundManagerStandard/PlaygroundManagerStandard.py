class Playground:

    def __init__(self):
        self.playground = [[7, 8, 9],
                           [4, 5, 6],
                           [1, 2, 3]]

    def show_playground(self):

        # Function displays how the playground looks like

        for i in self.playground:
            print(i)

    def reset_playground(self):

        self.playground = [[7, 8, 9],
                           [4, 5, 6],
                           [1, 2, 3]]

    def make_your_choice(self):

        choice_check = True
        self.show_playground()
        while choice_check:
            try:
                choice = int(input("Specify where you want to put your symbol:\n"))
            except ValueError:
                print("Enter a numeric value!")
            else:
                if choice > 9 or choice < 1:
                    print("Number must be between 1 and 9! Please enter a valid value!")
                    choice_check = True
                elif choice == 1 and isinstance(self.playground[2][0], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 2 and isinstance(self.playground[2][1], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 3 and isinstance(self.playground[2][2], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 4 and isinstance(self.playground[1][0], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 5 and isinstance(self.playground[1][1], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 6 and isinstance(self.playground[1][2], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 7 and isinstance(self.playground[0][0], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 8 and isinstance(self.playground[0][1], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                elif choice == 9 and isinstance(self.playground[0][2], str):
                    print("This number has already been taken. Please choose another place:")
                    self.show_playground()
                    choice_check = True
                else:
                    choice_check = False

        return choice

    def replace_symbol(self, choice, turn):

        match turn:
            case "Circle":
                match choice:
                    case 1:
                        self.playground[2][0] = "O"
                        return self.playground
                    case 2:
                        self.playground[2][1] = "O"
                        return self.playground
                    case 3:
                        self.playground[2][2] = "O"
                        return self.playground
                    case 4:
                        self.playground[1][0] = "O"
                        return self.playground
                    case 5:
                        self.playground[1][1] = "O"
                        return self.playground
                    case 6:
                        self.playground[1][2] = "O"
                        return self.playground
                    case 7:
                        self.playground[0][0] = "O"
                        return self.playground
                    case 8:
                        self.playground[0][1] = "O"
                        return self.playground
                    case 9:
                        self.playground[0][2] = "O"
                        return self.playground
            case "Cross":
                match choice:
                    case 1:
                        self.playground[2][0] = "X"
                        return self.playground
                    case 2:
                        self.playground[2][1] = "X"
                        return self.playground
                    case 3:
                        self.playground[2][2] = "X"
                        return self.playground
                    case 4:
                        self.playground[1][0] = "X"
                        return self.playground
                    case 5:
                        self.playground[1][1] = "X"
                        return self.playground
                    case 6:
                        self.playground[1][2] = "X"
                        return self.playground
                    case 7:
                        self.playground[0][0] = "X"
                        return self.playground
                    case 8:
                        self.playground[0][1] = "X"
                        return self.playground
                    case 9:
                        self.playground[0][2] = "X"
                        return self.playground
            