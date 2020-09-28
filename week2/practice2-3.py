import sys
even, odd = 0, 0

for line in sys.stdin:
    line=int(line)
    if line%2==1:
        odd+=line
    else:
        even+=line
print('odd:{} even:{}'.format(odd,even))