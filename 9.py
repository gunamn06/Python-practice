i=1
while i<=10:
    x=0
    while x<i:
        print("*",end="--")
        x+=1
    print("")
    i+=1
   
print("Stop")


pin="1234"
while True:
    user_input=input("PIN: ")
    if user_input==pin:
        print("CORRCT")
        break
    else:
        print("INCORRECT")
    


    
    
