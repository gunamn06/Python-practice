Number=int(input("Enter the number: "))
if Number%2==0:
    print("The num is even: ")
else:
    print("The num is odd: ")
    
    
word=input("Enter the string: ")
reversed_word=word[::-1]
if word==reversed_word:
    print("Palindrome")
else:
    print("Not plindrome")
    
    
for i in range(1,11):
    print(f"{5}x{i}={5*i}")
    
a=12
b=23
a,b=b,a
print("a",a,"b",b)

text=input("Enter a string: ")

vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count+=1
print("Num of vowels is:",count)


num=int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of number is:",fact)

l=[1,4,3,6,7,83,3]
new=sum(l)
print(new)


num=int(input("Enter the number:"))
a=0
b=1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c

    
    