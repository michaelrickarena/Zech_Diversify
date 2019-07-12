import csv
import pandas as pd
from functools import reduce

 
#input below
ranked_fighters = {'Francis Ngannou': {'Rank': 5}, 'Junior Dos Santos': {'Rank': 23}, 'Joseph Benavidez': {'Rank': 2}, 'Jussier Formiga': {'Rank': 17}, 'Demian Maia': {'Rank': 12}, 'Anthony Rocco Martin': {'Rank': 16}, 'Vinc Pichel': {'Rank': 8}, 'Roosevelt Roberts': {'Rank': 14}, 'Polo Reyes': {'Rank': 22}, 'Drew Dober': {'Rank': 2}, 'Paul Craig': {'Rank': 21}, 'Alonzo Menifield': {'Rank': 9}, 'Ricardo Ramos': {'Rank': 11}, 'Journey Newson': {'Rank': 15}, 'Eryk Anders': {'Rank': 4}, 'Vinicius Castro': {'Rank': 24}, 'Jared Gordon': {'Rank': 10}, 'Dan Moret': {'Rank': 13}, 'Dalcha Lungiambula': {'Rank': 6}, 'Dequan Townsend': {'Rank': 20}, 'Emily Whitmire': {'Rank': 19}, 'Amanda Ribas': {'Rank': 7}, 'Junior Albini': {'Rank': 18}, 'Maurice Greene': {'Rank': 1}}


all_combinations = [row for row in csv.reader(open("C:/Users/micha/Desktop/Python/Diversification_data.csv", "r"))]
all_combinations.sort(key=lambda row: row[-1], reverse=True)
top_combinations = []
next_rank = 1
worst_rank = reduce(
    lambda fighter_a, fighter_b: fighter_a
    if fighter_a["Rank"] > fighter_b["Rank"]
    else fighter_b,
    ranked_fighters.values(),
)["Rank"]
rank_counts = [0] * worst_rank
recent_ranks = [-1] * 3
for _ in range(150):
    recent_ranks.pop(0)
    recent_ranks.append(next_rank)
    for index, combination in zip(range(len(all_combinations)), all_combinations):
        for fighter in combination[:6]:
            if ranked_fighters[fighter]["Rank"] == next_rank:
                print(f"Found match at {index:3} for rank {next_rank:2}: {fighter}")
                for _fighter in combination[:6]:
                    rank_counts[ranked_fighters[_fighter]["Rank"] - 1] += 1
                top_combinations.append(all_combinations.pop(index))
                break
        else:
            # This only happens when break isn't used
            continue  # Current combination isn't invalid so skip back to the top of the loop
        break  # Current combination was valid so stop looping
    else:
        # This only happens when break isn't used
        print(
            f"No combination could be found for {next_rank}, changing worst rank and moving on"
        )
 
    invalid_ranks = [
        rank + 1
        for rank in range(worst_rank - 1)
        if rank + 1 not in recent_ranks and rank_counts[rank] <= rank_counts[rank + 1]
    ]
    next_rank = invalid_ranks[-1] if len(invalid_ranks) else worst_rank

with open('Zech2.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Score'])
    for comb in top_combinations:
        thewriter.writerow(comb)