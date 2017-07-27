from calculator_obj import CalculatorObj
from utils import symbolChecker
import parser

def testfunc(a,b):
    return a+b

name = 'test'

testing_app = CalculatorObj(name)

testing_app.register('%',lambda a,b: a+b)
testing_app.register('/',lambda a,b: a/b)
testing_app.register('^',testfunc)
# print type(testing_app.expressions)
# print ''.join(['Key:{0} Value:{1}'.format(k, v) for k,v in testing_app.expressions.iteritems()])
# print set(testing_app.expressions.iterkeys())
testing_app.calc('3*2/ 46/4')
testing_app.calc('32/ 46%4')
testing_app.calc('')
testing_app.calc('1^2')

# print len(testing_app.expressions())
# for key ,value in testing_app.expressions:
#     print 'Key:{} Value:{}'.format(key ,value)

