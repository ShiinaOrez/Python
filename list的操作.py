s1=raw_input('please scanf the str:')
s=list(s1)
i=0
while i==0:
    o=raw_input('please scanf the order(next or end):')
    key='x' in o
    if key==0:
        break
    else :
        l=len(s)
        print "now the 's':",s,'\n lenth is ',l
        head=input('please scanf the head:')
        tail=input('please scanf the tail:')
        ss1=raw_input('please scanf the word you want to replace:')
        ss=list(ss1)
        s[head:tail]=ss
print 'It is final str!'
