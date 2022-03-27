'''def outer(msg):
    def inner(name,age):
        bio=f'{msg} {name} is {age} yrs old!'
        return bio
    return inner

p=outer( 'Helloo')
print(p('siddu',28))'''
from functools import wraps

def decorated(msg):
    def outer(func):
        @wraps(func)
        def inner(*args):
            return func(*args,msg=msg)
        return inner
    return outer

@decorated('HI')
def display(name,age,msg):
    return(name,age,msg)
print(display('siddu',25))
print(display.__name__)



