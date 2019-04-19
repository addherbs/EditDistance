# Complete the electionWinner function below.
def electionWinner(votes):
    print (votes)

    names_count = {}
    max_vote = 0

    for each_name in votes:
        if (each_name in names_count):
            names_count[each_name] += 1
        else:
            names_count[each_name] = 1

    for key, value in names_count.items ():
        max_vote = max (max_vote, value)

    max_vote_names = []
    for key, value in names_count.items ():
        if (value == max_vote): max_vote_names.append (key)


