

boy_name=input("Name: ")
girl_name=input("Name: ")
boy_age=int(input("Age: "))
girl_age=int(input("Age "))
age_diff=boy_age - girl_age
if boy_age==girl_age:
    print(f"{boy_name} and {girl_name} are same")
elif boy_age>girl_age:
    print(f"{boy_name} is elder than {girl_name}")
else:
    print(f"{girl_name} is elder")

print(f"{boy_name}loves{girl_name}.Age difference is {age_diff}")
