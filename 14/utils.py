def generate_scores(n=2000):
    scores = [3,7] + [-1] * (n+20)
    score_len = 2
    player1_index = 0
    player2_index = 1
    while score_len < n+10:
        combined_score = scores[player1_index] + scores[player2_index]
        if combined_score // 10 != 0:
            scores[score_len] = combined_score // 10
            score_len += 1
        scores[score_len] = combined_score % 10
        score_len += 1
        player1_index = (player1_index + 1 + scores[player1_index]) % score_len
        player2_index = (player2_index + 1 + scores[player2_index]) % score_len

    return scores[:score_len]



def score(scores, n):
    assert n+10<len(scores)
    return ''.join(map(str, scores[n: n+10]))



def find_score(scores, score):
    return ''.join(map(str, scores)).find(score)
