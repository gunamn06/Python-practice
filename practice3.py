word=input("Enter the string:")
letter=input("Enter the letter to count")
count=0
for char in word:
    if char==letter:
        count+=1
print(f"The letter {letter} appears {count} times")