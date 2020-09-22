import  decimal
m=input("本金:")
m=decimal.Decimal(m)

n=input("利率:")
n=decimal.Decimal(n)

years=input("存幾年:")
years=decimal.Decimal(years)

result=m*(1+n)**years
print("本利和:{}".format(result))