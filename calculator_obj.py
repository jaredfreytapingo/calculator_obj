from utils import symbolChecker, expressionChecker, stringChecker
import parser ,itertools
class CalculatorObj:
    def __init__(self, name):
        self.name = name
        self.expressions = {}

    def register(self,symbol="", expression=""):
        try:
            if not symbolChecker(symbol):
                return
            elif not expressionChecker(expression):
                return
            else:
                self.expressions[symbol] = expression
            print 'The Symbols and expression pass the tests'.format(symbol,expression)
        except Exception:
            print 'An error occured {}. The Symbol {} and its expression {} did not work'.format(Exception,symbol, expression )
            raise
    pass


    def calc(self, input=""):
        '''
        :param input: 
        :return:         
        '''
        try:
            self.calcInputChecker(input)
            input = input.replace(" ", "")
            splitExpression = self.calcExpressionChecker(input)
            if splitExpression:
                # print 'Input is {}'.format(input)
                expressionList = splitExpression[1::2]
                valuesList = [float(x)for x in splitExpression[0::2]]
                buffer = [valuesList[0]]
                for i in range(len(expressionList)):
                    buffer.append(self.expressions.get(expressionList[i])(buffer[i],valuesList[i+1]))
                result =buffer[len(buffer)-1]
                print 'SUCCESS Result is {}'.format(result)
                return result
            else:
                return
        except Exception:
            print  Exception

    def calcInputChecker(self,input):
        if not stringChecker(input):
            return False
        elif (input.replace(" ", "") == '' or len(input.replace(" ", "")) == 0):
            print 'No Input Given'
            return False
        else:
            return True


    def calcExpressionChecker(self,input):
        splitExpression = ["".join(x) for _, x in itertools.groupby(input, key=str.isdigit)]
        nonDigits = [x for x in splitExpression if not x.isdigit()]
        if len(list(set(nonDigits)-set(self.expressions.keys()))) != 0:
            print 'Expressions were found in input that are not in list {}'.format(list(set(nonDigits)-set(self.expressions.keys())))
            return False
        else:
            return splitExpression


