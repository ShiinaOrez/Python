def log():
        def decorate(func):
                def wrapper(*args,**kw):
                        print('here is going to using a function!')
                        return func(*args,**kw)
                return wrapper
        print('function is over!')
        return decorate
        
@log()
def working():
	print('it just is a normal test')

working()

