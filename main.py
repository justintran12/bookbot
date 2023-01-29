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
def printReport(file_contents, book_name):
    num_words = countWords(file_contents)
    letters = countLetters(file_contents)
    # convert dictionary to list and sort by value
    sorted_letters = sorted(countLetters(file_contents).items(), key = lambda x:x[1], reverse = True)

    print("--- Report of %s ---" % book_name)
    print("%d words were found in the document" % num_words)
    print("\n")
    # sorted_letters is a list of tuples, each tuple is a key/value pair
    for letter_pair in sorted_letters:
        if (letter_pair[0].isalpha() == True):
            print("The letter \'%s\' was found %d times" % (letter_pair[0], letter_pair[1]))

    print("--- End of Report ---")

def main():
    path_to_file = "/home/justintran/workspace/github.com/justintran12/bookbot/books/frankenstein.txt"
    path_split = path_to_file.split("/")
    book_name = path_split[len(path_split) - 1]
    with open(path_to_file) as f:
        file_contents = f.read()

    #print(countWords(file_contents))
    #print(countLetters(file_contents))
    printReport(file_contents, book_name)
    
# only executes if running as a script on command line not importing
if __name__ == "__main__":
    main()

