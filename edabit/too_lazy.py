def calculate_score(games):
    abigal_score = 0
    ben_score = 0

    for game in games:
        if game[0] == "R" and game[1] == "P":
            # ben wins
            ben_score += 1
        elif game[0] == "P" and game[1] == "R":
            # abigal wins
            abigal_score += 1
        elif game[0] == "S" and game[1] == "R":
            # ben wins
            ben_score += 1
        elif game[0] == "R" and game[1] == "S":
            # abigal wins
            abigal_score += 1
        elif game[0] == "S" and game[1] == "P":
            # abigal wins
            abigal_score += 1
        elif game[0] == "P" and game[1] == "S":
            # ben wins
            ben_score += 1
        elif game[0] == "R" and game[1] == "P":
            # ben wins
            ben_score += 1
        else:
            # tie
            pass
    if abigal_score > ben_score:
        return "Abigail"
    elif abigal_score == ben_score:
        return "Tie"
    else:
        return "Benson"
