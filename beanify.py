#printing to show that program is running and library is just taking forever to load
print("loading WordNet and creating noun list...")

# from https://stackoverflow.com/questions/28033882/determining-whether-a-word-is-a-noun-or-not
#get the WordNet library and create a list of nouns
from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}

#takes a string s; returns "bean" if s exists in the list of nouns from WordNet, else returns s unmodified
def beanify(s):
    if s in nouns: 
        return "bean"
    else: 
        return s

#takes in an input file and output file; reads the whole input file as a string, splits it into words, performs beanify() on each word, and writes the list as a string into the output file
def beanifyFile(inputFile, outputFile):
    text = open(inputFile).read()
    wordList = [beanify(word) for word in text.split(" ")]
    text = " ".join(wordList)
    print(text)
    beanifiedPlay = open(outputFile, "w")
    beanifiedPlay.write(text)
    beanifiedPlay.close()
    print("Done!")

#main program begins, asks for the input and output file, calls beanifyFile()
i = input("Type the name and extension of the input file (ex. An_Inspector_Calls.txt)\n")
o = input("Type the name and extension of the output file (ex. A_Bean_Calls.txt)\n")
beanifyFile(i,o)