 try:
            with open('document_no_existent.txt', 'r') as fitxer:
               contingut = fitxer.read()
         except PermissionError:
            print("El fitxer no existeix.")
         else:
            print("Fitxer llegit correctament.")
         finally:
            print("Operació de fitxer acabada.")