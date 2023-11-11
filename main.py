from Scoreboard.Scoreboard import Scoreboard
from MatchManagers.MatchManagerStandard.MatchManagerStandard import MatchManagerStandard as Mms
from PlaygroundManagers.PlaygroundManagerStandard.PlaygroundManagerStandard import Playground
from RoundManagers.RoundManagerStandard.RoundManagerStandard import RoundManagerStandard as Rms


start = True
rms = Rms()
mms = Mms()
scoreboard = Scoreboard()
p = Playground()

while start and rms.number_of_rounds < rms.how_many_rounds and mms.is_match_over(rms.how_many_rounds,
                                                                                 rms.circle_wins,
                                                                                 rms.cross_wins) is False:

    p.reset_playground()
    rms.turn_count = 1
    print(f"Round {(rms.number_of_rounds + 1)}!")
    # Round loop
    while rms.turn_count < rms.number_of_turns_limit and rms.check_win_cross(
            p.playground) is not True and rms.check_win_circle(p.playground) is not True and rms.announce_draw(
        rms.turn_count, rms.check_win_circle(p.playground), rms.check_win_cross(p.playground)) is False:
        print(f"It's turn number {rms.turn_count}")
        rms.whose_turn_is_it(rms.turn_count)
        p.replace_symbol(p.make_your_choice(), rms.turn_define(rms.turn_count))
        p.show_playground()
        rms.turn_count += 1

    rms.round_result(p.playground)
    mms.is_match_over(rms.how_many_rounds, rms.circle_wins, rms.cross_wins)
    scoreboard.score(rms.circle_wins, rms.cross_wins)
    rms.number_of_rounds += 1
