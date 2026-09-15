
# Llistes

Les **llistes** són una estructura de dades molt important en Python. Permeten emmagatzemar més d'un element en una sola variable. A continuació, explorarem com crear i manipular llistes en Python.

---

## 1. Creació i manipulació de llistes

Una **llista** en Python és una col·lecció ordenada de valors, que poden ser de tipus de dades diversos (números, cadenes, altres llistes, etc.). Les llistes es creen amb corxets (`[]`).

### Exercici 2.1 - Crear una llista i accedir als seus elements

Crea un programa que:

1. Creï una llista amb els teus tres aliments preferits.
2. Impri el primer i l'últim element de la llista.

```python
# Crear una llista
aliments = ["pa", "formatge", "tomàquet"]

# Accedir als elements
primer = aliments[0]
ultim = aliments[-1]

# Mostrar els resultats
print(f"Primer aliment: {primer}")
print(f"Últim aliment: {ultim}")
```

---

## 2. Modificar llistes

Les llistes també permeten modificar els elements que contenen. Pots afegir, eliminar o modificar elements de la llista.

### Exercici 2.2 - Afegir i eliminar elements d'una llista

Crea un programa que:

1. Afegixi un nou aliment a la llista.
2. Elimini el segon aliment de la llista.
3. Impri la llista resultant.

```python
# Afegir un aliment a la llista
aliments.append("pernil")

# Eliminar el segon aliment
del aliments[1]

# Mostrar la llista actualitzada
print("Llista d'aliments actualitzada:", aliments)
```

### Pregunta:

- Què creus que passaria si utilitzes un índex que no existeix a la llista? Prova-ho i observa el resultat.

---

## Conclusió

Ara ja saps com treballar amb **llistes** en Python: crear-les, accedir als seus elements i modificar-les. Aquesta estructura de dades és molt útil quan necessites emmagatzemar múltiples elements en una sola variable.

---
