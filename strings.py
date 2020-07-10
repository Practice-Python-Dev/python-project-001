# STRING OPERATIONS ... (SORT AND ANALYZE STRINGS)


# FIND WHICH STRING IS BIGGER ...
my_string_a = 'abcdefghijklmnopqrstuvwxyz'
my_string_b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
my_string_c = 'This is a bunch of bologna bro'
# Use an if statement. Compare string length using the built in function len(). Return what the longest string ...
print("<----- Three strings live in thise machine. ----->")

if len(my_string_a) > len(my_string_b) and len(my_string_a) > len(my_string_c):
    print('First string is longer')
elif len(my_string_b) > len(my_string_a) and len(my_string_b) > len(my_string_c):
    print('Second string is longer')
elif len(my_string_c) > len(my_string_a) and len(my_string_c) > len(my_string_b):
    print('Third string is longer')
else:
    print('There was an error.')
print('\n' * 2)




# SLICE INTO STRINGS
print('<----- Let\'s print part of the alphabet. ----->')
# Index formating [start:stop:stride]
# Another example [::2] starts from zero, goes to the end, but still strides 2 indexes (jumps once)
skip_count = int(input('How often do you want to skip letters?'))
# Using skip_count + 1, because the default stride is 1
slice_string = my_string_a[::(skip_count + 1)]

if skip_count == 1:
    print('Skipping every other letter below.')
elif skip_count >= 2:
    print('Skipping every', str(skip_count) + '', 'letters gives us the string below.')
print(slice_string)
print('\n' * 2)




# ASK THE USER WHAT EYE COLOR THEY HAVE
print('<----- Valid Eye Colors ----->')
# Use a for loop to check a user's eye color is legiFor loop to ensure inputs are legit, then print
eye_colors = ['green', 'brown', 'blue', 'hazel', 'grey', 'gray', 'amber']
user_choice = input("What color are your eyes?")
# Convert to lower case just in case ...
user_choice = user_choice.lower()

for i in eye_colors:
    if i == user_choice:
        print('Your eyes are', user_choice)
# Error message if not a real color
if user_choice not in eye_colors:
    print('No way your eyes are', user_choice, '...')



#
# Loop string using range (2 ways)
new_string = 'abcdefghijklmnopqrs'
new_vowels = 0
# Dirty way
for i in range(len(new_string)):
    if new_string[i] == 'i' or new_string[i] == 'e':
        new_vowels += 1
print('There are', new_vowels, 'vowels')
# Clean way
new_vowels = 0
for i in new_string:
    if i == 'i':
        new_vowels += 1
    elif i == 'e':
        new_vowels += 1
print('There are', new_vowels, 'vowels')

