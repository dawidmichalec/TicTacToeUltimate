class MatchManagerStandard:

    def __init__(self):
        pass

    def is_match_over(self, how_many_rounds, circle_wins, cross_wins):

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
