
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

# Module
import os
import csv

# Set path for file  PayPoll/Resources
csvpath = os.path.join(".","Resources", "election_data.csv")

# 5 Lists 
candidates=[]
cant_candidates=[]
count_candidates=[]
unique_candidate=[]
votes=[]

# Open the CSV --election_data.csv / Skip the header
with open(csvpath, newline='', encoding="utf8") as election_data:
  csvreader = csv.reader(election_data, delimiter=',')  
  header = next(csvreader)

   #Loop to find the Votes 
  for row in csvreader:
      #  the length of the Votes_list
      votes.append(row[0])
      length = str(len(votes))

      # list of all candidates
      count_candidates.append(row[2])

  #  list of unique candidates,
  for i in count_candidates:
      if i not in unique_candidate:
          unique_candidate.append(i)

  # Total count of each candidate w/ comprehension method
  comprehension_list_total_count = [[x,count_candidates.count(x)] for x in set(count_candidates)]

  # Dictionary 
  summary_total_candidates = dict((x,count_candidates.count(x)) for x in set(count_candidates))

  # Keys and values from dictionary
  for key in summary_total_candidates:
      keys = key
  for value in summary_total_candidates.items():
      values = value

  # To know the one that recevied more votes, to be able to obtain the winner
  for row in comprehension_list_total_count:
     candidates.append(row[0])
     cant_candidates.append(int(row[1]))

  # Max value of the list of votes.
  max_increase_value = max(cant_candidates)
  max_increase_value_index = cant_candidates.index(max_increase_value)
  winner = candidates[max_increase_value_index]

 # Print the analysis 
print("Election Results")
print("-----------------------")
print(f"Total votes: {length}")
print("-----------------------")

for key, value in summary_total_candidates.items():
  print(f"{key}: {round((float(value)/int(length))*100,3)}% ({value})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

#Export a text file with the results
textfile_path = os.path.join('.','Resources','Final_Results_PayPoll.txt')

with open (textfile_path, 'w') as txtfile:
    txtfile.write(f"Election Results")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total votes: {length}")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    for key, value in summary_total_candidates.items():
      txtfile.write("\n")  
      txtfile.write(f"{key}: {round((float(value)/int(length))*100,3)}% ({value})")
      txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    

