

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



#test
print("overall Score: " + str(CalcWordDiff("Xylophon")))
