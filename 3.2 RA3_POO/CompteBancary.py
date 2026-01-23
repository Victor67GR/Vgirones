# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class comptebancari:

    def __init__(self,saldo):
        self.__saldo = saldo
    
    def consultar_saldo(self):
        return self.__saldo
    
    def retiran_diners (self,quantitat):
        self.__saldo = self.__saldo - quantitat

    def ingressar_diners (self,quantitat):
        self.__saldo = self.__saldo + quantitat



compte1 = comptebancari(5000)

compte1.ingressar_diners(1000)

print("El saldo actual és: ", compte1.consultar_saldo())

