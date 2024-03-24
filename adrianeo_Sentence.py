"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-26-2024
Homework Problem # 6_Sentence
Description of Problem: A class for evaluating and manipulating English
sentences.
"""

import re
import random


def _remove_punctuation(sentence):
    """Private method to remove punctuation from a sentence."""
    return re.sub(r'[^\w\s]', '', sentence)


class Sentence:
    """A class for evaluating and manipulating English sentences."""
    
    def __init__(self, sentence = ''):
        """Initializes a Sentence object with a sentence string."""
        self.__sentence = _remove_punctuation(sentence)
    
    def get_all_words(self):
        """Returns all words in the sentence as a list."""
        return self.__sentence.split()
    
    def get_word(self, index):
        """Returns the word at a given index, or an empty string if index is
        out of range."""
        words = self.get_all_words()
        return words[index] if index < len(words) else ''
    
    def set_word(self, index, new_word):
        """Replaces the word at a given index with a new word."""
        words = self.get_all_words()
        if 0 <= index < len(words):
            words[index] = new_word
            self.__sentence = ' '.join(words)
    
    def scramble(self):
        """Returns a scrambled list of the words in the sentence."""
        words = self.get_all_words()
        random.shuffle(words)
        return words
    
    def __repr__(self):
        """Represents the Sentence object's sentence as a single string with
        a period."""
        return self.__sentence + '.'


# Unit Test
if __name__ == '__main__':
    test_sentence = Sentence("This is a test sentence, with punctuation!")
    original_sentence = ' '.join(test_sentence.get_all_words())
    test_sentence.set_word(3, "replaced")
    assert 'replaced' in test_sentence.get_all_words(), ("set_word method "
                                                         "failed")
    
    scrambled_sentence = ' '.join(test_sentence.scramble())
    final_version = test_sentence.__repr__()
    
    print("Sentence unit test successful")
    print("Original version:", original_sentence)
    print("Scrambled version:", scrambled_sentence)
    print("Final version:", final_version)
    print("All tests passed.")
