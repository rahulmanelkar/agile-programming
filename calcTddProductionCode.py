def add(a,b):
    return a+b;
    '''
    if type(a) == int and type(b) == int:
        return a+b
    else:
        raise TypeError("Invalid type: {} and {}".format(type(a),
                                                     type(b)))
'''
    #pass

def sub(a,b):
    return a-b
    '''
    assert type(a) is not IntType, "a is not integer: %r" % a
    assert type(b) is StringType, "name is a string: %r" % name
    '''
    #pass

def multiply(a,b):
    return a*b
    pass

def divide(a,b):
    return a/b
    pass
