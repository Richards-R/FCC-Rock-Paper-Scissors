# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], played_patterns={}):
    #if first play, make previous play "R" 
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    prediction = 'P'

    #once opponent history reaches five plays, start grouping consecutive plays into groups of five, incrementing after each play
    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        #print("opphist_last_five", last_five)
        played_patterns[last_five] = played_patterns.get(last_five, 0) + 1
        #print("played_patterns.key_values", played_patterns[last_five])
        #print("played_patterns_dict", played_patterns)
        
        #make variable to test what oppontents next play could be to compare with already played turns
        potential_play_patterns = [
            # "".join([*opponent_history[-4:], v]) 
            # for v in ['R', 'P', 'S']
            last_five[-4:] + 'R',
            last_five[-4:] + 'P',
            last_five[-4:] + 'S',
        ]
        #print("ppp", potential_play_patterns)

        #check wether any of the potential plays have already been played...
        #*ppptmapp = potential_play_patterns_that_match_already_played_patterns
        ppptmapp = {
            key: played_patterns[key]
            for key in potential_play_patterns if key in played_patterns
        }
        #print("ppptmapp", ppptmapp)

        #...and if so, find the most played potential play...
        if ppptmapp:
            #get the ppptmapp with highest number of play repetitions
            prediction = max(ppptmapp, key=ppptmapp.get)[-1:]
            #print(prediction)
    
    #...and play the next turn accordingly
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    #print("return", ideal_response[prediction])
    return ideal_response[prediction]
