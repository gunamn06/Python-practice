l=[12,23,1,23,45,22,56]
total=0
for num in l:
    total=total+num
    print(total)
    
l=[12,23,1,23,45,22,56]
dl=[]
for num in l:
    dl.append(num*2)
    print(dl)
    
    
dll=[num*2 for num in l]
print(dll)


pop={
    "Bengaluru":76,
    "Hubli":45,
    "Smg":65,
    "Bdvt":34,
    "Gubbi":12
}
large_city={key:value for key,value in pop.items() if value>20}
print(large_city)
    