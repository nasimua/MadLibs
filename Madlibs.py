"""
Description: This project takes user input and completes a short story
using the words that the user provides.
Author:  Nasim Ahmed
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("Mad Libs has started")

# ask user for input and store to a variables
name = input("Enter a name: ")
adj_1 = input("Enter an adjective: ")
adj_2 = input("Enter another adjective: ")
adj_3 = input("Enter one more adjective: ")
verb_1 = input("Enter a verb: ")
noun_1 = input("Enter a noun: ")
noun_2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

# format string using % and variables provided by user input
print(
    STORY
    % (
        name,
        adj_1,
        adj_2,
        animal,
        food,
        verb_1,
        noun_1,
        fruit,
        adj_3,
        name,
        superhero,
        name,
        country,
        name,
        dessert,
        name,
        year,
        noun_2,
    )
)
