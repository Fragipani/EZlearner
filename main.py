import pickle, os
from Difficulty.TextDiff import calcTextDiff
from readabilityIndex.ReadabilityTool import ReadabilityTool


class Main:

    def printIndex(self, newText):
        index = ReadabilityTool()
        index.getIndex(newText)
        print("Custom Score: " + str(calcTextDiff(newText)))


print("Willkommen bei EZLearner! Berechnen Sie die Schwierigkeit eines Textes.")
print("1: Eigenen Text eingeben")
print("2: Bestehenden Text analysieren")
print("3: Neuen Text hochladen")
print("4: Beenden")
response = input("Auswahl:")

main = Main()
projectRoot = os.path.dirname(os.path.dirname(__file__))

newText = ""
if response == "1":
    newText = input()
    main.printIndex(newText)
elif response == "2":
    newText = pickle.load(open(projectRoot + "/EZLearner/ressources/tisch.pickle", "rb"))
    main.printIndex(newText)
    #Todo: Auswahl eines bestehenden Texts
elif response == "3":
    newText = input()
    #Todo: Auswahl eines bestehenden Texts
elif response == "4":
    print("Auf Wiedersehen")
    #Todo: Nichts machen. Einfach beenden
else:
 print("Falsche Eingabe")