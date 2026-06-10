# Run this exercise with the following command:
# python Exercise1.py --food "apple, adobo, Banana"
# Modify the code to identify if each food item is a fruit or not, and print the result accordingly.
# Expected output with the above command:
# Apple is a fruit.
# Adobo is not a fruit.
# Banana is a fruit.

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--food")
    args = parser.parse_args()
    return args.food


def main_process(food):
    # Split the input food string into individual items and check if each item is a fruit or not
    food_items = food.split(",")
    fruit_list = ["apple", "banana", "orange"]
    for item in food_items:
        if item.strip().lower() in fruit_list:
            print(f"{item.strip().capitalize()} is a fruit.")
        else:
            print(f"{item.strip().capitalize()} is not a fruit.")


if __name__ == "__main__":
    food = parse_arguments()
    main_process(food)

# Sample line added here to demo git commit and push
