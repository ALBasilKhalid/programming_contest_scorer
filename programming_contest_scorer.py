# ALBASIL AL-RAWAHI 
"""
ALGORITHM:

The program reads submissions from a file, processes the data to calculate the number of problems solved
and the total time taken by each team, and then displays the results including the winning team.

1. Read Submissions: 
   - Open the file containing submissions.
   - Read each line of the file.
   - Split each line into team name, problem name, and time duration.
   - Organize submissions into a dictionary where each team's submissions are stored.

2. Process Submissions:
   - Iterate over each team's submissions.
   - Create a Submission object for each team.
   - Calculate the number of problems solved and total time taken by each team.
   - Store this information in a list of Submission objects.

3. Display Team Results:
   - Print a header for the results table.
   - Iterate over each Submission object in the list.
   - Print team name, number of problems solved, and total time taken in a formatted manner.

4. Determine Contest Winner:
   - Initialize the winner as the first team in the list of Submission objects.
   - Iterate over each team in the list starting from the second team.
   - Compare the number of problems solved and total time taken with the current winner.
   - Update the winner if the current team has solved more problems or solved the same number of problems in less time.

5. Display Winner:
   - Print the winner of the contest along with the number of problems solved and total time taken.
"""

def ReadSubmissions():
    # Function to read submissions from a file and organize them into a dictionary.    
    # Initialize an empty dictionary to store team submissions.
    teamSubmissions={}
    fileName="submissions.txt"
    # Open the file containing submissions in read mode.
    file = open(fileName, 'r')
    # Read all lines from the file.
    Lines = file.readlines()   
    # Iterate over each line in the file.
    for line in Lines:
        # Strip any leading/trailing whitespace and split the line into components.
        line=(line.strip()).split()
        # Extract team name, problem name, and time duration from the line.
        teamName = line[0]
        problemName = line[1]
        timeDuration = line[2]      
        # Check if teamName is not already in the teamSubmissions dictionary.
        if teamName not in teamSubmissions:
            # If not, add an empty dictionary for the team.
            teamSubmissions[teamName] = {}        
        # Check if problemName not in teamName (seems like a mistake, should probably be if problemName not in teamSubmissions[teamName]).
        if problemName not in teamName:
            # If so, add the problemName and timeDuration to the team's submissions dictionary.
            teamSubmissions[teamName][problemName] = timeDuration
    # Return the dictionary containing team submissions.
    return teamSubmissions

class Submission:

    def __init__(self,teamName):
        # Constructor to initialize a Submission object with teamName, numberOfProblems, and totalTime attributes.
        self.teamName = teamName
        self.numberOfProblems=0
        self.totalTime=0

    def addSubmission(self, totalTime):
        # Method to add a submission for a team, updating numberOfProblems and totalTime.
        self.numberOfProblems += 1
        self.totalTime += int(totalTime)
       
  
def getTeamResults(teamSubmissions):
    # Function to process team submissions and create Submission objects for each team.
    # Initialize an empty list to store Submission objects.
    teamResults = []
    # Iterate over each team and their submissions in the teamSubmissions dictionary.
    for team, problems in teamSubmissions.items():
        # Create a new Submission object for the team.
        submission = Submission(team)
        # Iterate over each time duration in the team's submissions.
        for time in problems.values():
            # Add the time duration as a submission for the team.
            submission.addSubmission(time) 
        # Append the Submission object to the list of teamResults.
        teamResults.append(submission)
    # Return the list of Submission objects.
    return teamResults
    

def displayTeamResults(teamResults): 
    # Function to display team results including the number of problems solved and total time taken.
    print("\nThe results as follows")
    # Print header for the results table.
    print("{:<10} {:>18} {:>16}".format("Team", "#Problems", "Total Time"))
    # Iterate over each Submission object in teamResults.
    for submission in teamResults:
        # Print team name, number of problems, and total time taken in a formatted manner.
        print("{:<10} {:>15} {:>15}".format(submission.teamName, submission.numberOfProblems, submission.totalTime))
    return

def getContestWinner(teamResults):
    # Function to determine the winner of the contest based on the number of problems solved and total time taken.    
    # Initialize the winner as the first team in the list.
    winner = teamResults[0]   
    # Iterate over each team in teamResults starting from the second team.
    for team in teamResults[1:]:
        # Compare the number of problems solved and total time taken with the current winner.
        if team.numberOfProblems > winner.numberOfProblems or (team.numberOfProblems == winner.numberOfProblems and team.totalTime < winner.totalTime):
            # If the current team has solved more problems or solved the same number of problems in less time, update the winner.
            winner = team  
    # Return the winner's team name, number of problems solved, and total time taken as a tuple.
    return winner.teamName, winner.numberOfProblems, winner.totalTime

def main():
    # Main function to execute the program.
    print("Welcome to OCPC 2024\n")
    # Read submissions from the file and store them in a dictionary.
    teamSubmissions=ReadSubmissions()
    # Print the number of teams participating in the contest.
    print("There are",len(teamSubmissions),"teams\n")
    # Display the submissions read from the file.
    print("OCPC 2024 submissions as follow:")
    print(teamSubmissions)
    
    # Process team submissions and create Submission objects.
    teamResults = getTeamResults(teamSubmissions)
    # Display team results including the number of problems solved and total time taken.
    displayTeamResults(teamResults)
    # Determine the contest winner based on the results.
    winner_team, num_problems, total_time = getContestWinner(teamResults)
    # Print the winner of the contest.
    print(f"\nThe OCPC 2024 winner is {winner_team} after solving {num_problems} problems within {total_time} minutes")

# Execute the main function.
main()
