---
titlepage: false
lang: es
toc: false
footer-right: \thepage/\pageref{LastPage}
header-includes:
  - \usepackage{graphicx}
  - \usepackage{lastpage}
  - \usepackage{xltxtra}
  - \usepackage{listings}
  - \usepackage{pdflscape}
  - \usepackage{awesomebox}
  - \usepackage{xcolor,tikz,tcolorbox}
  - \usepackage{caption}
  - \usepackage{emoji}
  - \usepackage{eso-pic}
  - \AddToShipoutPictureBG{
      \ifthenelse{\value{page}=1}{
        \includegraphics[width=\paperwidth,height=\paperheight]{img/portadaEx.png}
      }{
        \includegraphics[width=\paperwidth,height=\paperheight]{img/paginasEx.png}
      }
    }
  - \setemojifont{Noto Color Emoji}
  - \tcbuselibrary{raster}
  - \definecolor{lightblue}{rgb}{0.68, 0.85, 0.9}
  - \definecolor{ballblue}{rgb}{0.13, 0.67, 0.8}
  - \definecolor{cerulean}{rgb}{0.0, 0.48, 0.65}
  - \definecolor{almond}{rgb}{0.94, 0.87, 0.8}
  - \definecolor{apricot}{rgb}{0.98, 0.81, 0.69}
  - \definecolor{cream}{rgb}{1.0, 0.99, 0.82}
  - \definecolor{coralred}{rgb}{1.0, 0.25, 0.25}
  - \definecolor{byzantium}{rgb}{0.44, 0.16, 0.39}
  - \definecolor{thistle}{rgb}{0.85, 0.75, 0.85}
  - \definecolor{ceruleanblue}{rgb}{0.16, 0.32, 0.75}
  - \definecolor{beaublue}{rgb}{0.74, 0.83, 0.9}
  - \renewcommand{\normalsize}{\small}
...

\noindent
\makebox[\textwidth][c]{
  \begin{minipage}[t]{0.65\textwidth}
    \textbf{\textit{\Large Examen Recuperació - RA3-RA5}}
  \end{minipage}%
  \hspace{0.05\textwidth} % espai entre títol i taula
  \begin{minipage}[t]{0.25\textwidth}
    \begin{tabular}{|c|c|}
    \hline
    \multicolumn{2}{|c|}{\textbf{NOTA}} \\ \hline
    RA3 & RA5 \\ \hline
     &  \\ \hline
    \end{tabular}
  \end{minipage}
}


## Preguntes RA3

1. **Quina serà l'eixida per pantalla d'aquest codi?**

   ```python
   def suma(a, b):
      return a + b
   resultat = suma("4", "5")
   print("El resultat és:", resultat)
   ```

   - a) El resultat és: 9
   - b) El resultat és: None
   - c) TypeError
   - d) Cap és correcta

2. **Què farà el següent codi si s'executa?**

   ```python
   def salutacio(nom="Usuari"):
      return f"Hola, {nom}!"

   print(salutacio(hola))
   print(salutacio("Joan"))
   ```
   - a)  Hola, Usuari! / Hola, Joan!
   - b)  Hola hola / Hola Joan
   - c)  Hola, None! <br> Hola, Joan!
   - d)  NameError: name 'hola' is not defined

3. **Què farà el següent codi?**

   ```python
      llista = [10, 20, 30, 40]
      llista[4] = 35
      print(llista)
   ```

   - a)  [10, 20, 30, 35]
   - b)  [10, 20, 35, 40]
   - c)  [35, 20, 30, 40]
   - d)  Cap és correcta

4. **Quin error presenta el següent codi?**

   ```python
      x = 10
      if x > 5:
      print("És major que 5")
   ```

   - a) Error de sintaxi en la condició if
   - b) Error d’indentació
   - c) Error en la funció print
   - d) El codi és correcte i s’executa sense errors

5. **Quina serà l'eixida del següent codi?**

   ```python
   x = 5
   y = 3
   z = x % y
   print(z)
   ```

   - a)  7
   - b)  25
   - c)  15
   - d)  2

6. **Un bucle while acaba quan...**
   - a) Es compleix la condició del bucle
   - b) No es compleix la condició del bucle
   - c) Quan usem exit
   - d) a) i c) són correctes

7. **Quina afirmació és certa sobre les assercions en Python?**
   - a) Les assercions llançaran excepcions sempre que una condició siga certa.
   - b) Les assercions no llancen excepcions
   - c) Les assercions es poden utilitzar per llançar excepcions, les capturem o no.
   - d) Les assercions es poden utiliztar per capturar excepcions.

\newpage

8. **Quina serà l'eixida del següent codi?**

   ```python
   x = 5
   y = 10
   if x < y:
      z = x * 2
   if z >= 10:
      z = y / 2
   print(z)
   ```

   - a) 10
   - b) 2.0
   - c) 5
   - d) 20

9. **Quina és la funció principal d'un bloc `try`/`except` en Python?**
   - a) Depurar errors lògics
   - b) Manipular el flux de control
   - c) Llançar excepcions
   - d) Cap és certa

10. **Què fa l'excepció `IndexError` en Python?**
   - a) Es produeix quan accedim a la posició 0 de range(1,4)
   - b) Es produeix quan utilitzem un tipus de dada incorrecte com a índex.
   - c) Es produeix quan intentem accedir a un element fora dels límits d’una seqüència.
   - d) a) i c) són correctes

11. **CQuina instrucció permet saltar a la següent iteració d’un bucle quan es compleix una condició, sense eixir del bucle?**
   - a) Usant `pass`
   - b) Usant `break`
   - c) Usant `continue`
   - d) Usant `exit`

 \newpage

12. **Què fa el mètode `input()` a Python?**
   - a) No mostra cap missatge per pantalla, llig una entrada de l’usuari i la converteix automàticament en un valor numèric.
   - b) Mostra el missatge per pantalla que se li passe, llig una entrada de l’usuari i la retorna sempre com una cadena.
   - c) Mostra el missatge per pantalla que se li passe i llig dades des d’una font externa definida pel sistema.
   - d) Mostra el missatge per pantalla que se li passe.

13. **Quina és l'eixida del següent codi?**

   ```python
      for i in range(2, 3):
         print(i)
   ```

   - a) 2 3
   - b) 3
   - c) 2
   - d) Cap és correcta

14. **Quina afirmació és incorrecta sobre les excepcions?**
   - a) Les excepcions es poden llançar amb `assert`.
   - b) Quan una excepció es llança, l'execució del programa es deté sempre.
   - c) Les excepcions són útils per controlar errors de lectura de fitxers.
   - d) Les excepcions es poden capturar encapsulant el codi en un try/except.

15. **Com es pot eixir d'un bucle `for`?**
   - a) Amb `break`
   - b) Amb `continue`
   - c) Amb `pass`
   - d) Amb `exit`

\newpage

16. **Quina serà l'eixida d'aquest codi?**

   ```python
      x = 0
      for i in range(2,5):
         x+=i
      assert x < 10, "El valor ha de ser menor de 10"
   ```

   - a) `El valor ha de ser menor de 10`
   - b) `ValueError: El valor ha de ser menor de 15`
   - c) `AssertionError: El valor ha de ser menor de 10`
   - d) No produeïx cap eixida

17. **En quina situació s'utilitza el bloc `else` dins de l'estructura `try`/`except`?**
   - a) Per capturar excepcions no controlades previament
   - b) Per garantir que el codi que conté s'executi sempre
   - c) Per executar si no hi han excepcions
   - d) Per executar quan finalitza el codi

18. **Quina eixida per pantalla produeix este codi `if`/`elif`/`else`?**

   ```python
      x = 2
      y = 1

      if(x != 2):
         y-=1

      else:
         y+=1

      if(y == 2):
         y+=1

      elif(x == 2):
         y+=2

      else:
         print("Adéu")

      if(x-y == 1):
         print("Eixida espectacular")
      else:
         print(str(x)+ " " + str(y))

   ```

   - a) Eixida espectacular
   - b) 2 4
   - c) 2 3
   - d) Adeu  
        3 1

19. **Quina serà l'eixida del següent codi?**

   ```python
      for i in range(6, 3):
            print(i)
   ```

   - a) 3 4 5 6
   - b) 6 5 4 3
   - c) 6 5 4
   - d) Cap és correcta

20. **Que val la variable suma al finalitzar la tercera iteració del bucle?**

   ```python
      suma = 0
      for i in range(6):
         if i == 2:
            continue
         if i % 2 == 1:
            suma += i % 2
         else:
            suma -= 1
      print("Resultat final:", suma)
   ```

   - a) -1
   - b) 0
   - c) 1
   - d) 2

---

\newpage

## Preguntes RA5

21. **Que passaria si el fitxer `fitxer_A.txt` no existeix quan executem el següent codi?**

   ```python
      with open('fitxer_A.txt', 'r') as fitxer_A:
         contingut = fitxer_A.read()
   ```

   - a) El codi capturaria el `FileNotFoundError` i continuaria.
   - b) El codi llançaria un error immediatament i es detindria.
   - c) El codi llegiria un fitxer buit.
   - d) El codi crearia automàticament el fitxer si no existia.

22. **Què passa si intentem obrir un fitxer que no existeix en mode `"x"`?**

   - a) Python llança un `FileNotFoundError`.
   - b) Python crea el fitxer correctament.
   - c) Python llança un `PermissionError`.
   - d) Python obri el fitxer en mode només lectura.


23. **Com capturaríeu una excepció d'entrada/eixida i treball amb fitxers que no siga una excepció coneguda com a `ValueError` o `TypeError`?**

   - a) Utilitzant un `try`/`except` per capturar `IOError`.
   - b) Utilitzant `assert` dins de la secció `try`.
   - c) Capturant qualsevol excepció genèrica amb `except Exception`.
   - d) Creant una excepció personalitzada amb `raise`.

24. **Quin tipus d'excepció es llançarà si intentem escriure en un fitxer en mode de només lectura?**

   ```python
      with open("exemple.txt", "r") as f:
      f.write("Hola món")
   ```

   - a) `FileNotFoundError`
   - b) `PermissionError`
   - c) `ValueError`
   - d) `TypeError`

\newpage

25. **Quina funció del mòdul `json` s’utilitza per llegir dades d’un fitxer JSON?**

   - a) `json.read()`
   - b) `json.start()`
   - c) `json.load()`
   - d) `json.open()`


26. **Quin mètode llegeix tot el contingut d’un fitxer d’una sola vegada?**

   - a) `readline()`
   - b) `readlines()`
   - c) `readAll()`
   - d) `read()`

27. **Què passa si obrim un fitxer en mode `'w'` i el fitxer ja existeix?**

   - a) Python llança un error
   - b) El contingut s’afegeix al final
   - c) El contingut es sobrescriu
   - d) El fitxer no es modifica

28. **Què passarà quan s’executa aquest programa si l’usuari introdueix "hola" com a edat?**

   ```python
      nom = input("Nom: ")
      edat = input("Edat: ")

      print(f"Hola {nom}, l'any que ve tindràs {edat + '1'} anys.")

   ```

   - a) Mostra: Hola <nom>, l'any que ve tindràs hola1 anys.
   - b) Mostra un ValueError perquè no es pot convertir "hola" a enter
   - c) Mostra només el nom i ignora l’edat
   - d) Mostra un TypeError perquè no es poden sumar edat i 1

\newpage

29. **Què passarà si el fitxer "dades.txt" no existeix quan s’executa aquest codi?**

   ```python
      try:
         with open("dades.txt", "r") as f:
            contingut = f.read()
            print("Contingut:", contingut.upper())
      except FileNotFoundError:
         print("Fitxer no trobat!")
   ```
   - a) Es crearà automàticament el fitxer i mostrarà un contingut buit
   - b) Es mostrarà el missatge: Fitxer no trobat!
   - c) Es produirà un PermissionError
   - d) Mostrarà un error de sintaxi


30. **Què farà aquest codi si el fitxer "noms.txt" existeix i conté les línies:**

   ```
   Joan
   Maria
   Pepe
   ```

   ```python
      try:
         with open("noms.txt", "r") as f:
            for linia in f:
                  print(linia.upper())
      except Exception as e:
         print("Error:", e)
   ```

   - a) Mostra cada nom en majúscules.
   - b) Mostra cada nom en la primera lletra en majúscula.
   - c) Llença un ValueError perquè no podem fer upper() a la linia.
   - d) No mostra res perquè cal utilitzar readlines().

\newpage

# Preguntes RA3: 0 - 20

# Preguntes RA5: 21 - 30

# Taula de Respostes (SOLS S'AVALUARAN LES RESPOSTES PRESENTS EN ESTA TAULA)

\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\hline
\rule{0pt}{1.5cm} & & & & & & & & & \\
\hline
\end{tabular}
\end{table}


\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 \\
\hline
\rule{0pt}{1.5cm} & & & & & & & & & \\
\hline
\end{tabular}
\end{table}

\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
21 & 22 & 23 & 24 & 25 & 26 & 27 & 28 & 29 & 30 \\
\hline
\rule{0pt}{1.5cm} & & & & & & & & & \\
\hline
\end{tabular}
\end{table}
