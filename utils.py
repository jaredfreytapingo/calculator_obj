import inspect
from types import *

def symbolChecker(symbol_input):
    if not stringChecker(symbol_input):
        print 'The Symbol {} must be a string'.format(symbol_input)
        return False
    elif symbol_input.isdigit():
        print "The Symbol you typed {} must not be a digit".format(symbol_input)
        return False
    else:
        return True

def stringChecker(input):
    if isinstance(input, str):
        return True
    else:
        return False


def expressionChecker(expression):
    """
    Input: expression input
    Output: True or False depending on the expression
    """
    if not inspect.isfunction(expression):
        print 'The Input expression is not a function'
        return False
    else:
        return True
