# PLAY AROUND WITH THE ALPHABET

# Initialize variable containing the alphabet (lower case), and start vowel count from 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 0
# Use a for loop to check if/or. Add to 'vowels' if True.
for i in alphabet:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
print('There are', str(vowels), 'vowels in the alphabet.')
print('\n' *1)




# Ask for a letter in the alphabet, ensure to point to it's lowercase
user_letter = input('Enter one letter')
user_letter = user_letter.lower()

# Loop through the alphabet. If the letter is in then print it and 'break' out of the for loop. If it isn't print sorrr ...
for i in range(len(alphabet)):
    if alphabet[i] == user_letter:
        print('You entered', user_letter, 'which is in the alphabet!')
        break
else:
    print('Sorry. You entered', user_letter, ', which isn\'t a letter ...')
print('\n' *1)



# This time initialize all possible letters. Use a 'while' loop to check and print in a cool way!

# Initialze all letters. Ask user for word. Ask user how many times to print.
all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
user_word = input('Enter a word, so I can print it back to you:')
how_many_times = int(input('How many times do you want to hear your word?'))

i = 0
while i < len(user_word):
    char = user_word[i]
    if char in all_letters:
        print('Give me an', char, '!')
    i += 1
print('What does that spell?')
for i in range(how_many_times):
    print(user_word, '!!!')
print('\n' *1)
