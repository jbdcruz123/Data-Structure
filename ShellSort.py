#shell sort python
def fA(A, N): #1B

  G =int(N /2)
  while G>= 1:#2
    
    print("G", G, "N", N, "A", A)
    I = G
    while I < N:#3
      
      J = I
      while J-G >= 0: #4
        
        if A[J-G] > A[J]: #5
          
          T = A[J-G]
          A[J-G] = A[J]
          A[J] = T

        #5 
        
        J -=G
      #4
      
      I +=1
    #3 

    G = int(G / 2)
  #2

#1B

def fMn(): #1A

  A =[4,3,0,5,1, 2]
  N = 6
  print("\n\nInput:")
  
  print(A)

  fA(A,N)

  print("\nResult A", A)
  
#1A 

fMn()
