"""
Variables
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to
switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed
to use variables to solve this exercise.
"""

glass1 = "milk"
glass2 = "juice"
print("This is the glasses before change:\n" + glass1 + "\n" + glass2)
glass3 = glass1
glass1 = glass2
glass2 = glass3

print("This is the glasses after change:\n" + glass1 + "\n" + glass2)