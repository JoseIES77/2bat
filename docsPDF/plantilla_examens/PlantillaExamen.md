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
    \textbf{\textit{\Large Examen 1a Avaluació - UD2-UD3 - RA3-RA5}}
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


1. **Quina serà l'eixida per pantalla d'aquest codi?**
   
      ```python
      def suma(a, b):
         return a + b

      resultat = suma(4, 5)
      print("El resultat és:", resultat)
      ```
   - a) El resultat és: 9
   - b) El resultat és: 45
   - c) El resultat és: None
   - d) El resultat és: 4


2. **Què farà el següent codi si s'executa?**
 
      ```python
      def salutacio(nom="Usuari"):
         return f"Hola, {nom}!"

      print(salutacio())
      print(salutacio("Joan"))
      ```
   - a)  Hola, Usuari!
         Hola, Joan!
   - b)  Usuari
         Joan
   - c)  Hola, None!
         Hola, Joan!
   - d)  Error


3. **Què farà el següent codi?**

      ```python
      llista = [10, 20, 30, 40]
      llista[2] = 35
      print(llista)
      ```
   - a)  [10, 20, 30, 40]
   - b)  [10, 20, 35, 40]
   - c)  [35, 20, 30, 40]
   - d)  [10, 20, 40, 35]


\newpage

4. **Què farà aquest codi?**

      ```python
      llista = ["pa", "formatge", "tomàquet"]
      llista.append("pernil")
      del llista[1]
      print(llista)
      ```
   - a)  ['pa', 'tomàquet', 'pernil']
   - b)  ['pa', 'formatge', 'tomàquet', 'pernil']
   - c)  ['formatge', 'tomàquet', 'pernil']
   - d)  ['pa', 'pernil', 'tomàquet']



5. **Quina serà l'eixida del següent codi?**
   
      ```python
      x = 5
      y = 2
      z = x ** y
      print(z)
      ```
   - a)  7
   - b)  25
   - c)  10
   - d)  2


6. **Quina instrucció s'utilitza per eixir d'un bucle `while` abans que la condició siga falsa?**
   - a) `continue`
   - b) `pass`
   - c) `break`
   - d) `exit`

7. **Quina afirmació és certa sobre les assercions en Python?**
   - a) Les assercions llançaran errors sempre que una condició falli.
   - b) Les assercions es poden desactivar en mode de producció per millorar el rendiment.
   - c) Les assercions es poden utilitzar per capturar excepcions específiques.
   - d) Les assercions no es poden utilitzar per verificar condicions internes al codi.

\newpage

8. **Quina serà l'eixida del següent codi?**
   
      ```python
      x = 5
      y = 10
      if x < y:
         z = x * 2
      else:
         z = y / 2
      print(z)
      ```
   - a) 10
   - b) 2.0
   - c) 5
   - d) 20

9.  **Quina és la funció principal d'un bloc `try`/`except` en Python?**
   - a) Depurar errors lògics
   - b) Manipular el flux de control
   - c) Capturar i manejar assercions
   - d) Cap és certa

10. **Què fa l'excepció `ValueError` en Python?**
   - a) Es produeix quan intentem accedir a una llista amb un índex que no existeix.
   - b) Es produeix quan intentem convertir una cadena no numèrica a un enter.
   - c) Es produeix quan intentem dividir un nombre per zero.
   - d) Es produeix quan intentem capturar una asserció que no té valor.

11. **Com es pot evitar que un codi es "bote" una iteració de bucle quan s'ha complert una condició?**
   - a) Usant `pass`
   - b) Usant `break`
   - c) Usant `continue`
   - d) Usant `exit`

\newpage

12. **Què fa el mètode `input()` a Python?**
   - a) Demana dades a l'usuari i retorna un valor enter.
   - b) Demana dades a l'usuari i retorna un valor com a cadena de text.
   - c) Llegeix el contingut d'un fitxer.
   - d) S'utilitza per imprimir resultats per pantalla.

13. **Quina és l'eixida del següent codi?**
    
      ```python
      for i in range(3, 8):
         print(i)
      ```
   - a) 3 4 5 6 7 8
   - b) 3 4 5 6 7
   - c) 1 2 3 4 5
   - d) Cap és correcta

14. **Quina afirmació és correcta sobre les excepcions?**
   - a) Les excepcions es poden capturar només dins de bucles.
   - b) Quan una excepció es llança, l'execució del programa es deté immediatament si no es captura.
   - c) Les excepcions són útils per controlar les condicions de l'usuari.
   - d) Les excepcions es poden capturar amb `assert`.

15. **Com es pot eixir d'un bucle `while` ?**
   - a) Amb `break`
   - b) Amb `continue`
   - c) Amb `pass`
   - d) Amb `exit`

16. **Quina serà l'eixida d'aquest codi?**
    
      ```python
      x = 0
      assert x => 0, "El valor ha de ser positiu"
      ```
   - a) `El valor ha de ser positiu`
   - b) No surt cap error
   - c) `AssertionError: El valor ha de ser positiu`
   - d) `ValueError: El valor ha de ser positiu`

\newpage

17.  **En quina situació s'utilitza el mètode `finally` dins de l'estructura `try`/`except`?**
   - a) Per capturar excepcions
   - b) Per garantir que el codi que conté s'executi sempre
   - c) Per definir l'error que es llançarà
   - d) Per executrar quan finalitza el codi

18.  **Quina eixida per pantalla produeix este codi `if`/`elif`/`else`?**

      ```python
      x=2
      y=1

      if(x==2):
      print("Hola X")

      if(y==1):
      print("Hola Y")

      elif(x==2):
      print("Hola de nou X")

      else:
      print("Adéu")

      ```

   - a) Hola X / Hola Y
   - b) Hola X / Hola Y / Hola de nou Y
   - c) Hola X / Adéu
   - d) Cap és correcta

19.    **Quina serà l'eixida del següent codi?**

   ```python
      for i in range(3, 6):
            print(i)
   ```    

   - a) 3 4 5 6
   - b) 0 1 2 3 4 5
   - c) 3 4 5 
   - d) 3 4

\newpage

20.    **Com canvien les variables durant les iteracions 2 i 3 d'aquest codi? Completa la taula de traça.**
    
   ```python
      suma = 0
      for i in range(1, 6):
         if i % 2 == 0:
            suma += i
         else:
            suma -= 1
      print("Resultat final:", suma)
   ```

| Iteració (`i`) | Condició `i % 2 == 0` | Valor de `suma` | Valor de `i` |
| -------------- | --------------------- | --------------- | ------------ |
| 2              |                       |                 |              |
| 3              |                       |                 |              |



21.   **Quina serà l'eixida d'aquest codi?**
   
   ```python
      num = 5
      print("El número és: " + num)
   ```
   - a) El número és: 5
   - b) El número és: `Error`
   - c) `TypeError: can only concatenate str (not "int") to str`
   - d) El número és: num

22.  **Què fa el següent codi?**
   
   ```python
      with open('fitxer_A.txt', 'r') as fitxer_A:
         contingut = fitxer_A.read()

      with open('fitxer_B.txt', 'w') as fitxer_B:
         fitxer_B.write(contingut)
   ```
   - a) El codi llegeix el fitxer B i afegeix el contingut a un altre fitxer.  
   - b) El codi llegeix el contingut d'el fitxer A i el copia a un nou fitxer.  
   - c) El codi crea un fitxer de text amb el contingut llegit del fitxer B. 
   - d) El codi copia el fitxer font al destí mantenint l'estructura original.  

\newpage

23. **Quin error es produeix si intentem obrir un fitxer en mode de lectura (`'r'`) que no existeix?**
   - a) `FileIndexError`  
   - b) `PermissionError`  
   - c) `ValueError`  
   - d) Cap és correcta

24. **Quina diferència hi ha entre obrir un fitxer amb mode 'x' i amb mode 'w'?**

   - a) El mode 'w' llança un error si el fitxer ja existeix, mentre que el mode 'x' el sobreescriu.
   - b) El mode 'w' crea un fitxer nou si no existeix, mentre que el mode 'x' llança un error si el fitxer ja existeix.
   - c) El mode 'x' crea un fitxer nou i l'obre per escriptura, mentre que el mode 'w' només el llegeix.
   - d) No hi ha cap diferència entre els dos modes, són exactament iguals.

25. **Què fa el següent codi quan intenta llegir un fitxer que no existeix?**

      ```python
         try:
            with open('document_no_existent.txt', 'r') as fitxer:
               contingut = fitxer.read()
         except PermissionError:
            print("El fitxer no existeix.")
         else:
            print("Fitxer llegit correctament.")
         finally:
            print("Operació de fitxer acabada.")

      ```

   - a) El codi llançarà un error específic i imprimirà el missatge "S'ha produït un error."
   - b) El codi captura qualsevol error general i imprimeix "S'ha produït un error."
   - c) El codi intentaria llegir el fitxer correctament i imprimira "Fitxer llegit correctament."
   - d) El codi imprimiria només "Operació de fitxer acabada."

\newpage

# Preguntes RA3: 0 - 20

# Preguntes RA5: 21 - 25

# Taula de Respostes (SOLS S'AVALUARAN LES RESPOSTES PRESENTS EN ESTA TAULA)

\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\hline
 &  &  &  &  &  &  &  &  &  \\
\hline
\end{tabular}
\end{table}


\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 \\
\hline
 &  &  &  &  &  &  &  &  &  \\
\hline
\end{tabular}
\end{table}


\begin{table}[h!]
\centering
\begin{tabular}{|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|p{1.2cm}|}
\hline
21 & 22 & 23 & 24 & 25 \\
\hline
 &  &  &  &  \\
\hline
\end{tabular}
\end{table}


