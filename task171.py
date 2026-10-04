x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

d1 = (x1-x2)**2 + (y1-y2)**2
d2 = (x2-x3)**2 + (y2-y3)**2
d3 = (x3-x1)**2 + (y3-y1)**2

if d1 + d2 == d3 or d2 + d3 == d1 or d1 + d3 == d2:
    print("Yes")
else:
    print("No")