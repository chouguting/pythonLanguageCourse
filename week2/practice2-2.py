x=input().replace("\r","")
y=input().replace("\r","")
z=input().replace("\r","")
theList=[]
theList=x.split(",")
if x.find(y)!=-1:
    print("True")

else:
    print("False")
print(x.find(y))
print(theList)
print(theList[0]+"--"+theList[1])
print(theList[0]==y)
print(theList[-1]==y)
print(x.upper())
print(x.title())
print(y.isnumeric())
print(x.replace(y,z))