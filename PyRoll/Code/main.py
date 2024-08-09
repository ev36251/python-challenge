import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


def analyze_election_data(csvpath):
        
        with open(csvpath) as election_data:
                csvreader = csv.reader(election_data, delimiter=',')
                csv_header = next(csvreader)


                total_votes = 0
                candidate_votes = {} #dictionary with candidate name as key, and # of votes as value


                for row in csvreader:
                        total_votes += 1
                        candidate_name = row[2]

                        if candidate_name in candidate_votes:
                                candidate_votes[candidate_name] += 1 #if candidate already exists, increment their vote count
                        else:
                                candidate_votes[candidate_name] = 1 #if not, add candidate to dictionary with give them 1 vote
                
                winner = max(candidate_votes, key=candidate_votes.get)

                output = [
                        "----------------------------",
                        "Election Results",
                        "----------------------------",
                        f"Total Votes: {total_votes}",
                        "----------------------------",
                ]
        
                for candidate, votes in candidate_votes.items():
                        vote_percent = (votes / total_votes) * 100
                        output.append(f"{candidate}: {vote_percent:.3f}% ({votes})")
                
                output.append("----------------------------")
                output.append(f"Winner: {winner}")
                output.append("----------------------------")
                
                return output

# Write the output to a text file

output_path = os.path.join('..', 'analysis', 'election_data_output.txt')

output = analyze_election_data(csvpath)


with open(output_path, mode='w') as output_file:
    for line in output:
        output_file.write(line + '\n')

for line in output:
    print(line)
