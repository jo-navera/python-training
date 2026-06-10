# -----*Argument Parser*-----
import argparse

parser = argparse.ArgumentParser()
# User can provide a name as an argument when running the script
parser.add_argument("--name")
# The name of the property here is what is defined in the add_argument method, in this case "name". This will print the value of the name argument provided by the user when running the script.
args = parser.parse_args()

print(args.name)
# -----*Argument Parser*-----

# -----*If-Elif-Else*-----
if number > 0:
    # Runs if condition1 is True
    print("Positive")
elif number < 0:
    # Runs if condition1 is False and condition2 is True
    print("Negative")
else:
    # Runs if none of the above conditions are True
    print("Zero")
# -----*If-Elif-Else*-----

# -----*For Loop*-----
for i in range(5):
    # Code to repeat for each value of i in the range from 0 to 4
    print(i)
# -----*For Loop*-----
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    # Code to repeat for each fruit in the list
    print(fruit)
# -----*For Loop*-----

# -----*While Loop*-----
# Condition to check before each iteration of the loop
while count <= 5:
    # Code to repeat while the condition is True
    print(count)
    # Update the condition to eventually become False to avoid an infinite loop
    count += 1
# -----*While Loop*-----

# -----*Try-Except*-----
try:
    # Code that might fail
    number = int("hello")
except ValueError as error:
    # Runs if an exception occurs
    print(f"Error details: {error}")
except Exception as error:
    # Runs if an exception of any other type occurs
    print(f"Unexpected error: {error}")
finally:
    # Runs regardless of whether an exception occurred or not, often used for cleanup actions
    print("Cleanup complete")
# -----*Try-Except*-----

# -----*Function Definition*-----
# Defines a function named "greet" that takes no arguments
def greet():
    # Code that defines what the function does when called
    print("Hello, world!")

# Calls the function to execute its code
greet()
# -----*Function Definition*-----
# Defines a function named "greet" that takes one argument called "name"
def greet(name):
    # Code that defines what the function does when called, using the provided argument to personalize the greeting
    print(f"Hello, {name}!")

# Calls the function with the argument "Alice", which will print "Hello, Alice!"
greet("Alice")
# Calls the function with the argument "Bob", which will print "Hello, Bob!"
greet("Bob")
# -----*Function Definition*-----
# Defines a function named "add" that takes two arguments called "a" and "b"
def add(a, b):
    # Code that defines what the function does when called, returning the sum of the two arguments
    return a + b

# Calls the function with the arguments 5 and 3, which will return 8
result = add(5, 3)
# Prints the result of the add function, which is 8
print(result)
# -----*Function Definition*-----

# -----Split String and Use in Loop-----
# A string containing items separated by commas. This can come from user input, a file, or any other source.
text = "apple,banana,orange"
# The split method is used to divide the string into a list of substrings based on the specified delimiter, which in this case is a comma. The resulting list will contain the individual items: ["apple", "banana", "orange"].
result = text.split(",")
# A for loop is used to iterate over each item in the resulting list. The variable "item" will take on the value of each element in the list during each iteration of the loop.
for item in result:
    # Inside the loop, the current item is printed. This will output each fruit on a new line: "apple", "banana", and "orange".
    print(item)
# -----Split String and Use in Loop-----

# -----*Load a file and process its contents*-----
from pathlib import Path
# Get the directory where the current script is located
script_dir = Path(__file__).parent
# Determine the file name to load, using a default if no file argument is provided
file_name = file if file else 'records.txt'
# Create a full file path by combining the script directory with the file name
file_path = script_dir / file_name

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the entire contents of the file into a variable called "content"
    content = file.read()
# -----*Load a file and process its contents*-----
