

def CalcWordDiff (input_word):
    #Rating per category from 1(easy) to 5 (hard)

    #category word length (harder: longer words)
    result_word_length = word_length(input_word)
    print("Resultat Wortlaenge: " + str(result_word_length))
    #category letter combination (harder: word uses 'xy' or 'sch/ch')
    result_letter_combination = letter_combination(input_word)
    print("Resultat Buchstabenkombinationen: " + str(result_letter_combination))

    # Calculating overall score
    score = result_word_length+\
            result_letter_combination

    return score;



def letter_combination (input_word):
    input_word = input_word.lower()
    occurance = 0
    wl = len(input_word)
    # List with letter combination
    letter_combination_list = ['xy', 'yx', 'ph', 'f', 'sch', 'ch', 'th', 't', 'cks', 'x']
    for combination in letter_combination_list:
        occurance = occurance + input_word.count(combination)

    #weighted_score
    ws = occurance / wl
    if ws > 0.4:
        calc_value = 5
    elif ws > 0.3:
        calc_value = 4
    elif ws > 0.2:
        calc_value = 3
    elif ws > 0.1:
        calc_value = 2
    else:
        calc_value = 1
    return calc_value



def word_length (input_word):
    wl = len(input_word)
    if wl > 25:
        calc_value = 5
    elif wl > 15:
        calc_value = 4
    elif wl > 9:
        calc_value = 3
    elif wl > 4:
        calc_value = 2
    else:
        calc_value = 1
    return calc_value


def getNumberOfDifferentLetters(input_word):
    letterlist=""
    for i in range(0, len(input_word)):
        if not(input_word[i] in letterlist):
            letterlist+=input_word[i]

    if len(letterlist) == len(input_word):
        calc_value = 5
    elif len(letterlist) >= len(input_word)*0.8:
        calc_value = 4
    elif len(letterlist) >= len(input_word)*0.6:
        calc_value = 3
    elif len(letterlist) >= len(input_word)*0.4:
        calc_value = 2
    elif len(letterlist) >= len(input_word)*0.2:
        calc_value = 1

    return calc_value

def getNumberOfRepeatingLetters(input_word):
    count=0
    for i in range(0, len(input_word)):
        if(i!=0):
            if(input_word[i-1]==input_word[i]):
                count+=1
    if count >= 5:
        calc_value = 5
    elif count >= 3:
        calc_value = 3
    elif count >= 1:
        calc_value = 2
    elif count == 0:
        calc_value = 1

    return calc_value

def getNumberOfRareLetters(input_word):
    count = 0
    rareLetters = ['q', 'x', 'y', 'j', 'ß', 'v', 'p', 'z']

    for rareLetter in rareLetters:
        count += input_word.count(rareLetter)

    if count >= 4:
        calc_value = 5
    elif count >= 3:
        calc_value = 4
    elif count >= 2:
        calc_value = 3
    elif count == 1:
        calc_value = 2
    elif count == 0:
        calc_value = 1

    return calc_value

def getRatioVowelsConsonants(input_word):
    countVowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        countVowels += input_word.count(vowel)

    countConsonants = len(input_word)-countVowels

    ratio = countVowels/len(input_word)

    if ratio == 0 or ratio == 1:
        calc_value = 5
    elif ratio > 0.8:
        calc_value = 4
    elif ratio > 0.6:
        calc_value = 3
    elif ratio > 0.4:
        calc_value = 2
    elif ratio > 0 and ratio <= 0.4:
        calc_value = 1

    return calc_value





#test
print("overall Score: " + str(CalcWordDiff("Xylophon")))

# print("Difficulty: different letters: " + str(getNumberOfDifferentLetters("Xylophon")))
#
# print("Difficulty: repeating letters: " + str(getNumberOfRepeatingLetters("Xylophonn")))
#
# print("Difficulty: rare letters: " + str(getNumberOfRareLetters("Xylophon")))
#
# print("Difficulty: ratio vowels/consonants: " + str(getRatioVowelsConsonants("Xylophon")))