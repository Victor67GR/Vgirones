# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash
# 10. Email d’un usuari Classe CompteUsuari amb atribut privat __email El setter valida que l’email contingui “@” i “.” El getter retorna l’email actual

class CompteUsuari:

    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            print("L'email ha de contenir '@' i '.'.")

compte1 = CompteUsuari("vgirones@gmail.com")
print("Email actual de l'usuari:", compte1.email)

compte1.email = "nouemailexample.com"
print("Email després de l'intent de canvi:", compte1.email)