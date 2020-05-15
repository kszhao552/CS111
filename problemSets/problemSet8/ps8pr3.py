# ps8pr3*-

#Markov first order program

"""
Created on Fri Nov 15 15:26:43 2019

@author: krado
"""
import random

def create_dictionary(filename):
    """creates a dictionary from a text file containing words
    the dictionary comprises of the each word as the key and the words that follow it as the definition"""
    file = open(filename, 'r')
    text = file.read()     
    file.close()
    
    words = text.split()
    dic = {}
    
    for word_ind in range(len(words)):
        cur_word = words[word_ind]
        prev_word = words[word_ind -1]       
        if prev_word[-1] == '.' or prev_word[-1] == '?' or prev_word[-1] =='!':
            prev_word = '$'
        
        if prev_word not in dic:
            dic[prev_word] = [cur_word]
        else:
            dic[prev_word] +=  [cur_word]
    return dic
            

def generate_text(word_dict, num_words):
    """creates a randomly generated paragraph of an input length from a dictionary of words"""
    cur_word = '$'
    wordlist = word_dict[cur_word]
    next_word = random.choice(wordlist)
    text = next_word + ' '
    for i in range(num_words-1):
        cur_word = next_word
        wordlist = word_dict[cur_word]
        next_word = random.choice(wordlist)
        text += (next_word + ' ')
        if next_word not in word_dict or next_word[-1] == '.' or next_word[-1] == '?' or next_word[-1] == '!':
            next_word = '$'
            
    print(text)