# Strings and casting

# some industry practices
# single and double quotes

greeting = "Hello World!"
# single_quotes = 'Single Quotes \'WOW\''
# double_quotes = "Double Quotes"

# print(single_quotes)
# print(double_quotes)


# String slicing
# greetings = "Hello world!" # string

# indexing in python starts from 0

# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

# How can we find the length of this string?

# print(len(greetings))

# slicing

# print(greetings[:5])
# print(greetings[6:11])
# print(greetings[-6:])

# reverse indexing in the exam

# whitespace = "lots of space at the end                "


# print(len(whitespace))
# print(len(whitespace.strip())) # strip removes whitespaces


# count() counts number of substrings in strings
example_text = "there's a lot of text in this text"
# print(example_text.count("text"))

# some useful string methods
# print(example_text)
# print(example_text.upper()) # capitalises all letters
# print(example_text.lower()) # lowercases all letters
# print(example_text.capitalize()) # capitalises the first letter
# print(example_text.replace("lot", "lol")) # replaces a substring with another

# concatenation
first_name = "James" # string
last_name = "Bond" # string
age = 99 # int

print(first_name + " " + last_name)
print(first_name, last_name)

# casting int to str
print(first_name + " " + last_name + ", " + str(age)) # str() converts other datatypes to string

# casting str to int
age = "99"
print(type(int(age)))

# formatting a string
print(f"Your first name is {first_name}, your last name is {last_name}, and you are {age} years old")


