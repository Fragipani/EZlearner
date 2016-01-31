from readabilityIndex.textanalyzer import *
import math

# http://web.mit.edu/6.863/spring2010/python/nltk_contrib/readability/readabilitytests.py

class ReadabilityTool:

    analyzedVars = {}
    text = ""
    lang = ""

    def __analyzeText(self, text=''):
        if text != '':
            if text != self.text:
                self.text = text
                t = textanalyzer()
                t.analyzeText(text)
                words = t.getWords(text)
                charCount = t.getCharacterCount(words)
                wordCount = len(words)
                sentenceCount = len(t.getSentences(text))
                complexwordsCount = t.countComplexWords(text)
                averageWordsPerSentence = wordCount/sentenceCount

                analyzedVars = {}

                analyzedVars['words'] = words
                analyzedVars['charCount'] = float(charCount)
                analyzedVars['wordCount'] = float(wordCount)
                analyzedVars['sentenceCount'] = float(sentenceCount)
                analyzedVars['complexwordCount'] = float(complexwordsCount)
                analyzedVars['averageWordsPerSentence'] = float(averageWordsPerSentence)
                self.analyzedVars = analyzedVars



    def ARI(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = 4.71 * (analyzedVars['charCount'] / analyzedVars['wordCount']) + 0.5 * (analyzedVars['wordCount'] / analyzedVars['sentenceCount']) - 21.43
        return score

    def GunningFogIndex(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = 0.4 * ((analyzedVars['averageWordsPerSentence']) + (100 * (analyzedVars['complexwordCount']/analyzedVars['wordCount'])))
        return score

    def SMOGIndex(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = (math.sqrt(analyzedVars['complexwordCount']*(30/analyzedVars['sentenceCount'])) + 3)
        return score

    def ColemanLiauIndex(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = (5.89*(analyzedVars['charCount']/analyzedVars['wordCount']))-(30*(analyzedVars['sentenceCount']/analyzedVars['wordCount']))-15.8
        return score

    def LIX(self, text = ''):
        self.__analyzeText(text)
        analyzedVars = self.analyzedVars
        score = 0.0
        longwords = 0.0
        for word in analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = analyzedVars['wordCount'] / analyzedVars['sentenceCount'] + float(100 * longwords) / analyzedVars['wordCount']
        return score

    def RIX(self, text = ''):
        self.__analyzeText(text)
        analyzedVars = self.analyzedVars
        score = 0.0
        longwords = 0.0
        for word in analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = longwords / analyzedVars['sentenceCount']
        return score


    def getReportAll(self, text = ''):
        self.__analyzeText(text)
        ari = 0.0
        gunningFog = 0.0
        smog = 0.0
        coleman = 0.0

        ari = self.ARI()
        gunningFog = self.GunningFogIndex()
        smog = self.SMOGIndex()
        coleman = self.ColemanLiauIndex()
        lix = self.LIX()
        rix = self.RIX()

        print('*' * 70)
        print(' ARI: %.1f' % ari)
        print(' Gunning Fog: %.1f' % gunningFog)
        print(' SMOG Index: %.1f' % smog)
        print(' Coleman-Liau Index: %.1f' % coleman)
        print(' LIX : %.1f' % lix)
        print(' RIX : %.1f' % rix)
        print('*' * 70)

        print("=" * 100)



    def demo(self):
        self = ReadabilityTool()
        f = open("../ressources/reiseberichtIndien.txt")
        raw_text = f.read()
        start_bookmark = raw_text.find("Erstes Kapitel")
        end_bookmark = raw_text.rfind("Im Verlag von R")
        text = raw_text[start_bookmark:end_bookmark]


        self.__analyzeText(text)
        self.getReportAll(text)
    demo = classmethod(demo)


def demo():
    ReadabilityTool.demo()

if __name__ == "__main__":
    ReadabilityTool.demo()












