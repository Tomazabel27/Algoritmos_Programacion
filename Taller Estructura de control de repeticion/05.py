restante=0
n=int(input())
k=int(input())
while True:
    if k<n:
        r=n-restante
        print("El numero ahora es:",r)
        restante=restante+1
    if r==k:
        break