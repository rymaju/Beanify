#printing to show that program is running and library is just taking forever to load
print("loading library and creating noun list...")    


# from https://stackoverflow.com/questions/28033882/determining-whether-a-word-is-a-noun-or-not
#pip install nltk, then download(wordnet)

from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}


def beanify(s):
    if s in nouns: 
        return "bean"
    else: 
        return s

def overwrite(inputFile, outputFile):
    print("Beanifying " + inputFile + " as " + outputFile)
    #get all of play as a list of single lines (im not doing try catch block because im lazy)
    lines = open(inputFile).readlines()
    beanifiedPlay = open(outputFile, "w")

    #for every line in lines
    for line in lines:
        wordList = line.split(" ")
        wordList = [beanify(word) for word in wordList]
        line = " ".join(wordList)
        beanifiedPlay.write(line)
        beanifiedPlay.write("\n")
        print(line)

    beanifiedPlay.close()
    print("Done!")

#main begins
i = input("Type the name and extension of the input file (ex. An_Inspector_Calls.txt)\n")

o = input("Type the name and extension of the output file (ex. A_Bean_Calls.txt)\n")

overwrite(i,o)
#main ends


