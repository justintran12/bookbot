path_to_file = "/home/justintran/workspace/github.com/justintran12/bookbot/books/frankenstein.txt"
with open(path_to_file) as f:
    file_contents = f.read()

# return number of words in document
def countWords(file_contents):
    words = file_contents.split()
    return len(words)

# return frequency of letters found in document
def countLetters(file_contents):
    letter_freqs = {}
    file_contents = file_contents.lower()
    for char in file_contents:
        if char.isspace() == False:
            if char not in letter_freqs.keys():
                letter_freqs[char] = 1
            else:
                letter_freqs[char] = letter_freqs.get(char) + 1
    return letter_freqs

# return report of number of words and number of letters found in document sorted by highest frequency
def printReport(file_contents):
    numWords = countWords(file_contents)
    letters = countLetters(file_contents)
    lettersList = letters.keys()

    print("%d words were found in the document" % numWords)
    print("\n")
    for letter in lettersList:
        if (letter.isalpha() == True):
            print("The letter \'%s\' was found %d times" % (letter, letters.get(letter)))


#print(countWords(file_contents))
#print(countLetters(file_contents))
printReport(file_contents)
print(countLetters(file_contents).items())

