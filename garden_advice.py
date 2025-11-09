# garden_advice.py
"""
Garden Advice App
This app provides simple gardening tips based on the month entered by the user.

TODO:
1. Add more months and seasonal tips.
2. Improve user input handling.
"""

def get_garden_tips(month):
    """
    Returns gardening tips for a given month.

    Args:
        month (str): The name of the month (e.g., "April").

    Returns:
        list: A list of gardening tips for that month.
    """
    tips = {
        "March": ["Plant tomatoes", "Prune roses"],
        "April": ["Plant tomatoes", "Prune roses"],
        "May": ["Plant tomatoes", "Prune roses"],
        "June": ["Water plants daily", "Check for pests"],
        "July": ["Water plants daily", "Check for pests"],
        "August": ["Water plants daily", "Check for pests"],
        # TODO: Add more months
    }
    return tips.get(month, ["No tips for this month yet"])

# Main program
def main():
    month = input("Enter the month: ").capitalize()
    tips = get_garden_tips(month)
    print(f"Gardening tips for {month}:")
    for tip in tips:
        print("-", tip)

if __name__ == "__main__":
    main()

