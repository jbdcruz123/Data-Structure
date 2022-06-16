#RSM 06/16/2022
#string manipulation
def print_title(a=""):
      n = len(a)
      i=0
      while i < int(n/2):
            sb_1 =""
            n_neg = i
            i_neg = 0
            while  i_neg < n_neg:
                  print("-", end="")
                  i_neg+=1                 
            j=0
            j+=i
            while j< n-i:
                  print( a[j], end="")
                  j+=1
            print()      
            i+=1
a = "URSA WARRIOR"
print_title(a)
b = "the quick brown fox"
print_title(b)
