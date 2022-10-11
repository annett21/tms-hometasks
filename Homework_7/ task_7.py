path = "Homework_7/Votes.txt"
parliament_places = 450
parties = []

with open(path, "r") as f:
    for line in f:
        line = line.split()
        party_name, party_votes = " ".join(line[:-1]), int(line[-1])
        parties.append({"name": party_name, "votes": party_votes})

all_votes = sum([party["votes"] for party in parties])
first_electoral_quotient = all_votes / parliament_places

for party in parties:
    unused_places = (party["votes"] / first_electoral_quotient) % 1
    places = int(party["votes"] // first_electoral_quotient)
    party.update({"unused_places": unused_places, "places": places})

left_places = parliament_places - sum((party["places"] for party in parties))
sorted_parties = sorted(
    parties,
    key=lambda party: (party["unused_places"], party["votes"]),
    reverse=True,
)

for party in sorted_parties[:left_places]:
    party["places"] += 1

for party in parties:
    print(party["name"], party["places"])
