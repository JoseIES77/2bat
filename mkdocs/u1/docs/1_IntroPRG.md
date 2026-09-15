# Introducció a la Programació

## Què és la programació?

La **programació informàtica** és el procés de dissenyar i escriure instruccions que un ordinador pot entendre i executar.  
És, en essència, el llenguatge que permet als humans comunicar-se amb les màquines. Programar no és sols escriure codi, sinó també **resoldre problemes** d’una manera estructurada i eficient.

La programació és el pont entre les **idees humanes** i la **execució automàtica** per part d’un ordinador.

---

## Breu història de la programació

- **Anys 1800** – _Ada Lovelace_, considerada la primera programadora, descriu un algoritme per a la màquina analítica de Charles Babbage.
- **Anys 1940** – Naixen els primers ordinadors electrònics (ENIAC) i els primers llenguatges de baix nivell (codi màquina i assemblador).
- **Anys 1950-1960** – Apareixen llenguatges d’alt nivell com _Fortran_ i _COBOL_, més propers al llenguatge humà.
- **Anys 1970-1980** – Popularització de _C_, _Pascal_ i la programació estructurada.
- **Anys 1990-2000** – Expansió de la programació orientada a objectes (_Java_, _C++_) i del web (_JavaScript_, _PHP_).
- **Actualitat** – Llenguatges com _Python_, _Go_, _Rust_ o _Kotlin_ destaquen per la seua senzillesa, potència i aplicació en camps com la intel·ligència artificial, la ciència de dades i el desenvolupament mòbil.

---

## Tipus de llenguatges de programació

Els llenguatges es poden classificar de diferents formes. Una distinció habitual és per nivell:

- **Llenguatges de baix nivell**  
  Propers al llenguatge de la màquina. Exemples: Codi màquina, Assembleur.  
  Són molt ràpids i eficients, però difícils d’aprendre.

- **Llenguatges d’alt nivell**  
  Propers al llenguatge humà. Exemples: Python, Java, C#, JavaScript.  
  Són més fàcils d’utilitzar i permeten escriure programes complexos amb menys esforç.

Altra classificació habitual és en base a l'execució del codi. En esta classificació parlem de llenguatges  **interpretats** i **compilats** segons com s'executa el codi escrit pel programador. Aquesta distinció té una gran influència en el rendiment del programa, la facilitat d'ús i la portabilitat.

   ### Llenguatges compilats

   Els llenguatges **compilats** es converteixen en **codi màquina** que el sistema pot entendre directament. El procés de compilació es realitza una sola vegada, i el codi resultant es pot executar tantes vegades com es vulgui sense necessitat de compilar-lo novament. Aquest tipus de llenguatge tendeix a ser més ràpid a l'hora d'executar-se.

   Exemples: **C, C++, Rust**.

   **Procés de compilació:**
   1. Es compila el codi font en codi màquina.
   2. El programa resultant (fitxer executable) pot ser executat directament pel sistema operatiu.

   ### Llenguatges interpretats

   Els llenguatges **interpretats**, en canvi, es llegeixen i s'executen línia per línia per un **intèrpret**. El codi font no es converteix en codi màquina abans d'executar-se, sinó que l'intèrpret llegeix i executa directament cada línia mentre el programa s'està executant. Aquest procés sol ser més lent que la compilació, però facilita el desenvolupament perquè els errors es poden detectar més fàcilment durant l'execució.

   Exemples: **Python, JavaScript, Ruby**.

   **Procés d'interpretació:**
   3. L'intèrpret llegeix i executa el codi font línia per línia.
   4. No es genera un fitxer executable separat, i el codi es necessita cada vegada que s'executa el programa.

   ### Llenguatges híbrids

   Alguns llenguatges utilitzen una combinació de compilació i interpretació. Per exemple, **Java** compila el codi font a **bytecode**, que posteriorment és executat per una **màquina virtual** (JVM). Aquest enfocament busca un compromís entre el rendiment i la portabilitat.

   Exemples: **Java, C#**.

---

## Paradigmes de programació

Un **paradigma de programació** és un estil o model que defineix com es poden resoldre els problemes mitjançant un llenguatge. Els més importants són:

### 1. Programació imperativa

- Se centra en **com** fer les coses pas a pas.
- El programa és una seqüència d’instruccions que canvien l’estat del sistema.
- Exemples: **C, Pascal**.

**Exemple en pseudocodi – suma dels 10 primers nombres**:

```
INICI
    suma ← 0
    PER i ← 1 FINS 10 FER
        suma ← suma + i
    FI
    Mostrar suma
FI
```

### 2. Programació estructurada

- Variant de la imperativa que utilitza **estructures de control** clares (seqüència, selecció i iteració).
- Redueix l’ús de “goto” i millora la llegibilitat.
- Exemples: **C, Ada**.

### 3. Programació orientada a objectes (POO)

- El codi s’organitza en **classes** i **objectes**.
- Permet modelar entitats del món real amb **atributs** (propietats) i **mètodes** (comportaments).
- Utilitza conceptes com **encapsulació, herència i polimorfisme**.
- Exemples: **Java, C++, Python**.

**Exemple en pseudocodi – Classe Cotxe**:

```
CLASSE Cotxe
    ATRIBUTS: marca, model, velocitat
    MÈTODES:
        accelerar()
        frenar()
        mostrar_informacio()
FI CLASSE
```

### 4. Programació funcional

- Basa en la idea de les **funcions matemàtiques** pures, sense efectes laterals.
- El programa és una combinació de funcions.
- Exemples: **Haskell, Scala, Lisp**.

**Exemple en pseudocodi – suma dels 10 primers nombres**:

```
FUNCIO sumaPrimers(n)
    SI n = 0 ALESHORES
        RETORNAR 0
    ALTRAMENT
        RETORNAR n + sumaPrimers(n-1)
FI
```

### 5. Programació lògica

- Es basa en **fets i regles** que descriuen coneixement.
- El motor d’inferència cerca solucions a partir d’aquests fets.
- Exemple: **Prolog**.

**Exemple conceptual – família**

```
FET: pare(joan, maria)
FET: mare(anna, maria)
REGLA: progenitor(X,Y) SI pare(X,Y) O mare(X,Y)
```

---

## Què és un algoritme?

Un **algoritme** és un conjunt ordenat i finit de passos que descriuen com resoldre un problema o aconseguir un objectiu.  
És la base de tota programació.

### Propietats d’un bon algoritme

- **Clar**: fàcil d’entendre.
- **Finit**: té un principi i un final.
- **Eficaç**: resol el problema dins de recursos raonables.
- **Generalitzable**: pot aplicar-se a casos semblants.

### Exemple: Algoritme per fer un entrepà

1. Obrir el pa.
2. Afegir els ingredients desitjats.
3. Tancar el pa.
4. Servir.

### Exemple en pseudocodi – màxim de dos nombres

```
INICI
    Llegir A
    Llegir B
    SI A > B ALESHORES
        Mostrar "A és major"
    ALTRAMENT
        Mostrar "B és major"
FI
```

### Exemple en pseudocodi – ordenació d’una llista (Mètode Bombolla)

```
INICI
    PER i ← 1 FINS n-1 FER
        PER j ← 1 FINS n-i FER
            SI llista[j] > llista[j+1] ALESHORES
                intercanviar(llista[j], llista[j+1])
            FI
        FI
    FI
FI
```

Aquest algoritme ordena una llista d’elements de menor a major.

---


---

## La manera de pensar d’un programador

Aprendre a programar no és sols dominar un llenguatge o memoritzar instruccions: és **aprendre a pensar d’una forma estructurada i lògica**.  
Un bon programador desenvolupa una mentalitat especial que li permet analitzar problemes complexos i trobar-hi solucions eficients.

### Característiques d’aquesta forma de pensar

- **Descomposició**: dividir un problema gran en parts més xicotetes i manejables.  
- **Abstracció**: ignorar els detalls innecessaris i centrar-se en allò essencial.  
- **Pensament lògic**: utilitzar raonaments clars i precisos per prendre decisions.  
- **Creativitat**: trobar diferents camins per arribar a una solució.  
- **Precisió**: expressar instruccions d’una manera que l’ordinador puga entendre sense ambigüitats.

### Exemple quotidià

Si vols cuinar una recepta, primer mires els ingredients, després prepares els utensilis, executes els passos en ordre i finalment obtens el plat.  
Això és exactament el que fa un programador: **organitzar passos per arribar a un resultat**.

---


## El pseudocodi

El **pseudocodi** és un llenguatge intermig entre el llenguatge natural i el llenguatge de programació.  
Serveix per descriure algoritmes de manera clara i sense preocupar-se per la sintaxi estricta d’un llenguatge.

### Avantatges del pseudocodi

- Fàcil d’entendre per humans.
- Ajuda a planificar abans de programar.
- Independent del llenguatge de programació.

### Exemple en pseudocodi – càlcul de l’àrea d’un cercle

```
INICI
    Llegir radi
    area ← PI * radi * radi
    Mostrar area
FI
```

---

## Exemples d’aplicació de la programació

- **Aplicacions web** (YouTube, Spotify, bancs online).
- **Aplicacions mòbils** (WhatsApp, TikTok).
- **Videojocs** (Minecraft, Fortnite).
- **Intel·ligència artificial** (reconeixement facial, traducció automàtica).
- **Ciència i enginyeria** (simulacions físiques, càlcul de trajectòries espacials).

En definitiva, la programació és una **eina universal** que transforma idees en solucions pràctiques.




!!! note "Exercici individual"
    Tria un d’aquests problemes i escriu el seu **algoritme en pseudocodi**:

    1. Programa que calcule la mitjana de 3 notes i mostre si l’alumne/a està **aprovat** (≥5) o **suspés** (<5).  
    2. Algoritme que done la **taula de multiplicar** d’un número introduït per teclat.  
    3. 1. Algoritme que pregunte l’edat d’una persona i mostre si és **menor d’edat**, **adult** o **jubilat** (>65).  

!!! note "Repte extra"
    Dissenya en pseudocodi un **algoritme creatiu** per a un problema quotidià (per exemple: preparar-se per anar a l’institut, organitzar un viatge, o triar quina sèrie mirar a Netflix).

---

!!! note "Posada en comú i reflexió final"

    - Comparteix amb la classe el teu pseudocodi i explica les teues decisions.
    - Reflexiona: **què és més difícil**, inventar l’algoritme o traduir-lo a pseudocodi?  
    - Creus que podries transformar el teu pseudocodi en codi real en algun llenguatge (Python, Java…)? Per què sí o per què no?

**Recorda: La millor forma de aprendre a programar, es programant.**
---