#RSM 06/18/2022
#string manipulation
def print_title(a=""):
      n = len(a)
      i=0
      if n %2 == 0:
            #para sa wlang butal na string ex: 1234
            n_div = int(n/2)-1
      else:
            #sa may butal na string ex: 12345
            n_div = int(n/2)
      while i < n_div +1:
            j= 0
            #      use -1 dahil ung unang buong string print
            neg_l = i-1
            while j < n:
                  if i== 0:
                        print(a[j], end="")
                  else:
                        if j >= 0 and j <= neg_l:
                              #range 0 to max neg
                              print("-", end = "")
                        elif j >= neg_l +1 and j <= (n-1) -i:
                              #range string format
                              print(a[j], end="")
                        else:
                              #else all range will be " "
                              print(" ", end="")
                  j+=1
            print()
            i+=1
a = "01234"
print_title(a)
b = "12345678901"
print_title(b)
