n=6
lista=[]
while True:
    if n<62:
        lista.append(n)
        n=n+5
    if n==61:
        lista.append(n)
        print(n)
        print(sum(lista))
        break
