#!/usr/bin/env python3

def return_evens(sequence):
    """
    Returns a list of all even elements from a sequence of integers.
    
    Args:
        sequence: A sequence of integers
        
    Returns:
        A list containing only the even integers from the input sequence
    """
    return [n for n in sequence if n % 2 == 0]


def make_exclamation(sentences):
    """
    Takes a list of sentence strings and returns them with exclamation marks.
    
    Args:
        sentences: A list of sentence strings
        
    Returns:
        A list of sentences with exclamation marks appended
    """
    return [sentence + "!" for sentence in sentences]