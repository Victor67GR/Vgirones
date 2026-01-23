# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class Usuari:

    def __init__(self, nom, contrasenya):
        self.nom = nom
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            print("Contrasenya canviada correctament.")
        else:
            print("La contrasenya ha de tenir almenys 8 caràcters.")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau
    
usuari1 = Usuari("Victor", "contrasenya123")
print(usuari1.verificar_contrasenya("contrasenya123"))  # True

usuari1.canviar_contrasenya("nova123")  # Error: massa curta

usuari1.canviar_contrasenya("novaContrasenya456")  # Contrasenya canviada correctament.
print(usuari1.verificar_contrasenya("novaContrasenya456"))  # True  