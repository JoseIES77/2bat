
# Operadors i Expressions

Els **operadors** i les **expressions** són fonamentals per realitzar càlculs i comparacions en Python. A continuació, veurem els diferents tipus d'operadors i com utilitzar-los en expressions.

---

## 1. Operadors aritmètics

Els operadors aritmètics permeten realitzar operacions matemàtiques bàsiques.

- **Suma (`+`)**
- **Resta (`-`)**
- **Multiplicació (`*`)**
- **Divisió (`/`)**
- **Mòdul (`%`)**
- **Potència (`**`)**
- **Divisió entera (`//`)**

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
mod = enter % flotant

# Mostrar els resultats
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicació: {multiplicacio}")
print(f"Divisió: {divisio}")
```

---

## 2. Operadors de comparació

Els operadors de comparació permeten comparar dos valors.

- **Igual a (`==`)**
- **Diferent de (`!=`)**
- **Més gran que (`>`)**
- **Menor que (`<`)**
- **Més gran o igual a (`>=`)**
- **Menor o igual a (`<=`)**

---

## 3. Operadors lògics

Els operadors lògics permeten realitzar operacions lògiques entre expressions booleans.

- **AND (`and`)**
- **OR (`or`)**
- **NOT (`not`)**

### Exercici 2.1 - Operadors lògics

Crea un programa que:

1. Assigni dos valors de booleans a les variables `x` i `y`.
2. Comproveu si ambdós són certs utilitzant l'operador lògic `and`.
3. Comproveu si almenys un d'ells és cert utilitzant `or`.

```python
x = True
y = False

if x and y:
    print("Ambdós són certs")
if x or y:
    print("Almenys un és cert")
```

---

## 4. Operadors d'assignació

Els operadors d'assignació permeten assignar valors a les variables amb operacions aritmètiques combinades.

- **Assignació simple (`=`)**
- **Assignació amb suma (`+=`)**
- **Assignació amb resta (`-=`)**
- **Assignació amb multiplicació (`*=`)**
- **Assignació amb divisió (`/=`)**

### Exercici 3.1 - Operadors d'assignació

Crea un programa que:

1. Assigni un valor inicial a la variable `counter`.
2. A continuació, incrementi el valor de `counter` utilitzant l'operador `+=`.
3. Resti 5 utilitzant `-=` i imprimeixi el valor final de `counter`.

```python
counter = 10
counter += 5  # Incrementar en 5
counter -= 5  # Restar 5
print(f"Valor final de counter: {counter}")
```

---

## 5. Operadors de membres

Els operadors de membres es fan servir per comprovar si un element es troba en una llista o cadena.

- **`in`**: Comprova si un element està dins d'una llista o cadena.
- **`not in`**: Comprova si un element no està dins d'una llista o cadena.

---

## Conclusió

Els **operadors** i les **expressions** són claus en qualsevol llenguatge de programació. Ara que coneixes els operadors bàsics en Python, podràs realitzar operacions matemàtiques, comparar valors i fer operacions lògiques en els teus programes.

---
