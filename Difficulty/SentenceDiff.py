import nltk, pickle, os, statistics
from random import randint
from Difficulty.WordDiff import CalcWordDiff
from nltk.tag.stanford import StanfordPOSTagger

os.environ['CLASSPATH'] = '../ressources/standforPOS/stanford-postagger.jar'
os.environ['STANFORD_MODELS'] = '../ressources/standforPOS/models'

st = StanfordPOSTagger('german-hgc.tagger')

def calcSentenceDiff (Sentence):
    return

def getSentenceLength(sentenceTokens):
    #Todo: remove stopwords??
    return len(sentenceTokens)

def getPosRank(sentence):
# 
    pos_sentence = st.tag(sentence)

    return pos_sentence

def getWordDifficulty (sentenceTokens):
    WordDiffList = list()
    for item in sentenceTokens:
        WordDiffList.append(CalcWordDiff(item))
    sum(WordDiffList)
    statistics.mean(WordDiffList)
    statistics.pstdev(WordDiffList)
    statistics.pvariance(WordDiffList)
    return


#test

# sentence_tokens = pickle.load(open("../ressources/sentenceTokens.pickle", "rb"))
# randSentence = sentence_tokens[randint(0,len(sentence_tokens))]
# randSentenceTokens = nltk.word_tokenize(randSentence, language='german')

randSentenceTokens = ['Ihr', 'Haupt', 'verdunkelte', 'die', 'Ampel', ',', 'so', 'daß', 'ihre', 'Gestalt', 'in', 'magischen', 'Lichträndern', 'glomm', '.']
#randSentenceTokens = ['Er', 'hat', 'das', 'mit', '"', 'I', 'love', 'you', '"', 'übersetzt']
print(randSentenceTokens)
print("Sentence length: " + str(getSentenceLength(randSentenceTokens)))

print(getWordDifficulty(randSentenceTokens))