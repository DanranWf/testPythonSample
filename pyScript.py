import sys
try:
    assert ('linux' in sys.platform), "linux runs"
except:
    print('first assert erropr')
try:
    assert 1==2, '1 not eauals 2'
except:
    print(' judge error')

try:
    assert 1==1, '1 not eauals 2'
except:
    print(' judge success')


point=(23,256)
print('scare the enemy{}'.format(point))
print('shot the enemy%s'%(point,))
# print

assert False,'false msg'

class Switch():
    pass

if 3==3:
    raise Switch()

