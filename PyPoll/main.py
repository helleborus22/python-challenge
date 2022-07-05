#import the csv and os files
import csv
import os

inputFile = os.path.join("Resources","election_data.csv")

#output file location for analysis
outputFile = os.path.join("Analysis.txt")

#set up variables
totalVotes = 0
Candidate = [] #list
CandidatesVotes = {} #dictionary
winningCount = 0
winningCandidates = ""
#read the csv file
with open(inputFile) as electionData:
    #create the csv reader
    csvreader = csv.reader(electionData)

    #read the header
    header = next(csvreader)

    #rows will be lists
        #index 0 is the user ID
        #index 2 is the user choice

    #for each row
    for row in csvreader:
        #add on to the total votes
        totalVotes += 1

        #check if the candidate is on the list of candidates or not
        if row[2] not in Candidate:
            #then add to the list
            Candidate.append(row[2])

            #add to the dictionary as well {"key": "value"}, start the count at 1
            CandidatesVotes[row[2]] = 1
        else:
            CandidatesVotes[row[2]] += 1
voteOutput = ""

for Candidate in CandidatesVotes:
    #get the vote count and the percentage
    votes = CandidatesVotes.get(Candidate)
    votePercentage = (float(votes) / float(totalVotes)) *100.00

    voteOutput += f"{Candidate}: {votePercentage:.3f}% ({votes})\n"
    #compare the votes to the winning count
    if votes > winningCount:
        winningCount = votes
        winningCandidate = Candidate

winningCandidateOutput = f"Winner: {winningCandidate}"
    
#create an output variable to hold the output
output = (
    f"Election Results\n"

    f"-----------------------\n"

    f"Total Votes:{totalVotes}\n"

    f"-----------------------\n"

    f"{voteOutput}\n"

    f"-----------------------\n"

    f"{winningCandidateOutput}\n"

    f"-----------------------"

)
#display the output to the console
print(output)
#export the output to txt file
with open(outputFile, "w") as textFile:
    textFile.write(output)
