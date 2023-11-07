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
    
    if turn_count == 10 and check_win_cross != True and check_win_circle != True:
        print("It's a draw!")
        return True
    
    return False

  

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
    if turn_count in [1, 3 ,5, 7, 9]:
        print("It's Circle turn.")
    else:
        print("It's Cross turn.")


def turn_define(turn_count):
    if turn_count in [1, 3 ,5, 7, 9]:
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
                choice_check
            elif choice == 1 and (type(playground[2][0]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 2 and (type(playground[2][1]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 3 and (type(playground[2][2]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 4 and (type(playground[1][0]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 5 and (type(playground[1][1]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 6 and (type(playground[1][2]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 7 and (type(playground[0][0]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 8 and (type(playground[0][1]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            elif choice == 9 and (type(playground[0][2]) == type("str")):
                print("This number has already been taken. Please choose another place:")
                show_playground(playground)
                choice_check
            else:
                choice_check = False
        
    return  choice


playground = [[7, 8, 9], 
              [4, 5, 6], 
              [1, 2, 3]]


start = True # Starts the main loop with the game
turn_count = 1 # Tracks number of turns
while start and turn_count < 11 and check_win_cross(playground) != True and check_win_circle(playground) != True and announce_draw(turn_count, check_win_circle(playground), check_win_cross(playground)) == False:
    
    print(f"It's turn number {turn_count}")
    whose_turn_is_it(turn_count)
    replace_symbol(make_your_choice(), playground, turn_define(turn_count))
    show_playground(playground)
    turn_count += 1 
