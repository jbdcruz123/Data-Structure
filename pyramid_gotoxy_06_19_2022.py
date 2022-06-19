#practice gotoxy
import os
import time
def gotoxy(x,y):
      #range start of x y is x =1 to up, y =1 to up
      print ("%c[%d;%df" % (0x1B, y, x), end='')
def fDrw(n):
      #triangle wide the total bottom computation
      wd = (n *2 )+1
      #           /2 to get the middle
      md = int(wd /2)
      #ad starts at 1, triangle updater/ iterator
      ad = 1
      y = 0
      os.system("clear")
      #           +2 adjust top and bottom border
      while y < n +2:
            x = 0
             #            +2 adjust left, right border
            while x < wd:
                  #+1 on x and y the starting range of gotoxy
                  gotoxy(x+1, y+1)
                  #                            +1 adjust bottom
                  if y == 0 or y == ((n+2) -2) +1:
                        print("O" , end="", flush=True)
                  else: 
                        #             left                       right range  
                        if x >=  (md - int(ad /2)) and x <= (md + int(ad /2)):
                              print(" " , end="", flush=True)
                        else:
                              print("O" , end="", flush=True)
                  time.sleep(.1)
                  x+=1
            #    ==1 to overpass top border  
            if y >= 1 :
                  ad+=2
            y+=1
      #give another line to next computer printout
      print()
os.system("clear")
print("input height of triangle:   ", end="")
n = int(input()) 
fDrw(n)
