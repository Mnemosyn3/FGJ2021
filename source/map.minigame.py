map =  []
newstring = ""
for i in range(900):
    newstring = ""
    for u in range(1000):
        if u == 1:
            newstring = newstring + "W"
        elif u == 999:
            newstring = newstring + "W"
            map.append(newstring)
        else:
            newstring = newstring + " "
for string in map:
    print('"' + string + '",')
list