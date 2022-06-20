#RSM 6/20/2022 one side left triangle with gotoxy code(background and triangle)
import time
import os
def fGotoxy(x,y):
      #range start of x y is x =1 to up, y =1 to up
      print ("%c[%d;%df" % (0x1B, y, x), end="")
def fPyr(n):
      os.system("clear")
      y=0
      #           +2 adjust top and bottom border
      while y < n+2:
            x = 0
            #         +2 adjust left and right border
            while x <n+2:
                  fGotoxy(x+1,y+1)
                  #      0 left border       +1 right border
                  if y ==0 or y == ((n+2) -2)+1:
                        print("*", end ="", flush =True)
                  else: #range of one side left triangle
                        if x >= 1 and x <= y:
                              print(" ", end ="" , flush =True)
                        else:
                              print("*", end ="", flush =True)
                  time.sleep(.1)
                  x+=1
            print()
            y+=1
fPyr(5)
