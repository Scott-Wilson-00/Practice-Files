Y = int(input())

found = False
i = 0
while not(found):
    i += 1
    year = str(Y+i)
    x = []
    for char in year:
        x.append(year.count(char))
    if sum(x)/len(x) == 1:
        found = True
    

print(year)
