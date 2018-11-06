# CS103 Fall 2018 Johnstone
# HW6 tester (firstWords only): please do not change; feel free to look it over
# python3; copyright 2018 john k johnstone jkj at uab dot edu ; mit license

print ("Use this tester to help refine your code.")
print ("But do not become overly dependent on it: see lecture 8.")
       
# check for syntax errors in the submission
print ("Checking for syntax errors ...", end='')
try:
    import hw6_first_words                              # the student's homework
except Exception as e:
    print ()
    print ('Your code contains a syntax error. Please correct and resubmit.')
    print ('For a fuller error message, run using `python hw6_first_words.py`.')
    print (e)
    exit (1)
print ('passed')

########################################################################
### enforce HW6 constraints on syntax and style, for each fn
########################################################################

import inspect
from tokenize import tokenize
from io import BytesIO

def lint_103 (code, banned_tokens):
    """Ban certain tokens (e.g., later syntax) and enforce 80-column lines.
    Params: 
        code (str): code to be linted
        banned_tokens (list of strings): the banned tokens
    """

    assert (type(banned_tokens) == list)

    # ban certain tokens
    s = code
    g = tokenize (BytesIO (s.encode ('utf-8')).readline)
    for toknum, tokval, _, _, _ in g:
        # ignore empty tokens and whitespace tokens (which do oddly arise)
        if not tokval.strip() == "" and tokval in banned_tokens:
            print ('\nDisallowed token: "' + tokval + '"')
            print ("You are using a feature of Python that is not allowed " +\
                    "in this assignment.\nYou will need to solve this " +\
                    "assignment without using that feature.")
            exit(1)

    # ban long lines
    t = code
    L = t.splitlines()
    for line in L:
        if (len(line) > 80):
            print ('\nDisallowed line: ' + str(line))
            print ("You may not have a line of code longer than 80 characters.")
            exit(1)

banned_tokens_hw6 = (
    'print,global')
banned_tokens = banned_tokens_hw6.split(',')
print ("Checking for violations of CS103 HW6 syntax constraints...", end='')
lint_103 (inspect.getsource (hw6_first_words), banned_tokens)
print ("passed\n")

import random

# ------------------------------------------------------------------------------
# motivation: you should never expect two floats to be exactly equal
# because of machine precision (more later in lecture)

def approxEq (a,b,eps=.00001):  # the 3rd parameter is given a default value
    """Is a ~ b?
    >>> approxEq (1, 1.000001, .0001)
    True
    Params: 
        a: (float)
        b: (float)
        eps: (float) allowable difference
    Returns: (bool) is a within eps of b?
    """
    
    return abs(a-b) < eps

import decimal
def significant (d, n):
    """Given a desired precision, express a float to this level of precision.
    >>> significant (12.345678, 4)
    12.35
    Params: 
        d (float): # of interest
        n (int):   precision (# significant digits)
    Returns: (float) d rounded to this precision
    """

    decimal.getcontext().prec = n
    return float(decimal.Decimal(d) / decimal.Decimal (1))

# ------------------------------------------------------------------------------
def grade (test_id, answer, correct_answer):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (flexible type): submitted answer
        correct_answer (same type as answer): correct answer
    Returns: (bool) is answer correct?
    """
    
    if answer != None:
        print (test_id + ' should be ' + str(correct_answer), end='')
        print ('. Your answer: '+str(answer), end='  ')
    typeCorrect = type(answer) == type(correct_answer)
    if answer != None and typeCorrect and answer == correct_answer:
        print ('CORRECT')
        return True
    else:
        print ('WRONG')
        return False

def ApproxEqualPt (P, Q, eps=.001):
    # are two points in 2-space approximately equal? i.e., dist(P,Q) < eps
    d = np.linalg.norm (np.array(Q) - np.array(P))
    # print ("distance =", d) # to discover what a good tolerance is
    return d < eps

def gradeApproxTuple (test_id, answer, correct_answer):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (float): submitted answer
        correct_answer (float): correct answer
    Returns: (bool) is answer correct?
    """
    
    if answer != None:
        print (test_id + ' should be about ', end='')
        print (str ((significant (correct_answer[0], 7), 
                     significant (correct_answer[1], 7))), end='')
        print ('. Your answer: ', end='')
        print (str ((significant (answer[0], 7), 
                     significant (answer[1], 7))), end=' ')
    if answer != None and ApproxEqualPt (answer, correct_answer):
        print ('CORRECT')
        return True
    else:
        print ('WRONG')
        return False

def gradeApprox (test_id, answer, correct_answer):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (float): submitted answer
        correct_answer (float): correct answer
    Returns: (bool) is answer correct?
    """
    
    if answer != None:
        print (test_id + ' should be about ', end='')
        print (str (significant (correct_answer, 7)), end='')
        print ('. Your answer: ', end='')
        print (str (significant (answer, 7)), end='  ')
    if answer != None and approxEq (answer, correct_answer):
        print ('CORRECT')
        return True
    else:
        print ('WRONG')
        return False

################################################################################
################################################################################
################################################################################
from hw6_first_words import *

def testFirstWords ():
    print ('Testing firstWords.')
    nCorrect = 0
    d = firstWords ('romeo_and_juliet_folger.txt')
    if type(d) != dict:
        print ("Your answer does not return a dictionary.")
        return False
    if grade ('t1', d['FRIARLAWRENCE'], [55,2,3]):
        nCorrect += 1
    if grade ('t2', d['JULIET'], [118,1,3]):
        nCorrect += 1
    if grade ('t3', d['ABRAM'], [5,1,1]):
        nCorrect += 1
    d = firstWords ('a_midsummer_nights_dream_folger.txt')
    if grade ('t4', d['OBERON'], [29,2,1]):
        nCorrect += 1
    if grade ('t5', d['COBWEB'], [4,3,1]):
        nCorrect += 1
    print()
    return nCorrect == 5

########################################
# HW5 main
########################################

def testAll():
    print ('Hello, ' + myName() + '. (If this is not your name, fix myName.)')
    print ('Commencing unit tests...')
    nCorrectQ = 0            # where `correct` doesn't actually mean correct ...
    if testFirstWords():
        nCorrectQ += 1
    print ('# questions passed the tester: ' + str(nCorrectQ) + ' out of 1')
    print ('Note that passing the tester is a positive sign, ')
    print ('but not a guarantee that the code is correct.')
    
def main():
    testAll()

if __name__ == '__main__':
    main()
