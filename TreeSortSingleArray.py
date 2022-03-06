# tree sort using array
# N * 2 + 1 (number of tree)

Cn = 0

def fNw(A, N, V): #1A 
  
  if A[N] == -1: #2

    A[N] = V
    
    print("Ang huling lengt na dinag dag (N*2)+2", (N*2)+2, "N", N)
    #left
    A[(N*2)+1] = -1
   
    #right
    A[(N*2)+2] = -1

    return
  #2

  if   V < A[N] : #2
    #left
    
    fNw( A, (N*2)+1, V) 
  else :#2.2  .. V > N
    #right
     fNw( A, (N*2)+2, V) 
  #2


#1A 

def fPr(A, N): #1B

  global Cn

  Cn +=1

  if A[N]==-1: #2
    return
  #2
  
  #left
  fPr( A, (N*2)+1) 
  
  print(A[N])

  #right
  fPr( A, (N*2)+2) 


#1B

def main(): #1C 
  global Cn
  A = []  
  #B = [10, 8, 12, 3, 11,  4 , 14,0 , 15, 13,     5, 19,16 , 6, 9,    1, 15, 7,2 , 18 ]
  #N= 20

  B = [0,1,2,3,4, 5]
  N=6

  j = 1 
  t=0
  i=0

  for i in range(0,N): #2

    j = j * 2
   
    #print("L21 j", j, "t", t)
    t += j
    
    #print("  L21B j", j, "t", t)

    i+=1

  #2
  
  t += 1

  print("Bilang ng na aasign na length t", t)
  
  for I in range(0, t): #2
    A.append(-2)
  #2

  #initial null
  A[0] =-1
  I =0
  while I < N : #2

    fNw(A, 0, B[I])
        
    I+=1
  #2

  print("\n\n\n\n\nAng total na ginamit na index ng array ", t," Ang resulta:")  

  fPr(A, 0)
  
  print("\n\nTotal Count ng func recursion(including return -1): ", Cn)
#1A 



if __name__ == "__main__": #1A
  main()

#1A
