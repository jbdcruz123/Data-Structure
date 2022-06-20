#simple pyramid 6/22/2022
def fSimple_pyramid(n):
      y=0
      while y < n:
            x =0
            while x < n:
                  if x <= y:
                        print("*", end="")
                  x+=1
            print()            
            y+=1
fSimple_pyramid(5)
