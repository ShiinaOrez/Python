import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print ('call %s():\n' % func.__name__)
        print ('hash_id:',hash(func.__name__))
        return func (*args,**kw)
    return wrapper

@log
def add():
    a=int(input("a:"))
    b=int(input("b:"))
    print ("a+b=",a+b)

add()

