def seeTheTruth(word):
    stripper = """,."'"""
    return word.strip(stripper).lower()
class InvertedFile:
    def __init__(self, file_name):
        file = open(file_name,"r")
        fileStr = file.read()
        wordList = fileStr.split()
        self.map = {}
        index = 0
        for word in wordList:
            trueWord = seeTheTruth(word)
            print(trueWord)
            if trueWord not in self.map:
                self.map[trueWord] = [index]
            else:
                self.map[trueWord].append(index)
            index +=1
    def indices(self,word):
        trueWord = seeTheTruth(word)
        if trueWord in self.map:
            return self.map[trueWord]
        return []

def test():
    file = InvertedFile("row your boat.txt")
    print(file.indices("row"))
    print(file.indices("the"))
    print(file.indices("hook"))
#test()
