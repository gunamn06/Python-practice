x=11
if x==10:
    print("Yes x is 10")
else:
    print("X is not 11")
    
if x%2==0:
    print("X is even")
else:
    print("Not even")
    
signal=input("What color: ")
if signal=="Red":
    print("STOP")
elif signal=="Yellow":
    print("READY")
else:
    print("GO")
    
  #nestedif  
gender="Female"
age=24
if age==5:
    print("Child discount")
else:
    if age==10:
        print("Half ticket")
    elif age<=24:
        print("Full ticket")
    else:
        print("free")