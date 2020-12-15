## DAY 15
puzzle = [17,1,3,16,19,0]
#puzzle = [0,3,6]
turns = [2020,30000000]
number_to_turns = {num:[i, i] for i, num in enumerate(puzzle)}
#print(number_to_turns)
current_idx, prev_num = len(puzzle), puzzle[-1]

for turn in turns:
    while current_idx < turn:
        if number_to_turns[prev_num][0] == current_idx - 1:
            prev_num = 0
        else:
            last = current_idx - 1 - number_to_turns[prev_num][0]
            prev_num = last

        if prev_num in number_to_turns:
            number_to_turns[prev_num][0] = number_to_turns[prev_num][1]
            number_to_turns[prev_num][1] = current_idx
        else:
            number_to_turns[prev_num] = [current_idx, current_idx]    
        current_idx += 1

    print(prev_num, turn) 
