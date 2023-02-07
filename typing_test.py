""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5

def lines_from_file(path):
    open_path = open(path)
    return [a.strip('\n').strip() for a in readlines(open_path)]

def new_sample(path,i):
    return lines_from_file(path)[i]


def analyze(sample_paragraph, typed_string, start_time, end_time):
    def words_per_min(typed_string, start_time, end_time):
        number_of_characters = len(typed_string)
        num_words = number_of_characters / 5
        rate = (num_words) / (end_time - start_time) 
        return rate * 60



    def accuracy(sample_paragraph, typed_string):
        sample = split(sample_paragraph)
        typed = split(typed_string)
        total = 0.0
        short_word=min(len(sample),len(typed))
        if min(len(sample),len(typed))== 0:
            return float(0)
        if len(sample) >= len(typed):
            shorter_string = typed_string
        for index in range(short_word):
            if sample[index] == typed[index]:
                total += 1
        return (total / short_word) * 100.0
    return [words_per_min(typed_string, start_time, end_time), accuracy(sample_paragraph, typed_string)]
vowel = ["a", "e", "i", "o", "u"]
def check_vowels(word):
    for i in word:
        if i in vowel:
            return True
    return False

def find_first_vowel(word):
    for i in range(len(word)):
        if word[i] in vowel:
            return i



def pig_latin(word):
    if check_vowels(word) == False:
        return word + "ay"
    elif word[0] in vowel:
        return word + "way"
    else:
        return word[find_first_vowel(word):]+ word[0:find_first_vowel(word)] + "ay"

def autocorrect(user_input,word_list,score_function):
    if user_input in word_list:
        return user_input
    return min(word_list,key = lambda a: score_function(user_input,a))

            
def swap_score(first_word,second_word):
    if first_word == "" or second_word == "":
        return 0
    if first_word[0] != second_word[0]:
        return 1 + swap_score(first_word[1:],second_word[1:])
    return swap_score(first_word[1:],second_word[1:])



                

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    if word1 == "" or word2 == "": # Fill in the condition
        # BEGIN Q6
        return max([len(word1),len(word2)])
        # END Q6

    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        return score_function(word1[1:],word2[1:])

        # BEGIN Q6
        
        # END Q6
    
    else:
        add_char = 1 + score_function(word1,word2[1:]) # Fill in these lines
        remove_char = 1 + score_function(word1[1:],word2)
        substitute_char = 1 + score_function(word1[1:],word2[1:])
        # BEGIN Q6
        return min([add_char,remove_char,substitute_char])
    """
  
"""

KEY_DISTANCES = get_key_distances()


# BEGIN Q7-8

def score_function_accurate(word1,word2):
    if (word1,word2) in my_memos or (word2,word1) in my_memos:
        return my_memos[word1,word2]
    else:
        if word1 == "" or word2 == "": # Fill in the condition
            return max([len(word1),len(word2)])
        
        elif word1[0] == word2[0]: # Feel free to remove or add additional cases
            return score_function_accurate(word1[1:],word2[1:])       
        else:
            add_char = 1 + score_function_accurate(word1,word2[1:]) # Fill in these lines
            remove_char = 1 + score_function_accurate(word1[1:],word2)
            substitute_char = KEY_DISTANCES[word1[0],word2[0]] + score_function_accurate(word1[1:],word2[1:])
            return min([add_char,remove_char,substitute_char])

my_memos={}
def score_function_final(word1,word2):
    if word1 == "" or word2 == "": # Fill in the condition
        return max([len(word1),len(word2)])
    elif (word1,word2) in my_memos:
        return my_memos[(word1,word2)]
    elif (word2,word1) in my_memos:
        return my_memos[(word2,word1)]
    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        return score_function_final(word1[1:],word2[1:])       
    else:
        add_char = 1 + score_function_final(word1,word2[1:]) # Fill in these lines
        remove_char = 1 + score_function_final(word1[1:],word2)
        substitute_char = KEY_DISTANCES[word1[0],word2[0]] + score_function_final(word1[1:],word2[1:])
        my_memos[(word1,word2)] = min([add_char,remove_char,substitute_char])
        return min([add_char,remove_char,substitute_char])
# END Q7-8
