#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys,os
import csv

SCORE_MIN = 1
SCORE_MAX = 5

def read_input(file):
    with open(file) as myFile:  
        reader = csv.reader(myFile)
        #index for score, text
        idx_score = 0
        idx_text = 2
        idx = [idx_score,idx_text] 
        for row in reader:
            yield([row[x] for x in idx]) #ignore summary
def mapper(k_max):
    # input comes from result.csv in the same directory
    input_file = 'result.csv'
    # for testing and debug purpose
    input_file = 'sample.csv'
    data = read_input(os.path.join(os.path.dirname(os.path.abspath(__file__)), input_file))
    
    idx_score = 0
    idx_text = 1
    valid_scores = [str(x) for x in range(SCORE_MIN,SCORE_MAX+1)]

    for record in data:
        score = record[idx_score]
        
        #skip the record if score is not valid
        if score not in valid_scores:
            continue
        else:
            score = int(score) #cast score to integer

        #process words in text in the record    
        word_list = [x.strip() for x in record[idx_text].split(" ") if x.strip() != ""]#non-empty words
        text_len = len(word_list) #number of words of the text
        k_len = min(text_len,k_max) #in case number of words < k_max
        k_min = 1

        #for k = 1 to k_len 
        #e.g. 1 to 5
        for k in range(k_min, k_len+1):
            for idx in range(0, text_len-k+1):
                #score, k-length, k-shingle, count
                yield (score, k, ' '.join(word_list[idx:idx+k]), 1) 
 


