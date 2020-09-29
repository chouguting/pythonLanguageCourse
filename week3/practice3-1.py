theInput = input().replace("\r", "")

theList = []
theList = theInput.split(",")

theList.sort()
for item in theList:
    print(item)

theList.reverse()
theSet = set(theList)
for item in theList:
    print(item)

theList = list(theSet)
theList.sort()
theList.reverse()

for item in theList:
    print(item)
