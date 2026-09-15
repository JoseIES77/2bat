
# Pràctica Final - Introducció a Python

Aquesta pràctica final t'ajudarà a consolidar els coneixements adquirits fins ara. Resol els exercicis següents, que integren els conceptes clau com **números**, **textos**, **llistes**, **funcions**, **operadors** i **expressions**.

---

## 1. Operacions amb números i textos

### Exercici 1.1 - Calculadora simple

Crea un programa que permeti a l'usuari realitzar operacions aritmètiques simples. El programa ha de fer el següent:

1. Demanar a l'usuari dos números (enter i flotant).
2. Mostrar el resultat de la suma, resta, multiplicació, divisió, divisió entera i mòdul entre els dos números.
3. Realitzar la **concatenació de cadenes de text** i mostrar un missatge com a resultat.

```python
# Pista: Utilitza la funció `input()` per obtenir dades de l'usuari i converteix-les amb `int()` o `float()`
```

### Exercici 1.2 - Comparar dos números

1. Demanar dos números a l'usuari.
2. Comprovar si el primer número és més gran que el segon, si són iguals o si el primer és menor que el segon.
3. Mostrar el resultat amb un missatge clar, utilitzant operadors de comparació.

---

## 2. Llistes i manipulació de dades

### Exercici 2.1 - Llista d'estudiants

1. Crea una llista amb els noms de 5 estudiants.
2. Afegir un nou estudiant a la llista.
3. Eliminar el segon estudiant de la llista.
4. Imprimir la llista completa després de cada operació.

---

## 3. Funcions

### Exercici 3.1 - Funció de salutació

1. Crea una funció que rebi el nom de l'usuari com a paràmetre i imprimeixi una salutació personalitzada.
2. Crida aquesta funció amb diferents noms i observa el resultat.

### Exercici 3.2 - Funció per calcular l'àrea d'un cercle

1. Crea una funció que rebi el radi d'un cercle i retorni l'àrea.
2. Demana a l'usuari el radi del cercle i imprimeix l'àrea calculada.

### Exercici 3.3 - Funció amb valor per defecte

1. Crea una funció que sumi dos números. Assigna un valor per defecte al segon número, de manera que si no es passa un segon valor, la funció utilitze aquest valor per defecte.
2. Crida la funció amb un sol valor i amb dos valors, i observa els resultats.

---

## 4. Operadors i expressions

### Exercici 4.1 - Operadors aritmètics i lògics

1. Crea una variable `x` amb valor `10` i una altra `y` amb valor `5`.
2. Realitza les següents operacions:
   - Suma, resta, multiplicació, divisió i mòdul entre `x` i `y`.
   - Comprova si `x` és més gran que `y` i imprimeix el resultat.
   - Comprova si `x` és igual a `y` i imprimeix el resultat.

3. Utilitza operadors lògics per combinar les condicions. Comprova si `x` és més gran que `y` **i** si el mòdul de `x` és 0. Imprimeix el resultat.

### Exercici 4.2 - Operador `in` i `not in`

1. Crea una llista amb noms de fruits.
2. Demana a l'usuari que introduisca un fruit i comprova si aquest fruit es troba a la llista utilitzant l'operador `in`.
3. Si el fruit no es troba a la llista, utilitza `not in` per mostrar un missatge indicant que el fruit no existeix.

---

## 5. Projecte final - Crear una xicoteta aplicació

### Exercici 5.1 - Calculadora d'IMC (Índex de Massa Corporal)

1. Crea una aplicació que calculi l'IMC d'una persona.
2. Demana a l'usuari el seu pes i la seva alçada.
3. Utilitza la fórmula `IMC = pes / (alçada ** 2)` per calcular l'IMC.
4. Mostra un missatge indicant si l'IMC està dins d'un rang saludable: 
   - **IMC < 18.5**: Inferior al pes saludable.
   - **18.5 <= IMC <= 24.9**: Pes saludable.
   - **IMC > 24.9**: Sobreeiximent de pes.

---

## 6. Què fa aquest codi?

### Exercici 6.1

Què fa el següent codi? Descriu en detall el que fa i el resultat que s'obtindria si l'executessis amb els valors actuals:

```python
a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
if 10 in a:
    b -= 10
if 15 in a:
    b -= 15

print(b)

```

### Exercici 6.2

Què fa el següent codi? Descriu en detall el que fa i el resultat que s'obtindria si l'executessis amb els valors actuals:

```python
a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
elif 10 in a:
    b -= 10
else 15 in a:
    b -= 15

print(b)
```


### Exercici 6.3

Què fa el següent codi? Explica què retornaria si el valor de `n` és 6:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6))
```

---

## 7. Corregeix aquest codi

### Exercici 7.1

El següent codi té un error. Troba'l i corregeix-lo:

```python
x = 10
y = 5

if x = y:
    print("Són iguals")
else:
    print("Són diferents")
```

### Exercici 7.2

El següent codi presenta un error al treballar amb llistes. Troba l'error i corregeix-lo:

```python
llista = [1, 2, 3, 4, 5]
print(llista[5])
```


### Exercici 8

Crea el teu repository a Github anomenat "IPRG_2526".

Una vegada creat, hauràs de pujar a ell una carpeta anomenada "Exercicis_UD1" amb tots els exercicis que hem fet.

---

# Avaluació i Criteris de Qualificació

| Exercici                                | Criteri de Qualificació | Ítem d'Avaluació Específic | Rúbrica de Puntuació (0-10) | Nota (0-10) |
|-----------------------------------------|-------------------------|----------------------------|----------------------------|-------------|
| **Gral.**                               | RA1.c) Ús d'entorns integrats de desenrotllament. | Execució i proves dins de l'IDE. | El programa s'executa correctament i es fa servir l'entorn de forma bàsica. | |
| **Gral.**                               | RA1.b) Creació de projectes de desenrotllament d’aplicacions. | Estructura d'arxius i del repositori. | Es crea el projecte/arxiu principal i es guarda en una estructura lògica. (Complementat per Ej. 8) | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 1.1 Calculadora simple                  | RA1.g) Ús dels operadors del llenguatge. | Aplicació dels 6 operadors aritmètics i l'operador de concatenació. | S'utilitzen correctament +, -, *, /, //, % i la concatenació de cadenes. | |
| 1.1 Calculadora simple                  | RA1.e) Modificació de codi per crear i utilitzar variables. | Declaració i ús de variables per a emmagatzemar entrades i resultats. | S'assignen i manipulen variables per als números i el text de manera efectiva. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 1.2 Comparar dos números                | RA1.g) Ús dels operadors del llenguatge. | Ús correcte d'operadors de comparació. | S'utilitzen de forma adequada els operadors de comparació (>, <, ==). | |
| 1.2 Comparar dos números                | RA1.d) Identificació dels diferents tipus de variables. | Conversió de les entrades de l'usuari als tipus numèrics adequats. | S'aplica correctament la conversió de l'entrada de text a tipus numèric (p. ex., amb int() o float()). | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 2.1 Llista d'estudiants                 | RA1.a) Identificació dels blocs de l'estructura. | Ús i manipulació de llistes com a estructura de dades. | Es crea i es manipula la llista mitjançant mètodes com append() (afegir) i pop() o del (eliminar). | |
| 2.1 Llista d'estudiants                 | RA1.e) Modificació de codi per crear i utilitzar variables. | Manipulació de l'estat d'una variable composta (llista). | La llista es crea i es modifica d'acord amb els 3 passos de l'exercici (crear, afegir, eliminar). | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 3.1 Funció de salutació                 | RA1.a) Identificació dels blocs de l'estructura. | Definició i crida d'una funció sense retorn (def). | La funció es defineix amb paràmetres i es crida de forma correcta. | |
| 3.1 Funció de salutació                 | RA1.i) Introducció de comentaris en el codi. | Inclusió de comentaris per descriure la funció. | S'afegeix un comentari (# o docstring) explicant l'objectiu de la funció o el seu ús. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 3.2 Funció per calcular l'àrea          | RA1.f) Creació i ús de constants i literals. | Ús de la constant π o un literal numèric. | Es defineix i utilitza un valor constant per a π o s'utilitza el literal correcte en la fórmula. | |
| 3.2 Funció per calcular l'àrea          | RA1.a) Identificació dels blocs de l'estructura. | Funció amb càlcul i retorn de valor (return). | La funció realitza el càlcul de l'àrea i retorna el resultat correcte. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 3.3 Funció amb valor per defecte        | RA1.d) Identificació dels diferents tipus de variables. | Implementació d'un paràmetre amb valor per defecte. | El segon paràmetre de la funció té un valor assignat per defecte (p. ex., def suma(a, b=0):). | |
| 3.3 Funció amb valor per defecte        | RA1.e) Modificació de codi per crear i utilitzar variables. | Crida de la funció amb un sol argument i amb dos. | La funció es prova amb èxit en tots dos escenaris (amb i sense el valor per defecte). | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 4.1 Operadors aritmètics i lògics       | RA1.g) Ús dels operadors del llenguatge. | Combinació d'operadors aritmètics, de comparació i lògics. | S'utilitzen +, -, *, /, %, >/== i l'operador lògic and per a una expressió composta. | |
| 4.1 Operadors aritmètics i lògics       | RA1.e) Modificació de codi per crear i utilitzar variables. | Ús de variables per emmagatzemar els resultats booleans. | Es creen variables per x i y, i s'utilitzen en les expressions complexes. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 4.2 Operador in i not in                | RA1.g) Ús dels operadors del llenguatge. | Ús correcte dels operadors de pertinença (in i not in). | Es comprova la presència/absència d'un element en una llista utilitzant ambdós operadors. | |
| 4.2 Operador in i not in                | RA1.a) Identificació dels blocs de l'estructura. | Ús de llistes i expressions condicionals basades en la pertinença. | Es fa servir una llista com a context de cerca i les expressions es resolen correctament. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 5.1 Calculadora d'IMC                   | RA1.h) Funcionament de conversions de tipus. | Conversió de text a numèric i gestió de la sortida. | Es converteixen les entrades (pes, alçada) a float abans de calcular l'IMC. | |
| 5.1 Calculadora d'IMC                   | RA1.e) Modificació de codi per crear i utilitzar variables. | Ús de variables per emmagatzemar l'IMC i utilització en condicions. | S'utilitzen variables per a pes, alçada, IMC i s'avaluen en la lògica condicional. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| "6.1, 6.2, 6.3 Descripció de codi"      | RA1.a) Identificació dels blocs de l'estructura. | Descripció detallada del funcionament (if/elif/else, recursivitat). | S'identifiquen correctament les estructures i es prediu el resultat del codi amb precisió. | |
| "6.1, 6.2, 6.3 Descripció de codi"      | RA1.e) Modificació de codi per crear i utilitzar variables. | Traçabilitat i seguiment del valor de les variables. | S'explica com el valor de variables com b o n canvia al llarg de l'execució del codi. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 7.1 Corregeix el codi (Comparació)      | RA1.e) Modificació de codi per crear i utilitzar variables. | Correcció de l'error de sintaxi d'assignació vs. comparació (= vs. ==). | S'identifica l'error if x = y: i es corregeix a if x == y:. | |
| 7.1 Corregeix el codi (Comparació)      | RA1.i) Introducció de comentaris en el codi. | Ús de comentaris per justificar la correcció. | S'afegeix un comentari (#) per explicar la diferència entre = i ==. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 7.2 Corregeix el codi (Llista)          | RA1.e) Modificació de codi per crear i utilitzar variables. | Correcció de l'error de lògica d'índexs de llista. | S'identifica l'error d'índex fora de rang (llista[5]) i es corregeix a un índex vàlid (p. ex., llista[4]). | |
| 7.2 Corregeix el codi (Llista)          | RA1.d) Identificació dels diferents tipus de variables. | Demostració de la comprensió de la indexació de llistes (tipus estructurat). | La correcció reflecteix que els índexs de llista comencen per 0 i que l'índex màxim és longitud - 1. | |
| ---                                     | ---                     | ---                        | ---                        | ---         |
| 8 Projecte final (Git)                  | RA1.b) Creació de projectes de desenrotllament d’aplicacions. | Creació i organització del repositori a Github. | El repositori existeix amb el nom correcte i conté la carpeta Exercicis_UD1 amb els arxius. | |
| 8 Projecte final (Git)                  | RA1.i) Introducció de comentaris en el codi. | Inclusió d'un README.md o missatges de commit clars. | Es crea el repositori amb almenys un missatge de commit coherent, demostrant traçabilitat del codi. | |

[Rubrica d'avaluació](./Correccio_Practica/Rubrica_PracticaFinal_IPRG2.xlsx)