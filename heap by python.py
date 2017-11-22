def heap_up(k,heap):
	j=k//2
	while heap[j]>heap[k]:
		heap[j],heap[k]=heap[k],heap[j]
		k=j
		j=k/2
def heap_down(k,heap,limit):
	while k*2<=limit :
		j=k*2
		if j<limit and heap[j+1]<heap[j]:
			j+=1
		if heap[k]>heap[j]:
			heap[k],heap[j]=heap[j],heap[k]
			k=j
		else :break	

def heap_sort(heap):
	i=0
	N=len(heap)-1
	for i in range(len(heap)-1):
		print heap[1],' '
		heap[1]=heap[N]
		N-=1
		heap_down(1,heap,N)
n=input('scanf the n:')
heap=list([-1])
i=0
for i in range(n):
	heap.append(input('scanf the element:'))
	heap_up(len(heap)-1,heap)
heap_sort(heap)
print 'sort over !'
