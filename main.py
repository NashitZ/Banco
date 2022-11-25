from Profile import Client

def main():
    print("\nBanco Estado\n")

    run = input("Ingrese su run sin digito verificador: ")
    password= input("ingrese su contrase;a: ")
    password2= input("Confirme su contrase;a: ")

    if password==password2:

        print("\nBienvenido/a complete sus datos\n")

        name = input("\nIngrese nombres: ")
        type_account = input("Tipo cuenta: ")

        print("\nIngrese el monto a depositar\n")
        saldo=23500

        print("\nTu saldo actual es de:", saldo)

        quantity = input("Cantidad: ")
        user=Client(run,password,password2,name,type_account,quantity,saldo)

        user.giro()

    else:
        print("contrase;a incorrecta")
    



if __name__ == "__main__":
    main()
