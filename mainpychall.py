import os
import csv

csvpath = "resources/election_data.csv"
file_output = "resources/election_results.txt"

total_votes = 0

vote_count = {}
candidate_options = []

winning_candidates = ""
winning_counts = 0

with open(csvpath) as election_data:
    csvreader = csv.reader(election_data)

    csv_header = next(csvreader)

    for row in csvreader:    
        total_votes = total_votes + 1  

        candidate_name = row[2]


        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            vote_count[candidate_name] = 0


        vote_count[candidate_name] = vote_count[candidate_name] + 1 


    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total_Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

with open(file_output, "w") as txt_file:
    txt_file.write(election_results)


    for candidate in vote_count:

        vote_names = vote_count[candidate]

        vote_percentage = float(vote_names) / float(total_votes)* 100

        if vote_names > winning_counts:
            winning_counts = vote_names
            winning_candidates = candidate

        output_votes = f"{candidate}:{vote_percentage:.3f}% ({vote_names})\n"
        print(output_votes)
        txt_file.write(output_votes)


            
    winning_candidates_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidates}\n"
        f"-------------------------\n")
    print(winning_candidates_summary)
        
    txt_file.write(winning_candidates_summary)


                                



