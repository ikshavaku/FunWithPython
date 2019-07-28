size=int(input("Enter the size of which you want to make the rangoli"))
row=size*2-1
for i in range(row+1):
    p=size
    if(i+1<size):
        for d in range(2*(size-(i+1))): #print the "-"
            print("-",end="")
        for c in range(2*i): #print the alphabets
            if(c%2==0):
                print(chr(96+p),end="")
                p=p-1
            else:
                print("-",end="")
        #print("-",end="")
        for c in range(2*i+1): #print the alphabets 
            if(c%2==0):
                print(chr(96+p),end="")
                p=p+1
            else:
                print("-",end="")
        for d in range(2*(size-(i+1))-1): #print the "-"
            print("-",end="")
        print("-")
    elif(i+1>size):
        p=size
        for d in range(2*((i+1)-size)-2):
            print("-",end="")
        for c in range(2*(row-i)): #print the alphabets
            if(c%2==0):
                print(chr(96+p),end="")
                p=p-1
            else:
                print("-",end="")
        for c in range(2*(row-i)+1): #print the alphabets 
            if(c%2==0):
                print(chr(96+p),end="")
                p=p+1
            else:
                print("-",end="")
        for d in range(2*((i+1)-size)-2):
            print("-",end="")
        print("")
