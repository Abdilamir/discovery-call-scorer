"""Discovery Call Scorer: asks yes/no questions about a sales call,
totals a score, and rates the call as Strong, Mediocre, or Not Ready.
Author: Abdi Sherif
Date: November 25, 2026"""

# The four questions about the call
QUESTIONS = ["Did the customer mention a budget?",
             "Were you talking to the decision maker?",
             "Did the customer describe a real problem?",
             "Did the customer give a timeline?"]


# Ask one question until the answer is yes or no
def askYesNo(question):
    """Returns True for yes, False for no."""
    # Get the answer without extra spaces, in lowercase
    answer = input(question + " ").strip().lower()
    # Keep asking until the answer is yes or no
    while answer not in ["yes", "no"]:
        # Tell the user what to type
        print("Please type yes or no.")
        # Ask again
        answer = input(question + " ").strip().lower()
    # True if yes, False if no
    return answer == "yes"


# Turn a score into a rating
def rateCall(score):
    """Returns the rating for a score."""
    # 4 points is a strong call
    if score == 4:
        return "Strong"
    # 2 or 3 points is a mediocre call
    elif score >= 2:
        return "Mediocre"
    # 0 or 1 point means not ready
    else:
        return "Not Ready"


# Run the program
def main():
    """Asks the questions and shows the score and rating."""
    # Welcome message and instructions
    print("Welcome to the Discovery Call Scorer!")
    print("Answer each question with yes or no.\n")
    # Start the score at zero
    score = 0
    # Ask each question and add a point for each yes
    for question in QUESTIONS:
        if askYesNo(question):
            score = score + 1
    # Show the score and rating
    print("\nScore:", score, "out of 4")
    print("Rating:", rateCall(score))


# Run main when this file is run
if __name__ == "__main__":
    main()
