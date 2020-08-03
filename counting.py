#------------------------------
# COUNT VOWELS IN THE ALPHABET
#------------------------------

# Initialize alphabet in a string, Initialize a counter
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = 0

# Check using 'if/or' - Add to 'vowels' if True
for i in alphabet:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels += 1
print("There are", str(vowels), "vowels in the alphabet.")
print("\n")

#------------------------------
# ASK FOR A LETTER IN THE ALPHABET
#------------------------------

# Ask user for a letter, Ensure it's lowercase
user_letter = input("Enter a Letter: ")
user_letter = user_letter.lower()

# If it's in the alphabet print and 'break' - If not print an 'error message'
for i in range(len(alphabet)):
    if alphabet[i] == user_letter:
        print("You entered", user_letter, "which is in the alphabet!")
        break
else:
    print("Sorry. You entered", user_letter, "which isn\'t a letter ...")
print("\n" *1)

#------------------------------
# SAME, BUT PRINT IN A COOL WAY
#------------------------------

# Initialize all possible letters, Initialize a counter
all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = 0

#Ask user for input, Ask how many times to print
user_word = input("Enter a word, so I can print it back to you:")
how_many_times = int(input("How many times do you want to hear your word?"))

# Use a 'while' loop to check and print

while counter < len(user_word):
    char = user_word[index]
    if char in all_letters:
        print("Give me an", char, "!")
    counter += 1
print("What does that spell?")
for counter in range(how_many_times):
    print(user_word, "!!!")
print("\n")
