"""Discovery Call Scorer: asks yes/no questions about a sales discovery call,
totals a score, and rates the call as Strong, Mediocre, or Not Ready.
Author: Abdi Sherif
Date: November 25, 2026"""

# List of the four questions a rep answers about the call
QUESTIONS = ["Did the customer mention a budget?",
             "Were you talking to the decision maker?",
             "Did the customer describe a real problem?",
             "Did the customer give a timeline?"]


# Define a function that shows the welcome message and instructions
def showWelcome():
    """Shows the welcome message and instructions."""
    # Print the program title
    print("Welcome to the Discovery Call Scorer!")
    # Print instructions telling the user how to answer
    print("Answer each question about your call with yes or no.")
    # Print a blank line to separate the welcome from the questions
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


# Define the main function that runs the program
def main():
    """Runs the Discovery Call Scorer."""
    # Show the welcome message and instructions
    showWelcome()
    # Test askYesNo with the first question and print what it returns
    print(askYesNo(QUESTIONS[0]))


# Run main only when this file is run directly
if __name__ == "__main__":
    main()
