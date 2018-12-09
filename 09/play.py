from tqdm import trange

def play(number_player, last_marble):
    scores = { p: 0 for p in range(number_player) }
    marbles = { p: 0 for p in range(number_player) }

    board = [0, 2 ,1]
    current_position = 1

    for marble_number in trange(3, last_marble+1):
        current_player = marble_number % number_player
        marbles[current_player] = marble_number
        if marble_number % 23 == 0:
            current_position -= 7
            current_position %= len(board)
            scores[current_player] += marble_number + board.pop(current_position)
        else:
            if current_position == len(board) - 2:
                current_position = len(board)
            else:
                current_position = (current_position + 2) % len(board)
            board.insert(current_position, marble_number)
        #print(marble_number, current_position, board)

    #return max(scores.items(), key=lambda x: x[1])[1], scores, marbles
    return max(scores.items(), key=lambda x: x[1])[1]
