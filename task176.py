n = input()

d1 = n[0]
d2 = n[1]
d3 = n[2]
d4 = n[3]

if int(d1) % 2 == 0:
    d1 = '*'
if int(d2) % 2 == 0:
    d2 = '*'
if int(d3) % 2 == 0:
    d3 = '*'
if int(d4) % 2 == 0:
    d4 = '*'

print(d1 + d2 + d3 + d4)