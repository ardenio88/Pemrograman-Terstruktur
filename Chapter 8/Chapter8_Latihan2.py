listx = [1,9,2,5,4,3]
tupx = tuple(listx)
def datastat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    listdata = [a,b,c]
    return listdata

print(datastat(tupx))