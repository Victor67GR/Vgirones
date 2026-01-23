# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class estudiant:

    def __init__(self,nota):
        self._nota = nota

    def llegir_nota(self):
        return self._nota
    def modificar_nota(self,nota):
        if nota >= 0 and nota <= 10:
            self._nota = nota
        else:
            print("La nota ha d'estar entre 0 i 10")


estudiant1 = estudiant(7)
print("La nota actual és: ", estudiant1.llegir_nota())

estudiant1.modificar_nota(9)
print("La nova nota és: ", estudiant1.llegir_nota())

        