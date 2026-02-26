for i in range(1,101):
    if i%2==0:
        print(i,end=" ")
        
num=int(input("Enter a number:"))
sum=0

while num>0:
    sum=sum+(num%10) #add last digit
    num=num//10 #remove last digit
    
print("Sum of digits:",sum)

String="  Hello world"
#print(String.upper())
print(String.strip())