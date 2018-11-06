################################################################################
# HW6, CS103 Fall 2018 Johnstone
# name:
# blazerid:
################################################################################

import string

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return '99'
################################################################################

################################################################################
# 'removePunctuation' is a helper function I am providing;
# you will want to write other helper fns, but I'm providing this tricky one
def removePunctuation (s):

    """Remove punctuation from a string.

    Params: s (str)
    Returns: s with all punctuation removed
    """
    
    return s.translate (str.maketrans ({c:None for c in string.punctuation}))
################################################################################

def firstWords (fn):

    """Act/scene of 1st words (+ #speeches) for characters in Shakespeare play.

    Params: fn (string) filename of a Shakespeare play,
                        downloaded from Folger Digital Texts in txt format;
                        Reference: http://www.folgerdigitaltexts.org/download/
                        I have made some edits to guarantee consistency.
    Returns: (dict) key = character; value = [nSpeech, act, scene], where
              character := 1st word listed for a character (e.g., BOTTOM) 
              nSpeech   := # speeches by the character;
              act/scene := act and scene of the character's first words
              so each key is a string and each value is [int, int, int] list
    """

    return
