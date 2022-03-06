
aIndx=[]
aVlue = []
aNull =0
aLngt =0
aGlbl = 0
aDrct = 0
aBack = 0

def fPrntArry(Indx): #1D

  if aVlue[Indx] == -1: #2
  
    return
  #2

  fPrntArry(aIndx[Indx][0])

  print(aVlue[Indx])
  fPrntArry(aIndx[Indx][1])

#1D

def fTreeSort(Indx, Vlue):#1C
  global aGlbl
  global aNull
  global aDrct
  global aBack

  print("L10 aValue[Indx]", aVlue[Indx], "Indx", Indx, "Vlue", Vlue, "aNull", aNull, "aGlbl", aGlbl)
  print("aBack", aBack, "aDrct", aDrct)
  #input()

  if aVlue[Indx] ==-1: #2
    Indx = aGlbl
    aGlbl +=1
    
    if aDrct == 0: #3
      
      #back call edit 
      aIndx[aBack][0] = Indx

    elif aDrct == 1: #3.2
       
      #back call edit
      aIndx[aBack][1] = Indx
          
    #3.3
      
    #ang new value na enter
    aVlue[Indx] = Vlue
    aIndx[Indx][0] = aNull
    aIndx[Indx][1] = aNull

    return 
  #2

  print("L11 Vlue", Vlue ,"aValue[Indx]", aVlue[Indx], "Indx", Indx, )

  if Vlue < aVlue[Indx]: #2
    #it is small find slot int left
    aBack = Indx
    aDrct = 0
    fTreeSort(aIndx[Indx][0], Vlue)
  else: #2.2
    #it is big fine slot in right
    aBack = Indx
    aDrct = 1
    fTreeSort(aIndx[Indx][1], Vlue)
  #2.2


#1C 

#initial array
def fIntlArry(): #1B
  global aLngt
  global aNull
  global aLngt

  #aLngt ang last null terminate imbis na 0 to (aLngt -1)
  n = aLngt +1
  k=0

  #dereference ang 10th element
  aNull = n-1
  for i in range(0, n): #2
  
    aIndx.append([])
    aVlue.append(-2)
    for j in range(0,2): #3 
    
      aIndx[i].append(-2)
      k+=1
    #3
  
  #2
  
  aVlue[aNull] = -1
#1B 

def main(): #1A 
  
  global aDrct
  global aBack
  global aLngt
  ########
  ####input value, tiyakin na ang range ng list ay pantay sa lenght ung n 
  inpt = [10, 8, 12, 3, 11,  4 , 14,0 , 15, 13,     5, 19,16 , 6, 9,    1, 15, 7,2 , 18 ]
  n = 20
  ######
  
  
  aLngt =n

  fIntlArry()
  
  print("\n\ninput:", inpt)

  aVlue[0]=-1
  
  #default intial for first dereference of index adress
  aDrct = 2
  aBack = 0

  for i in range(0, n): #2
    
    print("L9 i", i, "inpt[i]", inpt[i])
    print("aIndx", aIndx)
    print("aVlue", aVlue)

    fTreeSort(0, inpt[i])


  #2
  print("aIndx", aIndx)
  print("aVlue", aVlue)

  fPrntArry(0)

#1A


if __name__ == "__main__": #2

  main()
#2