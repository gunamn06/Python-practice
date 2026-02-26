#tuple
genders=("Male","Female","Others","Male","Male")
fruits=("Grapes","orange","kiwi")
new_list=print(genders+fruits)
print(type(genders))
print(genders[1:])
print("Grapes" in fruits)
print(genders.count("Male"))
print(genders.index("Male"))

#SETS

s={23,454,47,84,43}
print(s)

s1={1,2,3}
s2={3,4,5}
print(s1|s2)
print(s1&s2)
print(s1-s2)

a=s1.pop()