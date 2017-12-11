#Sample file for testing the git features
def oneover(j):
    return(1/j)
try:
    i = oneover('x')
    print i
except ZeroDivisionError as e:
    print 'An error occured: %s' % e
except TypeError as e:
    print 'can divide only integers: %s' % e
else:
    print 'No Exception Occured'
finally:
    print 'this always executed'
