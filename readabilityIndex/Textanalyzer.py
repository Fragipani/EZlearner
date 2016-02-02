#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sets the encoding to utf-8 to avoid problems with Ã¦Ã¸Ã¥
import nltk.data
from nltk.tokenize import *

class textanalyzer(object):

    tokenizer = RegexpTokenizer('(?u)\W+|\$[\d\.]+|\S+')
    special_chars = ['.', ',', '!', '?']

    def analyzeText(self, text=''):
        words = self.getWords(text)
        charCount = self.getCharacterCount(words)
        wordCount = len(words)
        sentenceCount = len(self.getSentences(text))
        complexwordsCount = self.countComplexWords(text)
        averageWordsPerSentence = wordCount/sentenceCount
        print(' Number of characters: ' + str(charCount))
        print(' Number of words: ' + str(wordCount))
        print(' Number of sentences: ' + str(sentenceCount))
        print(' Number of complex words: ' + str(complexwordsCount))
        print(' Average words per sentence: ' + str(averageWordsPerSentence))
    #analyzeText = classmethod(analyzeText)


    def getCharacterCount(self, words):
        characters = 0
        for word in words:
            characters += len(word)
        return characters
    #getCharacterCount = classmethod(getCharacterCount)

    def getWords(self, text=''):
        words = []
        words = self.tokenizer.tokenize(text)
        filtered_words = []
        for word in words:
            if word in self.special_chars or word == " ":
                pass
            else:
                new_word = word.replace(",","").replace(".","")
                new_word = new_word.replace("!","").replace("?","")
                filtered_words.append(new_word)
        return filtered_words
    #getWords = classmethod(getWords)

    def getSentences(self, text=''):
        sentences = []
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(text)
        return sentences
    #getSentences = classmethod(getSentences)

    #This method must be enhanced. At the moment it only
    #considers the number of syllables in a word.
    #This often results in that too many complex words are detected.
    def countComplexWords(self, text=''):
        words = self.getWords(text)
        sentences = len(self.getSentences(text));
        sentencesList = self.getSentences(text);
        complexWords = 0
        found = False;
        #Just for manual checking and debugging.
        cWords = []
        curWord = []

        for word in words:
            curWord.append(word)
            if len(word)>= 8:

                #Checking proper nouns. If a word starts with a capital letter
                #and is NOT at the beginning of a sentence we don't add it
                #as a complex word.
                if not(word[0].isupper()):
                    complexWords += 1
                    #cWords.append(word)
                else:
                    for sentence in sentencesList:
                        if str(sentence).startswith(word):
                            found = True
                            break

                    if found:
                        complexWords+=1
                        found = False

            curWord.remove(word)
        #print cWords
        return complexWords
    #countComplexWords = classmethod(countComplexWords)

    def demo(self):
#        text = "It is for us the living, rather,\
#                \nto be dedicated here to the unfinished\
#                \nwork which they who fought here have\
#                \nthus far so nobly advanced. It is\
#                \nrather for us to be here dedicated\
#                \nto the great task remaining before us,\
#                \nthat from these honored dead we take\
#                \nincreased devotion to that cause for which they\
#                \ngave the last full measure of devotion, that we\
#                \nhere highly resolve that these dead shall not have\
#                \ndied in vain, that this nation, under God, shall have a\
#                \nnew birth of freedom, and that government of the people, by\
#                \nthe people, for the people, shall not perish from this earth."
        text = ""
        print("The text : \n" + ("=" * 40))
        print(text)
        print(("=" * 40) + "\nHas the following statistics\n" + ("=" * 40))
        #nb = NaiveBayes()
        #ta = textanalyzer(nb.classifyText(text))

        f = open("../ressources/reiseberichtIndien.txt")
        raw_text = f.read()
        start_bookmark = raw_text.find("Erstes Kapitel")
        end_bookmark = raw_text.rfind("Im Verlag von R")
        text = raw_text[start_bookmark:end_bookmark]

        ta = textanalyzer(text)
        ta.analyzeText(text)
        pass
    demo = classmethod(demo)

def demo():
    textanalyzer.demo()

if __name__ == "__main__":
    textanalyzer.demo()







