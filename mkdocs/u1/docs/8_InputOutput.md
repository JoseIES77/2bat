
# Entrada i Sortida en Python (Teclat i Pantalla)

En aquesta secció aprendrem com interactuar amb l'usuari, per tal d'introduir dades i mostrar-ne el resultat. A Python, utilitzem les funcions **`input()`** per llegir dades del teclat i **`print()`** per mostrar resultats a la pantalla.

---

## **Entrada de dades des del teclat**

Per llegir dades introduïdes per l'usuari a través del teclat, utilitzem la funció **`input()`**. Aquesta funció permet capturar qualsevol tipus d'informació, però sempre retorna el valor com una **cadena de text** (string).

**Sintaxi**:

```python
variable = input("Missatge per a l'usuari: ")
```

On:
- **`"Missatge per a l'usuari"`** és el missatge que es mostrarà per demanar una entrada a l'usuari.
- **`variable`** és on es desarà el valor que l'usuari introdueix.

**Exemple**:

```python
nom = input("Introdueix el teu nom: ")
edat = input("Introdueix la teva edat: ")

print(f"Hola, {nom}! Tens {edat} anys.")
```

En aquest exemple:
- L'usuari introdueix el seu nom i edat.
- El sistema mostra un missatge personalitzat amb les dades introduïdes.

**Nota**: Recorda que **`input()`** sempre retorna un text (string), per tant, si vols treballar amb altres tipus de dades, com números, cal convertir-los:

```python
edat = int(input("Introdueix la teva edat: "))  # Convertim la entrada a enter
```

---

## **Sortida de dades a la pantalla**

Per mostrar informació a l'usuari per pantalla, utilitzem la funció **`print()`**. Aquesta funció permet imprimir qualsevol tipus de dades: textos, números, resultats d'operacions, etc.

**Sintaxi**:

```python
print(dada)
```

On:
- **`dada`** és la informació que volem mostrar a l'usuari.

**Exemple**:

```python
nom = "Joan"
edat = 25
print(f"El meu nom és {nom} i tinc {edat} anys.")
```

En aquest exemple, **`print()`** mostrarà un missatge formatat amb les variables `nom` i `edat`.

També podem mostrar múltiples dades alhora, separades per comes:

```python
print("El teu nom és", nom, "i tens", edat, "anys.")
```

**Tipus de dades en `print()`**:
- **String**: Text entre cometes (`"exemple"`).
- **Variables**: Qualsevol variable que continga un valor.
- **Operacions**: Operacions que resulten en un valor (per exemple, `5 + 3`).

---

## **Exercicis pràctics**

1. **Exercici de salutació personalitzada**:
   - Demana a l'usuari que introdueixi el seu nom i edat. Mostra un missatge de salutació personalitzat utilitzant les dades introduïdes.

2. **Exercici de càlcul d'edat en anys**:
   - Demana a l'usuari que introdueixi la seva edat en anys. Converteix la seva edat a mesos i mostra el resultat.

3. **Exercici de suma de dos números**:
   - Demana a l'usuari que introdueixi dos números, els suma i mostra el resultat de la suma.

---

### **Conclusió**

La funció **`input()`** permet capturar dades del teclat i **`print()`** és la manera de mostrar resultats a la pantalla. Aquestes funcions són fonamentals per a la interacció amb l'usuari en un programa.