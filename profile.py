class Client:
    ##atributos##
    #
    ##fin atributos##
    def __init__(self,run,password,password2,name,type_account,quantity,saldo):
        self.run=run
        self.password=password
        self.password2=password2
        self.name=name
        self.type_account=type_account
        self.quantity=quantity
        self.saldo=quantity

    def deposito(self):
        print("\nRut: ",self.run)
        print("Nombre: ",self.name)
        print("Tipo de cuenta:",self.type_account)
        print("Cantidad de deposito:",self.quantity)


    def giro(self):
        if (int(self.quantity) > 0):
            self.saldo+=self.quantity
            print("Tu saldo es de:",int(self.saldo))
        elif (int(self.quantity) < 0):
            print("ingrese un valor positivo")
        elif (int(self.quantity) ==0):
            print("ingrese un monto valido")
        else:
            print("incorrecto")




