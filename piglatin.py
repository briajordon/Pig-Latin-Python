pyg = 'ay'
original = input("Enter a word to translate into Pig Latin: ")
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word= new_word[1:]
if len(original) > 0 and original.isalpha():
    print (original + " in Pig Latin is equal to " + new_word )
else:
    print ('A single word was not inputted.')

input ("Press enter to exit!")
