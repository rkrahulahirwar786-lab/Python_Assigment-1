# tracker_basic.py
# Student: Rahul Ahirwar
# section: G 
# Date: 14-11-2025
# Project: Daily Calorie Tracker (Basic)
# Description: Basic CLI calorie tracker that collects meals, calculates total & average,

from datetime import datetime

def get_positive_number(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val < 0:
                print("Enter a non-negative number.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to Daily Calorie Tracker (Basic).")
    print("Enter your meals and calories. The program will show total, average and save option.\n")

    meals = []
    calories = []

    num = int(get_positive_number("How many meals do you want to enter? "))
    for i in range(1, num+1):
        name = input(f"Meal {i} name (e.g., Breakfast): ").strip() or f"Meal{i}"
        cal = get_positive_number(f"Calories for '{name}': ")
        meals.append(name)
        calories.append(cal)

    total = sum(calories)
    average = total / len(calories) if calories else 0.0

    limit = get_positive_number("\nEnter your daily calorie limit: ")

    status = "WITHIN LIMIT" if total <= limit else "EXCEEDED LIMIT"

 
    print("\nMeal Name\t\tCalories")
    print("-" * 40)
    for m, c in zip(meals, calories):
        print(f"{m:<16}\t{c:.2f}")
    print("-" * 40)
    print(f"{'Total:':<16}\t{total:.2f}")
    print(f"{'Average:':<16}\t{average:.2f}")
    print(f"Daily limit: {limit:.2f} -> {status}")

    save = input("\nDo you want to save this session to a text file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"calorie_log_basic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(f"Session timestamp: {datetime.now()}\n")
            f.write("Meal Name\tCalories\n")
            f.write("-" * 40 + "\n")
            for m, c in zip(meals, calories):
                f.write(f"{m}\t{c:.2f}\n")
            f.write("-" * 40 + "\n")
            f.write(f"Total:\t{total:.2f}\n")
            f.write(f"Average:\t{average:.2f}\n")
            f.write(f"Daily limit: {limit:.2f} -> {status}\n")
        print(f"Saved session to {filename}")

if __name__ == "__main__":
    main()