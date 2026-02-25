# Day 8: Lists and loops in Python

# Creating a list
countries = ["Malawi", "Zambia", "Tanzania"]

# Adding a new item to the list
countries.append("Mozambique")

# Looping through the list and printing countries
# with more than 6 letters
for country in countries:
    if len(country) > 6:
        print(country)
