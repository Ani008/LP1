# Implement any one of the following Expert System
# IV. Employee performance evaluation

# List of evaluation criteria
criteria = ["productivity", "communication", "teamwork", "punctuality", "quality_of_work"]

# Function to get rank input from the user (from -5 to 5)
def get_rank_input(criterion):
    rank = int(input(f"Enter rank for {criterion} (-5 to 5): "))
    if -5 <= rank <= 5:
        return rank
    else:
        print("Invalid input. Please enter an integer between -5 and 5.")
    return get_rank_input(criterion)

# Function to evaluate total score
def evaluate_employee(ranks):
    return sum(ranks.values())

# Main function
def main():
    ranks = {}
    for criterion in criteria:
        ranks[criterion] = get_rank_input(criterion)

    score = evaluate_employee(ranks)
    print(f"\nTotal Score: {score}")

    if score > 15:
        print("Performance: Exceptional")
    elif score > 10:
        print("Performance: Outstanding")
    elif score > 0:
        print("Performance: Good")
    elif score == 0:
        print("Performance: Neutral")
    elif score >= -10:
        print("Performance: Needs Improvement")
    elif score >= -15:
        print("Performance: Poor")
    else:
        print("Performance: Critical - Immediate Action Needed")

main()
