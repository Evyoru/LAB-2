x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dA = x1**2 + y1**2
dB = x2**2 + y2**2

if dA > dB:
    print("A")
elif dB > dA:
    print("B")
else:
    print("The distance is the same")