#!/usr/bin/env python3

def return_evens(num_list):
    pass
    return [item  for item in num_list if item%2==0]

def make_exclamation(sentence_list):
    pass
    return [item+"!" for item in sentence_list]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))