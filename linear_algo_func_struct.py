#RSM 6/15/2022 linear algo
def fInp_num():
      while True:
            try:
                  inp_s =input()
                  i = int(inp_s)
                  return i
            except:
                  print(f"U input wrong number input: {inp_s}")
def fLeav(a, i):
      global lf; global rg; global m; global lop
      if lop == False:
            return False
      if lf > rg :
            print(f"DID NOT FIND IT {i}")
            return False
      return True
def fDeci(a, i):
      global lf; global rg; global m; global lop 
      m = int( (lf+ rg ) /2)      
      print(f"L10 i {i}, a[m] {a[m]}, lf {lf}, m {m}, rg {rg}\n")      
      if i < a[m]:
            rg = m -1            
      elif i > a[m]:
            lf = m +1          
      else:
            print(f"found it {i}, index {m}")
            lop = False
def fMn_fn(a, i):
      global lf; global rg; global m; global lop
      lf = 0
      rg = len(a) -1
      while fLeav(a, i):
            fDeci(a,i) 
lop = True
lf=0
m=0
rg =0         
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(f"available numbers: {a}")
i = fInp_num()
fMn_fn(a,i) 


