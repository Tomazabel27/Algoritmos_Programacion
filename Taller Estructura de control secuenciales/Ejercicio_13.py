#Entradas
n50000= int (input("Ingrese el numero de billetes de 50000: "))
n20000= int (input("Ingrese el numero de billetes de 20000: "))
n10000= int (input("Ingrese el numero de billetes de 10000: "))
n5000= int (input("Ingrese el numero de billetes de 5000: "))
n2000= int (input("Ingrese el numero de billetes de 2000: "))
n1000= int (input("Ingrese el numero de billetes de 1000: "))
n500= int (input("Ingrese el numero de billetes de 500: "))
n100= int (input("Ingrese el numero de billetes de 100: "))
#Caja negra
n1=50000*n50000
n2=20000*n20000
n3=10000*n10000
n4=5000*n5000
n5=2000*n2000
n6=1000*n1000
n7=500*n500
n8=100*n100
ntotal=(n1+n2+n3+n4+n5+n6+n7+n8)
#Salidas
print("En el banco hay: $",ntotal,"COP")