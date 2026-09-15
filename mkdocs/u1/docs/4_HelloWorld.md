
# Introducció a Python: Consola i VSCode

En aquest apartat, aprendràs a treballar amb la consola de Python i amb l'editor de codi **VSCode**. Començarem amb els conceptes bàsics per tal que et familiaritzis amb la sintaxi i la manera d'executar programes simples.

## 1. L'origen de "Hello, World!"

La primera vegada que es va utilitzar el "Hello, World!" va ser en el llibre "The C Programming Language" de Brian Kernighan i Dennis Ritchie (1978). Aquest llibre, que va ser la guia introductòria al llenguatge de programació C, va fer que el programa de "Hello, World!" es convertís en un exemple clàssic per a introduir nous conceptes en la programació.

En aquell moment, el programa es veia així:
```c
#include <stdio.h>

main() {
    printf("Hello, World!\n");
}
```

Aquest programa imprimia el missatge "Hello, World!" a la pantalla, i es va escollir perquè era un exemple senzill que permetia a les persones familiaritzar-se amb la sintaxi bàsica del llenguatge, com la inclusió de biblioteques, la funció principal i la impressió a la pantalla.

El motiu principal per fer aquest programa és simple i efectiu: ens permet veure si l'entorn de programació està configurat correctament. Quan executes un programa de "Hello, World!", estàs fent algunes coses molt bàsiques que s'han de configurar correctament abans de fer qualsevol projecte més complex:

- Comprovar que el compilador o intèrpret funciona: Si el programa es pot compilar i executar, vol dir que l'entorn de desenvolupament funciona bé.

- Familiarització amb la sintaxi del llenguatge: Quan estàs aprenent un nou llenguatge, és una manera senzilla de veure com es fa servir la sintaxi bàsica, com es defineixen funcions, com s'utilitza l'output de la consola, etc.

- Primera experiència amb l'execució de codi: És un bon primer pas per a aquells que comencen en la programació, ja que proporciona una experiència pràctica de veure un programa funcional en acció sense complicacions.


---

## 2. Treballar amb la Consola de Python

La consola de Python et permet escriure i executar codi Python directament des de la terminal. És un entorn ideal per començar a practicar amb el llenguatge sense necessitat d'un editor de codi complet.

### Exercici 2.1 - Iniciar la consola de Python

Per iniciar la consola de Python, obre una terminal i escriu:

```bash
python3
```

Quan ho facis, hauràs de veure un símbol de Python (>>>), indicant que la consola està llesta per rebre ordres.

#### Què pots fer aquí?

A la consola de Python, pots escriure expressions simples i veure els resultats immediatament. Prova els següents exemples:

- Suma de dos números:

```python
>>> 2 + 3
5
```

- Assignar un valor a una variable i mostrar-lo:

```python
>>> nom = "Hola, món!"
>>> nom
'Hola, món!'
```

!!! note "Pregunta"

    - Quina diferència hi ha entre escriure expressions directament a la consola i escriure-les en un fitxer Python? Quan creus que és més útil una opció que l'altra?

---

## 3. Treballar amb VSCode

**VSCode** és un editor de codi molt popular que et permet escriure codi Python d'una manera més còmoda i organitzada. A continuació, et mostrarem com configurar-lo i fer el teu primer programa.

### Instal·lar i configurar VSCode

1. **Descarrega i instal·la VSCode**:
   - Pots descarregar-lo des de [Visual Studio Code](https://code.visualstudio.com/).

2. **Instal·lar l'extensió de Python**:
   - Un cop instal·lat, obre VSCode i ves a la secció d'extensions (a la barra lateral esquerra).
   - Cerca l'extensió de **Python** i instal·la-la.

3. **Configurar Python a VSCode**:
   - Un cop instal·lada l'extensió, obre un fitxer Python (`.py`) i VSCode hauria de detectar automàticament la versió de Python que tens instal·lada.

### Exercici 3.1 - Escriure el teu primer programa

Obre VSCode i crea un nou fitxer anomenat `hello_world.py`. A continuació, escriu el següent codi:

```python
# Programa: Hello, World!
print("Hello, World!")
```

Després, guarda el fitxer i executa'l.

- Per executar el codi, obre la terminal de VSCode (a baix) i escriu:

```bash
python3 hello_world.py
```

Després de fer-ho, hauries de veure l'eixida:

```
Hello, World!
```

!!! note "Pregunta"

    - Què creus que fa la funció `print()`? Quin tipus de dades pots imprimir amb ella?

---

## 4. Estructures bàsiques de Python

Ara que has escrit i executat el teu primer programa, és hora de començar a jugar amb algunes estructures bàsiques de Python. Les següents accions t'ajudaran a entendre millor el funcionament de les variables i operacions bàsiques.

### Exercici 4.1 - Variables i operacions

Obre un nou fitxer a VSCode anomenat `operacions.py` i escriu el següent codi:

```python
# Variables i operacions
a = 5
b = 3

# Operacions matemàtiques
suma = a + b
resta = a - b
multiplicacio = a * b
divisio = a / b

# Mostrar els resultats
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicació:", multiplicacio)
print("Divisió:", divisio)
```

Un cop hagis escrit aquest codi, guarda i executa el fitxer.

!!! note "Pregunta"

    - Què passaria si canviessis el valor de `a` o `b` per altres nombres? Prova-ho i observa com canvien els resultats.

---

## 5. Comprovar tipus de dades

Python permet treballar amb diversos tipus de dades com enters (`int`), decimals (`float`), cadenes de text (`str`), i booleans (`bool`). 

### Exercici 5.1 - Tipus de dades

Crea un nou fitxer anomenat `tipus_dades.py` i escriu el següent codi:

```python
# Tipus de dades
enter = 10         # Enter
decimal = 3.14     # Decimal (float)
text = "Python"    # Cadena de text (str)
boolea = True      # Boolean (True o False)

# Mostrar els tipus de dades
print("Enter:", enter)
print("Decimal:", decimal)
print("Text:", text)
print("Booleà:", boolea)
```

Després, guarda i executa el fitxer.

!!! note "Pregunta"

    - Què creus que passaria si intentessis sumar una cadena de text amb un número? Prova-ho i observa els resultats.

---

## Conclusió

Amb aquests exercicis, ja hauràs après a utilitzar la consola de Python per executar codi de manera ràpida, així com a treballar amb l'editor VSCode per escriure programes més organitzats. La propera vegada, explorarem operacions més avançades i estructures de control.

---
