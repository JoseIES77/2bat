
# Funcions

Les **funcions** en Python són blocs de codi que realitzen una tasca específica i poden ser reutilitzades diverses vegades al llarg d'un programa. Permeten organitzar el codi de manera més neta i modular, a més de reduir la repetició de codi. A continuació, veurem com definir i utilitzar funcions en Python.

---

## 1. Definició de funcions

Una funció es defineix amb la paraula clau `def`, seguida del nom de la funció i dels paràmetres entre parèntesis. La sintaxi bàsica de la definició d'una funció és la següent:

```python
def nom_funcio(parametre1, parametre2):
    # cos de la funció
    return resultat
```

- **`def`**: Paraula clau per definir la funció.
- **`nom_funcio`**: El nom que donaràs a la teva funció. Els noms de les funcions solen ser descriptius de la tasca que realitzen (ex: `sumar`, `calcular_area`).
- **`parametre1, parametre2`**: Els valors que la funció pot rebre quan es crida. Aquests valors s'anomenen **arguments** o **paràmetres**.
- **`return`**: La paraula clau `return` s'utilitza per enviar un valor de tornada al lloc on es va cridar la funció.

### Exemple de funció simple

A continuació, tens un exemple de funció que rep dos valors, els suma i retorna el resultat:

```python
def suma(a, b):
    return a + b

resultat = suma(5, 3)
print("La suma és:", resultat)  # La suma és: 8
```

En aquest exemple, la funció `suma` rep dos paràmetres (`a` i `b`), els suma i retorna el resultat. La crida a la funció `suma(5, 3)` retorna `8`.

---

## 2. Passant dades a les funcions

Les funcions poden rebre dades mitjançant **paràmetres**. Aquestes dades es poden utilitzar dins de la funció per realitzar operacions. Els paràmetres són com variables locals que només existeixen dins de la funció.

### Exemple: Passar dades a una funció

```python
def saludar(nom):
    return f"Hola, {nom}!"

nom_usuari = "Joan"
missatge = saludar(nom_usuari)
print(missatge)  # Hola, Joan!
```

En aquest cas, el paràmetre `nom` rep el valor de la variable `nom_usuari`. Quan cridem la funció `saludar("Joan")`, el valor de `"Joan"` es passa a la funció, i la funció retorna un missatge de salutació.

---

## 3. Valor de retorn

La paraula clau `return` s'utilitza per enviar un valor de tornada des de la funció al lloc on es va cridar. Si no es fa servir `return`, la funció no retornarà cap valor (per defecte retorna `None`).

### Exemple de funció amb retorn

```python
def multiplicar(a, b):
    return a * b

resultat = multiplicar(4, 5)
print(resultat)  # 20
```

En aquest cas, la funció `multiplicar` rep dos paràmetres, els multiplica i retorna el resultat. Quan cridem `multiplicar(4, 5)`, la funció retorna `20`, que es guarda a la variable `resultat`.

---

## 4. Funcions amb valors per defecte

A vegades, és útil assignar un **valor per defecte** a un paràmetre en cas que no es passi un valor. Això es pot fer a l'hora de definir la funció.

### Exemple: Funció amb valor per defecte

```python
def saludar(nom="Usuari"):
    return f"Hola, {nom}!"

print(saludar())  # Hola, Usuari!
print(saludar("Joan"))  # Hola, Joan!
```

En aquest exemple, si no es passa un nom a la funció, es fa servir el valor per defecte `"Usuari"`. Si es passa un nom, aquest substitueix el valor per defecte.

---

## 5. Funcions recursives

Una **funció recursiva** és una funció que es crida a si mateixa per resoldre un problema. Les funcions recursives són útils per resoldre problemes que poden ser descomposats en subproblemes més petits. Un exemple clàssic de funció recursiva és el càlcul del **factorial** d'un nombre.

### Exemple: Funció recursiva

El factorial d'un número `n` es defineix com el producte de tots els nombres enters des de `1` fins a `n`. Per exemple, el factorial de `5` és:

```
5! = 5 * 4 * 3 * 2 * 1 = 120
```

La funció recursiva per calcular el factorial seria la següent:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

En aquest exemple, la funció `factorial` es crida a si mateixa per calcular el factorial de `n`. Quan `n` arriba a `0`, la funció retorna `1` (el cas base), i la recursió es deté.

---

## Conclusió

Les funcions són una eina essencial en Python per organitzar i reutilitzar el codi. Permeten realitzar tasques repetitives, facilitar la lectura i el manteniment del codi, i resoldre problemes complexos de manera eficient (com a les funcions recursives). Ara que saps com crear funcions, passar-hi dades i utilitzar la recursió, estàs preparat per afrontar problemes més complexes amb Python!

---
