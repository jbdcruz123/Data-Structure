#RSM 6/18/22
#one side pyramid
def fPyr_left(n):
      i= 0
      while i < n:
            j=0
            while j < n:
                  if j >= 0 and j <= (n-1) - (i+1):
                        print(" ",end="")
                  else:
                        print("*", end= "")
                  j+=1
            i+=1
            print()
def fPyr_right(n):
      i= 0
      while i < n:
            n_2 =i
            j=0
            while j <= n_2:
                  print("*", end="")
                  j+=1
            print()
            i+=1
#ex: fPyr_left_blank by 5
#******* 
#***** *
#****  *
#***   *
#**    *
#*     *
#*******
def fPyr_left_blank(n): 
      #n = 5 sample input     
      i_y = 0
      #n+2 border top and botom
      while i_y < n+2:
            j_x=0
            while j_x < n +2:
                  #showing ((n+2)-2) ang adjustment sa past redefine
                  # top margin       dahil 0 to 5 length bottom may + 1, 
                  #  i_y == 0       ((n+2)-2)+1
                  if i_y == 0 or i_y == ((n+2)-2)+1:
                        print("*", end= "")
                  else: #ang middle triangle                      
                        if j_x >= (n+1)-i_y and j_x <= (n+1)-1:
                              # 5 + 1 extend    les         5 +1 show lenght border     get it back, accurate display
                              #(n +1)          -(i_y)       (n+1)-1                      -1      
                              print(" ", end="")  
                        else: #i use else cause no other condition will occur but 2 only
                              #.. j_x <= ( (n+1 )-1) - i_y or j_x == (n+1):
                              #   5 +1 ext les 1 to get 5   les 1        5 + 1 para sa border likod
                              #( (n +1 )      -1)          -i_y        (n+1)
                              print("*", end="")                    
                  j_x+=1
            print()
            i_y+=1
#ex: fPyr_right_blank by 5
#******* 
#* *****
#*  ****
#*   ***
#*    **
#*     *
#*******
def fPyr_right_blank(n):
      #n = 5
      i_y = 0
      # use         +2 dahil sa border sa top at bottom
      while i_y < n +2:
            j_x =0
            #use         +2 para sa x line or width 
            while j_x < n +2:
                  if i_y == 0 or i_y == ((n+2)-2) +1: 
                        print("*", end= "")
                  else: #focusing on "" triangle range 1 to up width
                        if j_x >= (0 +1) and j_x <= i_y:
                              print(" ", end = "")
                        else: #asuming left conditon will be "*"
                              # j_x_len = i_y+1 after while j_x
                              #      ==0  para sa boarder                          
                              #                                
                              #                                n+1 para sa sobra sa right
                              #.. j_x ==0 or j_x >= j_x_len and j_x <= n+1
                              print("*", end = "")
                  j_x +=1
            print()
            i_y +=1
def fPyr_test(n):
      i_y = 0
      #left side using "*" gilid ng triangle
      #aditional +2 for top botton and left, right width
      while i_y < n+2:
            j_x = 0
            j_x_len = i_y +1 
            while j_x < n+2:                  
                  if i_y == 0 or i_y == ( (n+2) -2) + 1:
                        print("*", end = "")
                  else: #reverse version ng condition ng fPyr_left_blank
                        if j_x == 0 or ( j_x >= j_x_len and j_x <= ( (n+2 )-2) +1 ):
                              print("*", end = "")
                        else:
                              print(" ", end = "") 
                  j_x+=1
            print()
            i_y+=1
print("input height of triangle max 20:  ", end="")
inp = int(input())
print("left")
fPyr_left(inp)
print("\nright")
fPyr_right(inp)
print("\nleft blank")
fPyr_left_blank(inp)
print("\nright blank")
fPyr_right_blank(inp)
print("Pyr test\n")
fPyr_test(inp)
