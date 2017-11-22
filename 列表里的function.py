s_b=raw_input('please scanf the start str:')
s=list(s_b)
i=0
while i==0 :
    order=raw_input('please scanf the order(a,c,e,ind,ins,end):')
    if 'a' in order :
        key=0
    if 'c' in order :
        key=1
    if 'e' in order :
        key=2
    if 'ind' in order :
        key=3
    if 'ins' in order :
        key=4
    if 'end' in order: break
    lenth=len(s)
    print "now the str is:",s,'the lenth is:',lenth
    if key==0:
        s_a=raw_input('please scanf the element:')
        s.append(s_a)
    if key==1:
        s_c=raw_input('please scanf the element you want to know how much is it:')
        t=s.count(s_c)
        print 'number:',t
    if key==2:
        ss_e=raw_input('please scanf the list you want to extend:')
        s_e=list(ss_e)
        s.extend(s_e)
    if key==3:
        s_ind=raw_input('please scanf the element you want to find:')
        place=s.index(s_ind)
        print 'location:',place
    if key==4:
        p=input('scanf the place:')
        s_ins=raw_input('please scanf the element you want to insert:')
        s.insert(p,s_ins)
print 'this program is over!thanks to use me!'
        
