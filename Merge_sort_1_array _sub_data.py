#RSM MergeSort lf + rg /2 
def fMn_mrg(lf, rg):
      if lf >= rg:     
            return 
      m = int( (lf + rg) /2)
      fMn_mrg(lf, m-1)
      fMn_mrg(m+1, rg)
      fMrg_prc(lf,m,rg)
#may konting nabago dito pinag sabay ko ung 2nd while at isang array of list nalng ang 
#humawak ng sub data na d 
def fMrg_prc(lf,m,rg):
      d = [0,0,0,0,0,0,0,0,0,0]; i = lf; j =m+1; k=0
      while i <= m and j <= rg:
            if a[i] < a[j]:
                  d[k] = a[i]
                  i+=1
            else:
                  d[k] = a[j]
                  j+=1
            k+=1
      while i<=m or j<= rg:   
            if i <=m:
                  d[k] = a[i]
            if j <=rg:
                  d[k] = a[j]
            i+=1; j+=1; k+=1
      i= 0; k =lf
      while k <= rg:
            a[k] = d[i]
            i +=1; k+=1 
a = [3,1,4,0,5,2]
print(a)
fMn_mrg(0, len(a)-1)
print(a)
