# Cracking the Coding Interview: 17.11
# Written by Josh Humphrey
from collections import defaultdict
import math

def read_book(file_name):
    bad_chars = {',','.',';',':','"','\''}
    book_array = []
    with open(file_name,'r') as f:
        for line in f:
            for word in line.split():
                for special in bad_chars:
                    new_word = word.replace(special,"")
                book_array.append(new_word)

    return book_array

def pre_computation(arr):
    wordmap = defaultdict(list)
    for i in range(len(arr)):
        key = arr[i]
        wordmap[key].append(i)
    return wordmap

def find_word_relation(word1, word2, wordmap):
    indices1 = wordmap[word1]
    indices2 = wordmap[word2]
    result = math.inf
    result_ind = [None, None]
    for i1 in range(len(indices1)):
        for i2 in range(len(indices2)):
            temp = abs(indices1[i1]-indices2[i2])
            if temp < result:
                result = temp
                result_ind = [i1, i2]
    return result_ind



shakespeare_array = read_book("Shakespeare.txt")
wordmap = pre_computation(shakespeare_array)
res1 = find_word_relation("Pupper", "Thee", wordmap)
res2 = find_word_relation("We", "Need", wordmap)
res3 = find_word_relation("Romeo", "Juliet", wordmap)
print("Pupper and Thee: " + str(res1) + ", Art and Thou: " + str(res2) + ", Romeo and Juliet: " + str(res3))
