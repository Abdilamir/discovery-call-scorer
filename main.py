"""Discovery Call Scorer: asks yes/no questions about a sales discovery call,
totals a score, and rates the call as Strong, Mediocre, or Not Ready.
Scored calls are saved to a file so the user can see a summary later.
Author: Abdi Sherif
Date: November 25, 2026"""

# List of the four questions a rep answers about the call
QUESTIONS = ["Did the customer mention a budget?",
             "Were you talking to the decision maker?",
             "Did the customer describe a real problem?",
             "Did the customer give a timeline?"]

# Name of the file where scored calls are saved
FILE_NAME = "calls.txt"


# Define a function that shows the welcome message and instructions
def showWelcome():
    """Shows the welcome message and instructions."""
    # Print the program title
    print("Welcome to the Discovery Call Scorer!")
    # Print instructions telling the user how to answer
    print("Answer each question about your call with yes or no.")
    # Print a blank line to separate the welcome from the menu
    print()


# Define a function that asks one question until the answer is yes or no
def askYesNo(question):
    """Asks a yes/no question and returns True for yes, False for no."""
    # Ask the question, remove extra spaces, and make the answer lowercase
    answer = input(question + " ").strip().lower()
    # Keep asking while the answer is not yes, y, no, or n
    while answer not in ["yes", "y", "no", "n"]:
        # Tell the user what went wrong
        print("Please type yes or no.")
        # Ask the same question again
        answer = input(question + " ").strip().lower()
    # Return True if the answer was yes, otherwise False
    return answer in ["yes", "y"]


# Define a function that asks every question and adds up the score
def scoreCall():
    """Asks all the questions and returns the total score."""
    # Start the score at zero
    score = 0
    # Go through each question in the list, one at a time
    for question in QUESTIONS:
        # If the user answered yes, add one point
        if askYesNo(question):
            # Add one to the score
            score = score + 1
    # Return the total score
    return score


# Define a function that turns a score into a rating
def rateCall(score):
    """Returns Strong, Mediocre, or Not Ready for a score."""
    # A perfect score of 4 is a strong call
    if score == 4:
        # Return the strong rating
        return "Strong"
    # A score of 2 or 3 is a mediocre call
    elif score >= 2:
        # Return the mediocre rating
        return "Mediocre"
    # Any other score (0 or 1) means the call is not ready
    else:
        # Return the not ready rating
        return "Not Ready"


# Define a function that adds one scored call to the end of the file
def saveCall(customer, score, rating):
    """Saves one scored call to the file."""
    # Open the file in append mode so old calls are kept
    with open(FILE_NAME, "a") as outfile:
        # Write the customer, score, and rating on one line, split by commas
        outfile.write(customer + "," + str(score) + "," + rating + "\n")


# Define a function that reads the file and prints every saved call
def showSummary():
    """Prints every saved call and how many there are."""
    # Try to open the file, since it won't exist before the first save
    try:
        # Open the file for reading
        with open(FILE_NAME, "r") as infile:
            # Read all the lines into a list
            lines = infile.readlines()
    # If the file isn't there yet, there are no saved calls
    except FileNotFoundError:
        # Use an empty list so the code below still works
        lines = []
    # Print a heading for the summary
    print("\nSaved Calls")
    # Go through each saved line
    for line in lines:
        # Split the line into customer, score, and rating
        parts = line.strip().split(",")
        # Print the call in a readable way
        print(parts[0] + ": " + parts[1] + "/4 - " + parts[2])
    # Print how many calls were found
    print("Total calls saved:", len(lines))
    # Print a blank line after the summary
    print()


# Define a function that shows the menu and returns a valid choice
def getMenuChoice():
    """Shows the menu and returns 1, 2, or 3."""
    # Print the menu options
    print("1. Score a new call")
    print("2. Show saved calls")
    print("3. Quit")
    # Ask for a choice and remove extra spaces
    choice = input("Choose 1, 2, or 3: ").strip()
    # Keep asking while the choice is not 1, 2, or 3
    while choice not in ["1", "2", "3"]:
        # Tell the user what went wrong
        print("Please type 1, 2, or 3.")
        # Ask again
        choice = input("Choose 1, 2, or 3: ").strip()
    # Return the valid choice
    return choice


# Define the main function that runs the program
def main():
    """Runs the Discovery Call Scorer."""
    # Show the welcome message and instructions
    showWelcome()
    # Get the first menu choice
    choice = getMenuChoice()
    # Keep going until the user chooses 3 to quit
    while choice != "3":
        # Choice 1 scores a new call
        if choice == "1":
            # Ask for the customer's name and swap out commas for the file
            customer = input("Customer name: ").strip().replace(",", " ")
            # Keep asking while the name is blank
            while customer == "":
                # Tell the user what went wrong
                print("Please enter a name.")
                # Ask again
                customer = input("Customer name: ").strip().replace(",", " ")
            # Ask the questions and get the total score
            score = scoreCall()
            # Turn the score into a rating
            rating = rateCall(score)
            # Show the result to the user
            print("\nScore:", score, "out of 4")
            print("Rating:", rating)
            print()
            # Save the call to the file
            saveCall(customer, score, rating)
        # Choice 2 shows the saved calls
        else:
            # Print the summary of saved calls
            showSummary()
        # Show the menu again and get the next choice
        choice = getMenuChoice()
    # Say goodbye when the user quits
    print("Goodbye!")


# Run main only when this file is run directly
if __name__ == "__main__":
    main()
