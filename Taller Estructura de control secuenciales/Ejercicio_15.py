#Entradas
pvp= int (input("Ingrese el precio original del producto: "))
ppf= int (input("Ingrese el valor que usted pagó por el producto: "))
#Caja negra
descuento=(100*ppf) / pvp
final=(descuento-100)*-1
#Salida
print("El descuento fue del:",final,"% de descuento")