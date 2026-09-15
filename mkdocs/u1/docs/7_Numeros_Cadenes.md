
# Números i Textos

Els **números** i **textos** són tipus de dades fonamentals en qualsevol llenguatge de programació. A continuació, explorarem com treballar amb aquests tipus de dades en Python.

---

## 1. Números

En Python, els **números** es poden dividir en dues categories:

- **Enteros (int)**: Són nombres sense decimals. Per exemple, 5, -3, 100.
- **Flotants (float)**: Són números amb decimals. Per exemple, 3.14, -0.5, 2.0.

### Exercici 1.1 - Treballar amb números

Crea un programa que:

1. Assigni un número enter i un número flotant a dues variables.
2. Impri les operacions següents: suma, resta, multiplicació i divisió entre aquests dos números.

```python
# Assignar valors a les variables
enter = 10
flotant = 3.14

# Realitzar operacions
suma = enter + flotant
resta = enter - flotant
multiplicacio = enter * flotant
divisio = enter / flotant

# Mostrar els resultats
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicació: {multiplicacio}")
print(f"Divisió: {divisio}")
```

---

## 2. Textos

Els textos en Python es representen com a **cadenes de caràcters (strings)**. Les cadenes es poden crear amb cometes simples o dobles. Per exemple: `"Hola, món!"` o `'Python'`.

### Operacions amb cadenes

- **Concatenació**: Unir dues cadenes de text.
- **Indexació**: Accedir a un caràcter de la cadena per la seva posició.

### Exercici 1.2 - Treballar amb cadenes de text

Crea un programa que:

1. Assigni el teu nom i cognoms a dues variables de tipus cadena.
2. Concatenar aquestes dues cadenes per formar el teu nom complet.
3. Imprimir el nom complet.

```python
# Assignar valors a les cadenes
nom = "Joan"
cognom = "Pérez"

# Concatenar les cadenes
nom_complet = nom + " " + cognom

# Mostrar el resultat
print("El meu nom complet és:", nom_complet)
```

!!! note "Pregunta"

      - Quines altres operacions creus que es poden realitzar amb cadenes de text en Python? Investiga i les provem a classe.

---

## Conclusió

Ara ja saps treballar amb els tipus de dades **números** i **cadenes de text** en Python. Amb aquestes eines bàsiques podràs realitzar operacions matemàtiques i manipular dades textuals de manera efectiva.

---
