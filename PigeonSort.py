#!/usr/bin/python

#pigeon sort, effective on characters
def fPg(A, N, Mn, Mx): #1B
  
  Cn=[]
  Ln = Mx - Mn
  for I in range(0, Ln +1):#2

    Cn.append(0)
  #2
  
  I = 0
  while I < N: #2
   
    Cn[A[I]-Mn] += 1  
    I +=1
  #2
  
  J=0
  
  for I in range(0, Ln+1): #2

    while Cn[I] >=1: #3

      Cn[I] -=1
      A[J] = I +Mn
      J+=1 
    #3
          
   #2

#1B 

def fMn(): #1A
  
  A= [50,3,12,4,1000, 1]

  print("\ninput: ", A)
  fPg(A, 6, 1, 1000)  

  print("\nresult: ", A)

#1A

fMn()
