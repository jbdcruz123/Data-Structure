#!/usr/bin/python

#cycle sort

def fCy(A, N): #1A
  
  C=0
  while C < N -2: #2
    
    P = C
    V = A[C] 
    I =P +1

    

    while I < N: #3 
      if A[I]< V :#4
      
        P +=1
      #4
      I +=1
    #3 
    
    if C == P: #3
      C +=1
      continue
    #3
    
    while V == A[P]: #3
      P +=1
    #3

    #swap
    T = A[P]
    A[P] = V
    V = T

    while C != P: #3
      
      P = C
      I = P+1
      while I < N: #4

        if A[I]< V: #5
          P +=1
        #5
        I+=1
      #4
      
      while A[P] == V: #4

        P +=1
      #4
          
      #swap
      T = A[P]
      A[P] = V
      V = T


    #3 

    C +=1
  #2

#1A 

def fMn(): #1B
  
  A=[4,9,1,7,3, 5,0, 5, 2,6]
  N = 10
  print("\nInput: ", A)
  fCy(A, N)
  
  print("\nResult: ", A)

#1B

fMn()