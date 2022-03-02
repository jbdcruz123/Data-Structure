#!/usr/bin/python

#CombSort.py RSM Version
def fA(A, N): #1

  G = N
  Sw=1
  while 1: #2
  
    if G <=1 and Sw ==0: #3
      break
    #3

    #dapat mahuli ang update ng increment para masala ung G==1
    G = (G *10 ) //13 
    
    if G <=1: #7
    
      G=1
    #7
    
    Sw = 0
     #sa ori version sinimulan sa 0, sa version ko sa kalahati ng length nag simula
    R = G
  
    while R < N: #4

      if A[R-G] > A[R] : #5

        #switch
        T =  A[R-G]
        A[R-G] =  A[R]
        A[R] =T
        Sw =1
      #5

      R+=1
    #4

  #2

#1A

def fMn(): #1B

 #A= [5,4,3,0,4, 1]
 
 A= [6, 47, 3, 8, 9,   4, 2, 90, 1, 6]
 
 N =10

 print("\ninput:", A)
 
 fA(A, N)
 print("\nresult:", A)
#1B


fMn()