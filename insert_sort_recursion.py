#RSM insert sort recursion recursion
def fMn(i):
      n = len(a)
      if i < n-1:
            v = a[i+1]
            fSc(i, v)
            fMn(i+1)
def fSc(j, v):
      if j >=0 and v < a[j]:
            a[j+1] = a[j]
            fSc(j-1, v)
      else:
            a[j+1] = v

a =[3,0,7,2,5,9,1,8,3,6,4]
print(a)
fMn(0)
print(a)
            
