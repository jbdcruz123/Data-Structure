#example code linkelist using array method
#complete but manual debuger is active
def fCreate(inputD):
    global head; global tail; global tailCount; global elementIndex
   
    #print(f"L10 elementIndex {elementIndex}, inputD {inputD}")
    node[ elementIndex] = -1
    data[  elementIndex ] = inputD
    elementIndex+=1
    return elementIndex-1
    
def fAdd(elementP):
    global head; global tail; global tailCount; global elementIndex    
    
    if node[head] == -1:       
        node[head] = elementP
        tail = node[head]
    else:
        node[tail] = elementP 
        tail = elementP      
    tailCount+=1
    print(f"\n\ntagumpay na nai-add ang {data[elementP]} \npress any...   ", end="")
    input()
    
def fDisplay():
    global head; global tail; global tailCount; global elementIndex
    print("\n\nDisplay:  ")
    countI = 0
    i = node[head]
    while i != -1:
        #print(f"i {i}")
        print( f"[ {countI}, {data[i]} ]", end="")
        i = node[i]
        countI+=1
        #input()
    print("\n")
    
    print(f"\npress any...   ", end="")
    input()
    
def fDelete(countP):
    global head; global tail; global tailCount; global elementIndex
    
    countI = 0
    backI = head
    i  = node[head]
    
    print(f"L20 i {i}, backI {backI}, tail {tail}, tailCount {tailCount}, countP {countP} ")
    print(countP, type(countP))
    while i != -1:
        print(countI, countP)
        if countI == countP:
            print(f"L20A i {i}, backI {backI}, tail {tail}, tailCount {tailCount} ")
            if (tailCount-1) == countI:
                tail = backI                
                print(f"L21")
            
            node[backI] = node[i] 
            node[i] = -1   
            data[ i  ] = -1 #delete value of data    
            tailCount-=1
            print(f"\n\ntagumpay na delete ang {countP}\npress any...   ", end="")
            input()
            break
        countI+=1
        backI = i
        i = node[i]
    else:
         print(f"\n\nalang maidedelete na index na {countP}\npress any...   ", end="")
         input()
         
def fInsert(countP, inputD):
    global head; global tail; global tailCount; global elementIndex
    countI = 0
    backI = head
    i = node[head]
    #new data, new tail
    if i == -1:
        getElementIndex = fCreate( int (inputD) )
        node[head] = getElementIndex
        tail = getElementIndex
        tailCount+=1
        print(f"\n\nalang laman ang node at data, idadagdag natin ang {inputD} sa node at data.\npress any...   ", end="")
        input()    
        return 
        
    #problema ang pagpasok ng insert pag unang input ng node palang
    while i != -1:
        #pag di kita count, canceled or kita new data
        if countI == countP:
            getElementIndex = fCreate( int (inputD) )
            node[backI] = getElementIndex
            node[getElementIndex] = i
            tailCount+=1
            print(f"\n\ntagumpay na na-insert ang index {countP}, data {inputD}\npress any...   ", end="")
            input()
            break
        backI = i
        i = node[i]
        countI+=1
        
    else:
        print(f"\n\nalang nakitang index na {countP}\npress any...   ", end="")
        input()
         
head = 0
tail = 0
tailCount = 0
elementIndex = 1
node = []
for i in range(15):
    node.append(-2)
data = []
for i in range(15):
    data.append(-2)
#intial
node[0] = -1

while 1:
    print("\n\n", node)
    print(data)
    print(f"\n\nhead {head}, tail {tail}, tailCount {tailCount}, elementIndex {elementIndex}")    
    print("\n\n*****\nq quit, a add, p display, d delete, i insert\n*****\ninput code on menu:   ", end="")
  
    inputV = input()
    if inputV == "q":
        print("\n\nexiting...", end="")
        inputV = input()
        break
    elif inputV == "a":
        #add new
        print("\n\nadd mode, input data:  ", end="")
        inputV = input()
        returnV = fCreate(int(inputV))
        fAdd(returnV)
    elif inputV == "p":
        #display all data
        fDisplay()
    elif inputV == "d":
        #delete selected index
        print("\n\ndelete mode, input index to delete:  ", end="")
        inputV = input()
        fDelete(int(inputV))
    elif inputV == "i":
        #insert selected data
        print("\n\ninsert mode, input index to insert:  ", end="")
        inputV = input()
        print("\n\ninsert mode, input data to insert:  ", end="")
        inputD = input()
      
        fInsert( int( inputV ) ,int( inputD )  )
    else:
        print(f"\n\nmali input mo, wla ito sa menu, input mo ay {inputV}\npress any key...   ", end="")
        inputV = input()
    


