# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:10:55 2019

@author: krado
"""
import math

class TextModel():
    def __init__(self, model_name):
        """initializes text model with name and empty dictionaries"""
        self.name = model_name
        self.words ={}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        
    def __repr__(self):
        """prints out the model name and the lengths of each dictionary"""
        t = 'text model name: ' + self.name + '\n'
        t += '  number of words: ' + str(len(self.words)) + '\n'
        t += '  number of word lengths: ' + str(len(self.word_lengths)) +'\n'
        t += '  number of stems: ' + str(len(self.stems)) + '\n'
        t += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        t += '  number of punctuation: ' + str(len(self.punctuation))

        return t
    
    def add_string(self, s):
        """updates the dictionaries based on the string input"""
        cur_count = 1
        for char in s:
            if char == ' ':
                cur_count += 1
            if (char == '.' or char == '?' or char == '!'):
                if cur_count not in self.sentence_lengths:
                    self.sentence_lengths[cur_count] = 1
                else:
                    self.sentence_lengths[cur_count] += 1
                cur_count =0   
        
        
        
        
                if char not in self.punctuation:
                    self.punctuation[char] = 1
                else:
                    self.punctuation[char] += 1
                
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
                
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] +=1
                
            w_stem = stem(w)
            if w_stem not in self.stems:
                self.stems[w_stem] = 1
            else:
                self.stems[w_stem] += 1
            
            
            
    def add_file(self, filename):
        """takes a file and updates the content of the dictionaries based on the file's content"""
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        txt = file.read()
        file.close()
        self.add_string(txt)
        
    def save_model(self):
        """takes the dictionaries and saves them to new files"""
        words = self.name + '_' + 'words'
        f= open(words, 'w')
        f.write(str(self.words))
        f.close()
        
        word_lengths = self.name+'_'+'word_lengths'
        f= open(word_lengths, 'w')
        f.write(str(self.word_lengths))
        f.close()
        
        sentences = self.name + '_' + 'sentence_lengths'
        f = open(sentences, 'w')
        f.write(str(self.sentence_lengths))
        f.close()
        
        stems = self.name + '_' +'stems'
        f = open(stems, 'w')
        f.write(str(self.stems))
        f.close()
        
        puncuation = self.name + '_' + 'punctuation'
        f = open(puncuation, 'w')
        f.write(str(self.punctuation))
        f.close()
        
    def read_model(self):
        """takes files with dictionaries and saves them to the respective atributes"""
        words = self.name + '_' + 'words'
        f = open(words, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.words = d
        
        word_lengths = self.name+'_'+'word_lengths'
        f = open(word_lengths, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.word_lengths = d
        
        sentences = self.name + '_' + 'sentence_lengths'
        f= open(sentences, 'r')
        d_str = f.read()
        f.close()
        d= dict(eval(d_str))
        self.sentence_lengths = d
        
        stems = self.name + '_' +'stems'
        f = open(stems,'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.stems = d
        
        puncuation = self.name + '_' + 'punctuation'
        f = open(puncuation, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.punctuation = d
        
    def similarity_scores(self, other):
         word_score = compare_dictionaries(other.words, self.words)
         sentence_length_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
         word_length_score = compare_dictionaries(other.word_lengths, self.word_lengths)
         stem_score = compare_dictionaries(other.stems, self.stems)
         punctuation_score = compare_dictionaries(other.punctuation, self.punctuation)
         return [word_score, word_length_score, stem_score, sentence_length_score, punctuation_score]
     
    def classify(self, source1, source2):
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ' ' + str(scores1))
        print('scores for ' + source2.name + ' ' + str(scores2))
        
        weight =0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                weight += 1
            else:
                weight -=1
                
        if weight >0:
            print(self.name +' is more likely to have come from ' + source1.name)
        else:
            print(self.name +' is more likely to have come from ' + source2.name)
        
        
def clean_text(txt):
    """removes punctuation from the text and makes everything lower case"""
    txt = txt.lower()
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('!', '')
    txt = txt.replace('?', '')
    txt = txt.split()
    
    return txt

def stem(s):
    if s == 'the':
        return s
    
    if s[-1] == 's' and len(s) >1:
        s = stem(s[:-1])
    elif s[-3:] == 'ing' and len(s) > 5:
        if s[-4] == s[-5]:
            s = stem(s[:-4])
        else:
            s = stem(s[:-3])
    elif s[-2:] == 'er' and len(s) >3:
        if s[-3] == s[-4]:
            s = stem(s[:-3])
        else:
            s = stem(s[:-2])
    elif s[-2:] == 'ed' and len(s)>2:
        s = stem(s[:-2])
    elif s[-4:] == 'ment' and len(s) > 4:
        s = stem(s[:-4])
    elif s[-4:] == 'ness' and len(s) >4:
        s = stem(s[:-4])
    elif s[-4:] == 'less' and len(s) >4:
        s = stem(s[:-4])
    elif s[-2:] == 'ly' and len(s) >2:
        s = stem(s[:-2])
            
        
    if s[-1] == 'e' and len(s) >1:
        s = s[:-1]
    if s[-1] == 'y' and len(s) >1:
        s = s[:-1] + 'i'
    return s


def compare_dictionaries(d1, d2):
    score = 0
    total = 0
    for key in d1:
        total += d1[key]
          
    for key in d2:
        if key in d1:
            score  += d2[key] * math.log(d1[key]/total)
        else:
            score += d2[key] * math.log(.5/total)

    return score

def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.

def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)
    
    
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
    
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('nytimes')
    source1.add_file('nytimes.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('Shakespeare.txt')

    new1 = TextModel('wr120')
    new1.add_file('wr120.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('boston globe')
    new2.add_file('bostonglobe.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('christmas carol')
    new3.add_file('christmascarol.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('family guy')
    new4.add_file('familyguy.txt')
    new4.classify(source1, source2)