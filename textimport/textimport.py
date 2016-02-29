import nltk, pickle

#Import from txt file
f = open("../ressources/tisch.txt")
raw_text = f.read()

# create new tokens from import and append these tokens to existing token list
raw_tokens = nltk.word_tokenize(raw_text, language='german')
sentence_tokens = nltk.sent_tokenize(raw_text, language='german')
del_list = [',','.',':',';']
new_tokens = [token for token in raw_tokens if token not in del_list]
old_tokens = pickle.load(open("../ressources/tokens.pickle", "rb"))
old_tokens.extend(new_tokens)

#Save newly created token list
pickle.dump(new_tokens ,open("../ressources/tokens.pickle", "wb"))
pickle.dump(sentence_tokens ,open("../ressources/sentenceTokens.pickle", "wb"))

#Do frequency distribution of current token list
freqdistr = nltk.FreqDist(new_tokens)
pickle.dump(freqdistr, open("../ressources/freqdistr.pickle", "wb"))

