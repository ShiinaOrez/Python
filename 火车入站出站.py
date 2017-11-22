n=input('please scanf the n:')
i=0
lifo=[]
for i in zip(range(n)):
    element=raw_input('please scanf the  next:')
    lifo.append(element)
i=0
for i in zip(range(n)):
    s=lifo.pop()
    print s,'\n'
print 'over'
