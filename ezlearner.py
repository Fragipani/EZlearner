__author__ = 'Rayk, Thomas'

import urllib.request, nltk


# Import zufaellig ausgesuchter DE Text
#url = "http://www.gutenberg.org/cache/epub/24377/pg24377.txt"
#response = urllib.request.urlopen(url)
#raw_text = response.read().decode('UTF-8')

#Import from txt file
f = open("ressources/reiseberichtIndien.txt")
raw_text = f.read()
print(raw_text)

#Buchtext definieren.
#start_bookmark = raw_text.find("Erstes Kapitel")
#end_bookmark = raw_text.rfind("Im Verlag von R")
#text = raw_text[start_bookmark:end_bookmark]

#Saetze tokenizieren
#sentence_tokens = nltk.sent_tokenize(text)
#print(sentence_tokens)
# warum ist die Liste sentence_tokens leer? In der Console nicht...
# Umgang mit Umlauten