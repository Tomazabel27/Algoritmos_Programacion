usuarios = { 
    "iperurena": { 
        "nombre": "Iñaki", 
            "apellido": "Perurena", 
                "password": "123123" 
        }, 
        "fmuguruza": { 
            "nombre": "Fermín", 
                "apellido": "Muguruza", 
                "password": "654321" 
        }, 
        "aolaizola": { 
            "nombre": "Aimar", 
                "apellido": "Olaizola", 
                "password": "123456" 
        } 
    } 
c=0
usuario=input("Ingrese el usuario: ")
while True:
    if usuario=="iperurena":
        break
    if usuario=="fmuguruza":
        break
    if usuario=="aolaizola":
        break
    else:
        print("Usiuario no reconocido")
        usuario=input("Ingrese usuario: ")
        if usuario=="iperurena":
            contraseña=input("Ingrese la contraseña: ")
            while contraseña!="123123":
                contraseña=input("Ingrese la contraseña: ")
                c=c+1
                if c==2:
                    print("Usuario bloqueado")
                    break
            if contraseña=="123123":
                print("Iñaki Perurena")
        if usuario=="fmuguruza":
            contraseña=input("Ingrese la contraseña: ")
            while contraseña!="654321":
                contraseña=input("Ingrese la contraseña: ")
                c=c+1
                if c==2:
                    print("Usuario bloqueado")
                    break
            if contraseña=="654321":
                print("Fermín Muguruza")
        if usuario=="aolaizola":
            contraseña=input("Ingrese la contraseña: ")
            while contraseña!="123456":
                contraseña=input("Ingrese la contraseña: ")
                c=c+1
                if c==2:
                    print("Usuario bloqueado")
                    break
            if contraseña=="123456":
                print("Aimar Olaizola")
