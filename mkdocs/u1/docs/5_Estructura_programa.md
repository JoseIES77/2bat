
# Estructura bàsica d'un programa en Python

Abans de començar a escriure programes més complets, és important entendre l'estructura bàsica d'un programa en Python. Això inclou com escriure un programa simple i entendre els elements que el composen.

---

## 1. Estructura d'un programa Python

Un programa en Python es compon bàsicament de les següents parts:

### 1.1 **Comentaris**

Els comentaris s'utilitzen per explicar el codi. Els comentaris no s'executen i serveixen per fer que el codi sigui més comprensible. Es poden escriure de dues maneres:
- **Comentaris de línia**: S'usen el símbol `#` per a comentar una línia.
- **Comentaris de bloc**: S'escriuen entre triples cometes ('''...''') per comentar múltiples línies de codi.

### 1.2 **Importacions**

Si un programa necessita biblioteques externes (mòduls), aquestes es poden importar amb la paraula clau **`import`**.

```python
import math  # Importar el mòdul math per utilitzar funcions matemàtiques
```

### 1.3 **Funcions**

Les funcions permeten agrupar codi que es pot reutilitzar, evitant la repetició. Es defineixen amb la paraula clau **`def`**.

```python
def saludar():
    print("Hola!")
```

### 1.4 **Codi executat i mètode `main`**

Quan un programa en Python es llança, l'execució comença des de la part superior del codi. No obstant això, si volem estructurar millor el codi i evitar que s'executi automàticament quan el mòdul es carrega, utilitzem una estructura especial amb el mètode **`main`**.

Un mètode `main` és una funció especial que conté la lògica principal d'un programa i es crida només quan el programa s'executa directament, no quan es importa com a mòdul en altres programes.

#### Exemple de flux d'execució amb el mètode `main`:

```python
# Definir una funció
def calcular_area_cercle(radius):
    area = math.pi * (radius ** 2)
    return area

# Codi principal
if __name__ == "__main__":  # Comprova si el programa es llança directament
    radi = float(input("Introdueix el radi del cercle: "))  # Sol·licitem l'entrada de l'usuari
    area = calcular_area_cercle(radi)  # Cridem la funció per calcular l'àrea
    print(f"L'àrea del cercle és: {area}")
```

**Explicació de l'exemple**:
- **`if __name__ == "__main__":`** és una condició que verifica si el codi s'està executant directament. Això permet que el codi dins de `main` només s'executi quan el programa es llança directament, no quan es fa servir com a mòdul.
- **`calcular_area_cercle(radi)`** és una funció que rep el radi i retorna l'àrea del cercle, utilitzant la constant `math.pi` del mòdul **math**.

---

## 2. La importància de la indentació

Python utilitza la **indentació** per definir blocs de codi. Això vol dir que els blocs de codi dins de funcions, condicions, bucles i altres estructures es defineixen mitjançant espais o tabuladors. A diferència d'altres llenguatges de programació que utilitzen claus (`{}`), Python depèn de la indentació per determinar què forma part d'un bloc de codi.

### 2.1 **Indentació incorrecta**:

```python
# Incorrecte
def saludar():
print("Hola!")  # Error d'indentació!
```

### 2.2 **Indentació correcta**:

```python
# Correcte
def saludar():
    print("Hola!")  # La indentació és important!
```

A la segona versió, el **bloc de codi** que pertany a la funció `saludar()` s'indenta amb un espai o tabulador, indicant que aquesta línia forma part de la funció.

---

## 3. Flux d'execució del programa

Quan s'executa un programa en Python, el flux d'execució segueix un ordre lineal a menys que es faci servir algun tipus de control de flux (com condicions o bucles). El flux d'execució es defineix en tres parts principals:

1. **Les funcions**: El codi que es troba dins d'una funció no s'executa fins que la funció sigui cridada.
2. **Condicions (`if`, `elif`, `else`)**: El flux es modifica en funció de les condicions.
3. **Bucles (`for`, `while`)**: Els bucles permeten repetir codi fins que es compleixi una condició.

**Exemple de flux d'execució amb condició i bucle**:

```python
# Funció principal
def main():
    x = 5
    if x > 3:
        print("x és més gran que 3.")

    # Bucle
    for i in range(3):
        print(f"Iteració {i}")

# Condició per executar la funció main
if __name__ == "__main__":
    main()
```

**Explicació**:
- El flux d'execució comença al mètode `main` gràcies a la línia `if __name__ == "__main__":`.
- Primer es comprova la condició `if x > 3:`, que imprimeix un missatge si és certa.
- Després, s'executa un bucle `for` que imprimeix "Iteració" i el valor de `i` per a cada pas.

---

## **Conclusió**

Ara ja coneixes l'estructura bàsica d'un programa Python, el flux d'execució i la importància de la indentació. També has après a utilitzar el mètode `main` per controlar l'execució del teu codi. Amb aquesta comprensió bàsica, estàs llest per començar a escriure programes més complexos i organitzats.