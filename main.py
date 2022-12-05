from Profile import Client

def main():
    print("\nBanco Estado\n")

    run = input("Ingrese su run sin digito verificador: ")
    password= input("ingrese su contrasena: ")
    password2= input("Confirme su contrasena: ")

    if password==password2:

        print("\nBienvenido/a complete sus datos\n")

        name = input("\nNombre: ")
        last_name = input("ingrese su apellido: ")
        mail = input("Correo:")
        type_account = input("Tipo cuenta: ")

        print("\nIngrese el monto a depositar\n")
        balance=0

        quantity = input("Cantidad: ")
        user=Client(run,password,name,last_name,mail,type_account,quantity,balance)

        user.turn()
        if int(quantity)>0:
            user.summary()
        else:
            print("vuelva a intentar")


    else:
        print("contrasena incorrecta")
    



if __name__ == "__main__":
    main()
