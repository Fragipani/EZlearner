import nltk, pickle, os, statistics
from random import randint
from Difficulty.WordDiff import calcWordDiff
from nltk.tag.stanford import StanfordPOSTagger

projectRoot = os.path.dirname(os.path.dirname(__file__))

os.environ['CLASSPATH'] = projectRoot + '/ressources/standforPOS/stanford-postagger.jar'
os.environ['STANFORD_MODELS'] = projectRoot + '/ressources/standforPOS/models'
os.environ['JAVA_HOME'] = "C:\\Program Files\\Java\\jdk1.8.0_66\\bin"
st = StanfordPOSTagger('german-hgc.tagger')

def calcSentenceDiff (sentence):
    raw_words = nltk.word_tokenize(sentence, language='german')
    del_list = [',','.',':',';','!','?']
    words = [token for token in raw_words if token not in del_list]

    score = (2*getSentenceLength(words)+\
            1*getPosRank(sentence)+\
            3*getWordDifficulty(words))/6

    return score

def getSentenceLength(sentenceTokens):
    #Todo: remove stopwords??
    if len(sentenceTokens) >= 30:
        calc_value = 5
    elif len(sentenceTokens) >= 20:
        calc_value = 4
    elif len(sentenceTokens) >= 10:
        calc_value = 3
    elif len(sentenceTokens) >= 5:
        calc_value = 2
    else:
        calc_value = 1
    return calc_value

def getPosRank(sentence):
    # Definition of POS Container
    adjektive = ['ADJA', 'ADJD', 'PAV']
    praepositionen = ['ADV', 'APPR', 'APPRART', 'APPO', 'APZR']
    # weiteres = ['Art', 'CARD', 'FM', 'ITJ', 'ORD', 'PTKNEG', 'PTKANT', 'PTKA', 'SGML', 'SPELL', 'TRUNC', 'XY', '$,', '$.', '$(']
    nomen_Eigenwörter = ['NN', 'NE']
    pronomen = ['PDS', 'PDAT', 'PIS', 'PIAT', 'PIDAT', 'PPER', 'PPOSS', 'PPOSAT', 'PRELS', 'PRELAT', 'PRF', 'PWS', 'PWAT', 'PWAV']
    verben_konjugationen = ['KOUI', 'KOUS', 'KON', 'KOKOM', 'PTKZU', 'PTKVZ', 'VVFIN', 'VVIMP', 'VVINF', 'VVIZU', 'VVPP', 'VAFIN', 'VAIMP', 'VAINF', 'VAPP', 'VMFIN', 'VVINF', 'VMPP']
    # Reset
    adj=0
    pra=0
    wei=0
    nom=0
    pro=0
    ver=0
    # Counting occurences of Containers in sentence
    pos_sentence = st.tag(sentence)
    for count_pos_tags in pos_sentence:
        if count_pos_tags[1] in adjektive:
            adj=adj+1
        if count_pos_tags[1] in praepositionen:
            pra=pra+1
        if count_pos_tags[1] in nomen_Eigenwörter:
            nom=nom+1
        if count_pos_tags[1] in pronomen:
            pro=pro+1
        if count_pos_tags[1] in verben_konjugationen:
            ver=ver+1
        else:
            wei=wei+1

    #Weighted occurence of containers
    adjpercent = adj / len(pos_sentence)
    prapercent = pra / len(pos_sentence)
    nompercent = nom / len(pos_sentence)
    propercent = pro / len(pos_sentence)
    verpercent = ver / len(pos_sentence)
    weipercent = 1 - adjpercent - prapercent - nompercent - propercent - verpercent

    #Compare sentence with preset values to indicate if this is a not usual sentence
    deviation=0
    if 0.05 < adjpercent < 0.15:
        deviation=deviation+1
    if 0.1 < prapercent < 0.2:
        deviation=deviation+1
    if 0.25 < nompercent < 0.35:
        deviation=deviation+1
    if 0.1 < propercent < 0.2:
        deviation=deviation+1
    if 0.5 < verpercent < 1.5:
        deviation=deviation+1
    if 0.15 < weipercent < 0.25:
        deviation=deviation+1

    if deviation == 6:
        calc_value = 5
    elif deviation == 5:
        calc_value = 4
    elif deviation == 4:
        calc_value = 3
    elif deviation == 3:
        calc_value = 2
    elif deviation <= 2:
        calc_value = 1

    return calc_value

def getWordDifficulty (sentence):
    # satzzeichen?

    easyList = list()
    middelList = list()
    hardList = list()
    completeList = list()
    for item in sentence:
        score = calcWordDiff(item)
        completeList.append(score)
        if(score<2): easyList.append(score)
        elif(score<=2.5): middelList.append(score)
        else: hardList.append(score)

    #if(len(hardList)/len(words) > 0.1): result = statistics.mean(hardList)
    #else: result = statistics.mean(completeList)

    if len(hardList) >= 4:
        result = 5
    elif len(hardList) >= 3:
        result = 4
    elif len(hardList) >= 2:
        result = 3
    elif len(hardList) >= 1:
        result = 2
    else: result = 1

    return result
