import nltk
#load this package for this file

def open_file_and_get_text(filename):
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text
#"return text" spits out the variable "text"

def clean_tokens(word_list):
    #tokenizes and cleans the list according to instructions
    words = nltk.word_tokenize(word_list)
    clean_words = []
    for word in words:
        clean_words.append(word.lower())
    return clean_words
def common_words(popular_words):
    most_common = []
    count = nltk.FreqDist(popular_words)
    print(count.most_common(5))
    return count

filename = "eyre.txt"

text = open_file_and_get_text(filename)

cleaned_tokens = clean_tokens(text)
frequency = common_words(cleaned_tokens)
nltk.Text(frequency).dispersion_plot(['he', 'she', 'jane', 'tony'])

#print(cleaned_tokens [0:40])

#word_counts = nltk.FreqDist(cleaned_tokens)
#print(word_counts.most_common(10))


#saving specific text as a variable

#with open(filename,'r') as our_file:
#    text = our_file.read()
#given a filename, open it
#takes the file and reads the text, stores it. This produces a read-only file,
#but you can change the command to meet your needs. our_file is a temporary variable.

#this shows the first 99 characters

#words = nltk.word_tokenize(text)
#print(words[0:10])
#take long string and break it into words. word_tokenize is a method.

#if "The" != "the":
#    print("Does case matter?")
#this symble != means "not equal to"

#clean_words = []
#for word in words:
#    clean_words.append(word.lower())
#print(clean_words[0:30])

#this takes all of the selected text and changes the words to lowercase. It creates an empty list called "clean_words"
#the "word in words" loops over every item (token) in the word list
#the third line of code here makes each word lowercase and adds it to the pre-existing list
