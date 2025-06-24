import sys
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
        # Consonant cluster
        if word[0].lower() in CONSONANTS and word[1].lower() in CONSONANTS:
            pass
        elif word[0].lower() in CONSONANTS:
            # Deal with consonant clusters later
            new_word =  word[1].upper() + word[2:] + f"-{word[0]}ay"
            res.append(new_word)
    
    return " ".join(res)

print(pigLatinConverter("Ali was here".split()))


        
