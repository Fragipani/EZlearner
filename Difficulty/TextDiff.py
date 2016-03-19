import nltk, Difficulty.SentenceDiff as diff

def calcTextDiff (text):
    sentence_tokens = nltk.sent_tokenize(text, language='german')

    sentDifficulty = 0
    hardSent = 0
    for sent in sentence_tokens:
        score = diff.calcSentenceDiff(sent)
        if(score) >= 3.5:
            hardSent+=1

    if hardSent / len(sentence_tokens) >= 0.5:
        result = 5
    elif hardSent / len(sentence_tokens) >= 0.3:
        result = 4
    elif hardSent / len(sentence_tokens) >= 0.2:
        result = 3
    elif hardSent / len(sentence_tokens) >= 0.1:
        result = 2
    else:
        result = 1

    return result

# interessanter link https://de.wikipedia.org/wiki/Lesbarkeitsindex