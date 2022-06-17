#RSM pyramid 6/17/2022
def fPyramid(n_p):
      n = n_p
      #use plus 1
      mx = ( (n)* 2) +1
      i =0
      ad =1
      n_l = n+ 2
      md = int(mx /2) 
      while i < n_l:     
            j =0
            while j < mx:
                  if i == 0 or i == n_l-1:
                        print("a", end="")
                  else: 
                        #i = 1 to n_l -1                  
                        if j >= md - int(ad /2) and j<= md + int(ad /2):
                              print(" ", end="")
                        else:
                              print("a", end="")                                
                  j+=1
            print()
            if i >= 1 :
                  ad+=2
            i+=1
print("input pyramid: ", end="")
fPyramid(int(input()))



