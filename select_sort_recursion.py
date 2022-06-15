#select sort
def fFr(i , n):
      if i < n-1:     
            fSc(i, n, i)
            fFr(i+1, n)
def fSc(j, n, v):
      if j < n-1:
            if a[v] > a[j+1]:
                  a[v], a[j+1] = fSw(a[v], a[j+1])
            fSc(j+1,n, v)
def fSw(a,b):
      return b, a
a=[3,0,5,1,2,4]
print(a)
fFr(0, len(a))
print(a)
