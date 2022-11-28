class Client:
    ##atributos##
    #
    ##fin atributos##
    def __init__(self,run,password,name,last_name,mail,type_account,quantity,balance):
        self.run=run
        self.password=password
        self.name=name
        self.last_name=last_name
        self.mail=mail
        self.type_account=type_account
        self.quantity=quantity
        self.balance=0

    def summary(self):
        print("\nResumen de deposito")
        print("\nRut: ",self.run)
        print("Nombre: ",self.name,self.last_name)
        print("Correo: ",self.mail)
        print("Tipo de cuenta:",self.type_account)
        print("Monto de deposito:",self.quantity)


    def turn(self):
        if (int(self.quantity) > 0):
            self.balance+=int(self.quantity)
        elif (int(self.quantity) < 0):
            print("ingrese un valor positivo")
        elif (int(self.quantity) ==0):
            print("ingrese un monto valido")
        else:
            print("incorrecto")





