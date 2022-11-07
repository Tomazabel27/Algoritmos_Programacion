t=0
z=0
h=0
for k in range(1,500):
    t=((k**2+1)/k)
    z=z+1
    if z<=1000:
        h=h+1
print(h)