#DICTIONARY

dictionary={
    "Guna":"06-10-2003",
    "nagu":"05-03-1971",
    "leela":"30-05-1977"
}

print(dictionary["nagu"])
print(type(dictionary))
print(dictionary.get("poo","Not found"))

dictionary["sudeep"]="34-3-2032"
print(dictionary)
dictionary["Guna"]="05-02-2020"
print(dictionary)
x=dictionary.pop("Guna")
print(x)

print(dictionary.keys())

print(dictionary.items())


for mac in dictionary.items():
    print(mac)