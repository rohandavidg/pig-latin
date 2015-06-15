#!/usr/bin/env python2.7


import sys

vowels = ['a','e','i','o','u', 'y']
constonants = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
               

def main():
    input = sys.argv[1:]
    list = input[0].split()
    output_word = []
    for word in list:
        new_prefix, prefix = get_prefix(vowels, word)
        pig_latin_word = get_stem_prefix(word, new_prefix,  prefix)
        output_word.append(pig_latin_word)
    print " ".join(output_word)

def get_prefix(vowels, word):
    new_word = []
    if len(word) == 1:
        new_prefix = word + "yay"
        return new_prefix
    else:    
        for letter in word:
            if letter in vowels:
                break
            new_word.append(letter)
    prefix = "".join(new_word)
    return prefix

def get_stem_prefix(word, new_prefix, prefix):
    list_word = word.split(prefix)
    suffix = list_word[1]
    new_word = suffix + prefix
    pig_latin_word = new_word + "ay"
    return pig_latin_word


if __name__ == "__main__":
    main()



