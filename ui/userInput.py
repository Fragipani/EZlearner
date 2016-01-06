
import nltk, string, os

from random import randint
from nltk.tag.stanford import StanfordPOSTagger

os.environ['CLASSPATH'] = '../ressources/standforPOS/stanford-postagger.jar'
os.environ['STANFORD_MODELS'] = '../ressources/standforPOS/models'

st = StanfordPOSTagger('german-hgc.tagger')

#tagset: http://www.coli.uni-saarland.de/projects/sfb378/negra-corpus/stts.asc



#Import from txt file

f = open("../ressources/reiseberichtIndien.txt")
raw_text = f.read()
#print(raw_text)

#Buchtext definieren.
start_bookmark = raw_text.find("Erstes Kapitel")
end_bookmark = raw_text.rfind("Im Verlag von R")
text = raw_text[start_bookmark:end_bookmark]


tokens = nltk.word_tokenize(text, language='german')
sentence_tokens = nltk.sent_tokenize(text, language='german')

randSentence = sentence_tokens[randint(0,len(sentence_tokens))]

randSentenceTokens = nltk.word_tokenize(randSentence, language='german')



print(st.tag(randSentence.split()))

randNumberTokens = randint(0,len(randSentenceTokens))
cutWord = randSentenceTokens[randNumberTokens]
randSentenceTokens[randNumberTokens]='________'



newSent ="".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in randSentenceTokens]).strip()
print("Satz: " + newSent)

#print("Lueckenwort: " + cutWord)

text = nltk.Text(word.lower() for word in tokens)



idx = nltk.text.ContextIndex([word.lower( ) for word in tokens])

save = idx.similar_words(cutWord, n=3)
save.append(cutWord)

print("Moegliche Woerter:")
print(save)

response = input("Fehlendes Wort eingeben: ")

if response == cutWord:
 print("Korrekt")
else:
 print("Falsch!!!!")



