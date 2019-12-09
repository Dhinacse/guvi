#bubble sort
l=[3,5,8,2,5]
a=len(l)
  for j in range(a):
    for i in range(a-1):
      if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
print(l)

#merge sort
l=[2,4,6,8,1,3,57,0]
leng=len(l)/2
le=int(leng)
y=l[:le]
u=l[le:]
y,u.sort()
z=y+u
z.sort()
print(z)

#selection sort
a=list(map(int,input().split()))
for i in range(len(a)): 
	key = i 
	for j in range(i+1, len(a)): 
		if A[key] > A[j]: 
			key = j 
	a[i], a[key] = a[key], a[i] 
print(a)
