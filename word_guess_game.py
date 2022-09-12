 
MAX_GUESS_TIMES = 10
  
def filterByPattern(pattern , word_list):
    
    count = len(pattern)
    word_dict = []
    for word in word_list:
        if(len(word) == count):
            word_dict.append(word)
   
    return word_dict

def getPatternLetters(pattern):
    letters={''}
    split_pattern = pattern.split("_")
    for c in split_pattern:
        if(c !=''):
            letters.add(c)
    letters.remove('')
    return letters
    
def getPatternLettersIndexes(pattern):
    
    pattern_letters = getPatternLetters(pattern)
    letter_data_dict = []
    for c in pattern_letters:
        data_index = getWordLetterIndexes(c, pattern)
        letter_data_dict.append(data_index)
            
    return letter_data_dict


def getWordLetterIndexes(ch, word):
    letter_data_dict = []
    i=0
    for c in word:
        if( c == ch):
            letter_data_dict.append(i)
        i = i+1  
    data_dict = {
        "letter": ch,
        "positions": letter_data_dict
        } 
    return data_dict       


def findMultiMatchFromPattern(pattern, word_list):
    
    filtered_word_list = filterByPattern(pattern,word_list)
    letter_data =  getPatternLettersIndexes(pattern)
    matched_words = []
    containAll = True
    for ch in letter_data:
        for word in filtered_word_list: 
            for index in ch["positions"]:
                if word[index] != ch["letter"]:
                    containAll = False
    
            if containAll == True:
                matched_words.append(word)
    
    return matched_words

guesses = ''
def guess_next_letter(pattern, used_letters, word_list):
    global guesses
    final_list = []
    multi_result_list = findMultiMatchFromPattern(pattern, word_list)
    letter_length = {}
     
    if len(used_letters) != 0:
        if len(used_letters) > MAX_GUESS_TIMES:
            guesses = 'Out to times, challenge failed !'
            return guesses
        letters_count = []
        for word in multi_result_list:
            word_counts = getWordLetterIndexes(used_letters[0], word)
            if len(word_counts['positions']) != 0:
                letters_count.append(word_counts)
                letter_length[word] = len(word_counts['positions']) 
    
        if len(letter_length) !=0:
            dictionary_keys = list(letter_length.keys())
            sorted_dict = {dictionary_keys[i]: sorted(letter_length.values())[i] for i in range(len(dictionary_keys))}
            sorted_dict_keys = list(sorted_dict.keys())
            
            result_word = sorted_dict_keys[-1]
            final_list.append(result_word)
            result_pattern = replaceLetterToWord(used_letters[0],result_word, pattern)
            guesses = result_pattern
            guess_next_letter(result_pattern,used_letters[1:],final_list )
            #return guesses
        else:
            if(len(final_list)!=0):
                guess_next_letter(guesses,used_letters[1:],final_list )
            else:
                guess_next_letter(pattern,used_letters[1:],multi_result_list )       
        
    return guesses   

def replaceLetterToWord(used_letters, word, pattern):
    for  ch in used_letters:
        indexes = getWordLetterIndexes(ch, word)
       
        if len(indexes['positions']) != 0:
            for index in indexes['positions']:
                pattern = pattern[:index]+ch+pattern[index+1:]
            
    return pattern
    
   
def checkDictValuesAreEqual(words):
    x = list(words.values())
    r = False
    if(x.count(x[0]) == len(x)):
        r = True
    return r


def test_function_should_return_something():
    
    pattern = "_______e"
    used_letters = list("ipilkbeog")
    word_list=['about', 'abound', 'program', 'increase', 'eligible', 'generously', 'letter', 'strategy', 'implementation', 'public', 'intelligent']

    assert guess_next_letter(pattern, used_letters, word_list) is not None


if __name__ == '__main__':
    
    result = ''
    word_list=['about', 'abound', 'program', 'increase', 'eligible', 'generously', 'letter', 'strategy', 'implementation', 'public', 'intelligent']
    
    print(filterByPattern("______", word_list))
    
    data = getWordLetterIndexes('t', "title")
    print(data)
   
    pattern = "____e".split("_")
    print(pattern)
    print(getPatternLettersIndexes("___t_o__p__t___"))
    print(getPatternLetters("___t_o__p__t___"))
    print(findMultiMatchFromPattern("_______e", word_list))
    print(guess_next_letter("_______e", "ipilkbeog", word_list))
    
    
    test_function_should_return_something()
    
    
