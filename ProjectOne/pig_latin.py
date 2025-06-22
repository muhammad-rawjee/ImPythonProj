CONSONANTS = set(list("bcdfghjklmnpqrstvwxyz"))
VOWELS = set(list("aeiou"))
# Get Input
sentenceToConvert = input("What did say?\n")
# Convert input into list
sentenceToWordList = sentenceToConvert.split()
# Convert each word into pig latin
def pigLatinConverter(wordList):
    res = []
    print(wordList)
    for word in wordList:
        if word[0].lower() in CONSONANTS:
            # Deal with consonant clusters later
            new_word = 
        pass
        
