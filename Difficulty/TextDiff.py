import nltk, Difficulty.SentenceDiff as diff

def calcTextDiff (text):
    sentence_tokens = nltk.sent_tokenize(text, language='german')

    sentDifficulty = 0
    for sent in sentence_tokens:
        sentDifficulty += diff.calcSentenceDiff(sent)
    return sentDifficulty / len(sentence_tokens)


# interessanter link https://de.wikipedia.org/wiki/Lesbarkeitsindex