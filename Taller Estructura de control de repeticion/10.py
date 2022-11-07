lista=[]
while True:
    alturas=float(input())
    if(alturas!=0):
        lista.append(alturas)
    if(alturas==0):
        print("El estudiate mas alto es de:",max(lista))
        break