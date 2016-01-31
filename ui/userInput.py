# /usr/local/bin/python
# coding: latin-1

import nltk, string, os

from random import randint
from nltk.tag.stanford import StanfordPOSTagger

os.environ['CLASSPATH'] = '../ressources/standforPOS/stanford-postagger.jar'
os.environ['STANFORD_MODELS'] = '../ressources/standforPOS/models'

st = StanfordPOSTagger('german-hgc.tagger')

#tagset: http://www.coli.uni-saarland.de/projects/sfb378/negra-corpus/stts.asc



##############################
# Text importieren
##############################

f = open("../ressources/reiseberichtIndien.txt")
raw_text = f.read()
start_bookmark = raw_text.find("Erstes Kapitel")
end_bookmark = raw_text.rfind("Im Verlag von R")
text = raw_text[start_bookmark:end_bookmark]



##############################
#  Tokenization des Textes
##############################

tokens = nltk.word_tokenize(text, language='german')
sentence_tokens = nltk.sent_tokenize(text, language='german')

# Auswahl eines zufälligen Übungssatzes
randSentence = sentence_tokens[randint(0,len(sentence_tokens))]
randSentenceTokens = nltk.word_tokenize(randSentence, language='german')

# Auswahl des zu trainierenden Worttyps
pos_sentence = st.tag(randSentence.split())
print(pos_sentence)
response = input("Welche Wortart wollen Sie trainieren? (Verb, Nomen, Adjektiv, Artikel)")
if response == "Verb":
 picked_wordtype= "VAFIN"
elif response == "Nomen":
 picked_wordtype = "NN"
elif response == "Adjektiv":
 picked_wordtype = "ADJA"
elif response == "Artikel":
 picked_wordtype = "ART"
else:
 print("Nicht zugelassen")

# Ausgewählten Worttyp im Übungssatz finden
temp = list()
word_changed = None
for index, item1 in enumerate(pos_sentence):
 if (picked_wordtype == item1[1] and word_changed == None):
  index_of_picked_wordtype = index
  cutWord = item1[0]
  temp.append("____")
  word_changed = True
 else: temp.insert(index, item1[0])

#randNumberTokens = randint(0,len(randSentenceTokens))
#cutWord = randSentenceTokens[index_of_picked_wordtype]
#randSentenceTokens[index_of_picked_wordtype]='________'


# Ausgabe des Satzes mit Platzhalter
newSent ="".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in temp]).strip()
print("Satz: " + newSent)
#print("Lueckenwort: " + cutWord)


# Ermitteln aehnlicher Woerter mittels nltk-contextindex
text = nltk.Text(word.lower() for word in tokens)
idx = nltk.text.ContextIndex([word.lower( ) for word in tokens])
save = idx.similar_words(cutWord, n=3)
save.append(cutWord)

# Ausgabe moeglicher Altnerativwoerter
print("Moegliche Woerter:")
print(save)

# Input des Nutzers und Ergebnisauswertung
response = input("Fehlendes Wort eingeben: ")

if response == cutWord:
 print("Korrekt")
else:
 print("Falsch!!!!")



