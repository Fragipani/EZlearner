import pickle, os
from Difficulty.WordDiff import calcWordDiff
from Difficulty.SentenceDiff import calcSentenceDiff
from Difficulty.TextDiff import calcTextDiff
from readabilityIndex.ReadabilityTool import ReadabilityTool

projectRoot = os.path.dirname(os.path.dirname(__file__))

print("Willkommen bei EZLearner! Berechnen Sie die Schwierigkeit eines Textes.")
print("1: Eigenen Text eingeben")
print("2: Bestehenden Text analysieren")
print("3: Neuen Text hochladen")
print("4: Beenden")
response = input("Auswahl:")

newText = ""
if response == "1":
    newText = input()
elif response == "2":
    newText = pickle.load(open(projectRoot + "/EZLearner/ressources/tisch.pickle", "rb"))
    #Todo: Auswahl eines bestehenden Texts
elif response == "3":
    newText = input()
    #Todo: Auswahl eines bestehenden Texts
elif response == "4":
    newText = "blabla"
    #Todo: Nichts machen. Einfach beenden
else:
 print("Falsche Eingabe")


index = ReadabilityTool()
index.getIndex(newText)

print("Custom Score: " + str(calcTextDiff(newText)))
