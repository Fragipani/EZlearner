__author__ = 'Rayk'

#Import from txt file
f = open("../ressources/reiseberichtIndien.txt")
raw_text = f.read().encode('utf-8')

#Buchtext definieren.
start_bookmark = raw_text.find("Erstes Kapitel")
end_bookmark = raw_text.rfind("Im Verlag von R")
text = raw_text[start_bookmark:end_bookmark]
print(text)