path = "Homework_7/Parties.txt"

votes = {}

with open(path, "r") as f:
    for line in f:
        line = line.replace("\n", "")
        if line in ["PARTIES:", "VOTES:"]:
            continue

        if line not in votes:
            votes[line] = 0
        else:
            votes[line] += 1

all_votes = sum(votes.values())

for party, votes in votes.items():
    percent = votes / all_votes * 100
    if percent > 7:
        print(party)
