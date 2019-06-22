# PyBank Code

import os
import csv

# tells computer about path to dataset
csvpath = os.path.join("election_data.csv")
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None) # Orders computer to skip first row of data (headers)
#creating variables to store data, list and dictionaries
    total_votes = 0
    # votes_per_candidate = 0
    candidates = []
    dic = {}

    all_votes = [] # this dictionary will store the accumulated votes (each time a candidate is mentioned in the file)

#Counting the number of total votes cast:
    for row in csvreader:
        total_votes = total_votes + 1 # votes count
        all_votes.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2]) # creates list of candidates
    

    print("Number of candidates: " + str(len(candidates))) # number of candidates: 4 
    print("Number of votes cast: " + str(total_votes)) # total number of votes


#Presenting a list of the candidates who received votes:

    votes_list=[0,0,0,0] # creating list for counting the votes of each candidate

    dict_candidates = dict(zip(candidates, votes_list)) # dictionary for storing candidates and total votes

    for k in dict_candidates.keys(): # for each candidate (each one being a key)
        for x in range(len(all_votes)):
            if all_votes[x]==k:
                dict_candidates[k]+=1                

    print(dict_candidates)

    dict_candidates_per={}
    dict_candidates_per = dict.fromkeys(dict_candidates)
    print(dict_candidates_per)

    for k in dict_candidates.keys(): # each candidate corresponds to a given key
        dict_candidates_per[k] = dict_candidates[k]/total_votes
    print (dict_candidates_per)