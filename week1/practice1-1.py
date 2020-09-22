theTotalNum=int(input())
pickNum=int(input())

up=1
down=1
for i in range(1,theTotalNum+1):
    up=up*i

for i in range(1,pickNum+1):
    down=down*i

for i in range(1,theTotalNum-pickNum+1):
    down=down*i

print(up//down)