a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3,10)
b.insert(2,15)
a.append(4)
b.append(8)
a.sort()
b.sort(reverse=True)
c = a[0:7]
d = b[2:9]
e = []
for x in range(len(c)):
    e.insert(x,c[x]+d[x])
etuple = tuple(e)
min(e)
max(e)
sum(e)
mystring = "python adalah bahasa pemrograman yang menyenangkan"
setstring = set(mystring)
print(setstring)
liststring = list(setstring)
liststring.sort()
print(liststring)