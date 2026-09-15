
# Creació d'un compte a GitHub, repositori i pujada d'un projecte

En aquesta secció, s'explicarà com crear un compte a GitHub, com crear un repositori i com pujar un projecte des del teu ordinador a GitHub. Tot i que no es valorarà directament aquesta tasca, és important que coneguis com utilitzar GitHub per gestionar els teus projectes i compartir-los amb altres.

## 1. Crear un compte a GitHub

Per crear un compte a GitHub, segueix aquests passos:

1. Visita la pàgina web de [GitHub](https://github.com).
2. Fes clic a "Sign up" (Registra't).
3. Omple la informació necessària (nom d'usuari, correu electrònic, contrasenya) i segueix les instruccions per completar la creació del compte.
4. Un cop registrat, tindràs accés al teu perfil a GitHub.

## 2. Crear un repositori

Un repositori és on es guardaran els arxius del teu projecte. Per crear un repositori a GitHub:

1. Inicia sessió al teu compte de GitHub.
2. A la pàgina principal del teu compte, fes clic al botó **"New"** (Nou) a la part superior esquerra per crear un repositori nou.
3. Omple el formulari amb la següent informació:
   - **Repository name** (Nom del repositori): Nom del teu projecte.
   - **Description** (Descripció): Una breu descripció del teu projecte.
   - **Public/Private**: Escull si el repositori serà públic o privat.
   - **Initialize this repository with a README**: Marca aquesta opció per crear un fitxer README per al teu repositori. Nosaltres **NO la marcarem**.
4. Fes clic a **"Create repository"** (Crear repositori).

## 3. Pujar el projecte al repositori

Per pujar un projecte des del teu ordinador al repositori que acabes de crear, segueix aquests passos:

1. **Instal·la Git**:
   - Si no tens Git instal·lat al teu ordinador, descarrega'l des de [aquí](https://git-scm.com/downloads) i segueix les instruccions d'instal·lació.+


2. Es possible fer el següent des de visual estudio:

   - Ctrl + Shift + P : Obriràs la barra d'accions superior
   - Busca l'opció "Git:Clone"
   - Quan t'ho demane, introdueix el teu usuari i contrasenya
   - Et preguntarà en quin punt del sistema vols crear el teu directori. Selecciona la carpeta que vulgues.

Una vegada seguits estos passos, tindràs el teu repository GitHub enllaçat en un directori local.


**ÚNICAMENT** si açò no funciona, segueix els següents passos


1. **Inicialitza el repositori localment**:
   - Obre el terminal o la línia de comandes (pots fer-ho desde VSCode).
   - Navega a la carpeta del teu projecte amb el comandament:
     ```bash
     cd /ruta/a/teu/projecte
     ```
   - Inicialitza el repositori Git:
     ```bash
     git init
     ```

2. **Afegir els arxius al repositori**:
   - Afegeix els arxius del teu projecte al repositori Git local:
     ```bash
     git add .
     ```

3. **Fer el primer commit**:
   - Fes un commit per registrar els canvis:
     ```bash
     git commit -m "Primer commit del projecte"
     ```

4. **Connectar el repositori local amb el repositori remot de GitHub**:
   - Copia la URL del teu repositori GitHub (per exemple, `https://github.com/usuari/nom-del-repositori.git`).
   - Afegeix el repositori remot amb el comandament:
     ```bash
     git remote add origin https://github.com/usuari/nom-del-repositori.git
     ```

4. **Pujar els arxius a GitHub**:
   - Pujar els arxius al repositori remot a GitHub:
     ```bash
     git push -u origin master
     ```

Amb això, el teu projecte haurà estat pujat a GitHub i estarà disponible a la URL del repositori que has creat.

---


## 4. Commit, Push i Pull a GitHub

### 4.1 Commit

El **commit** és l'operació que permet enregistrar canvis en el repositori local. Quan fas un commit, estàs guardant una instantània del teu projecte en el moment actual. Aquest canvi es realitza de forma local, és a dir, no es puja encara a GitHub, però deixa un registre d'història en el repositori local.

Per fer un commit, primer afegeix els arxius que vols guardar amb el següent comandament:

```bash
git add .
```

Després, fes el commit amb el missatge explicatiu que descriu els canvis realitzats:

```bash
git commit -m "Missatge del commit"
```

### 4.2 Push

El **push** permet enviar els canvis locals a GitHub per actualitzar el repositori remot. Un cop has fet el commit, per pujar els teus canvis a GitHub, utilitza el següent comandament:

```bash
git push
```

Aquesta acció actualitzarà el teu repositori remot amb els canvis realitzats en el repositori local.

### 4.3 Pull

El **pull** serveix per obtenir els últims canvis realitzats en el repositori remot i integrar-los en el teu repositori local. Aquesta acció és útil quan treballes en un projecte amb altres persones i vols assegurar-te de tenir la versió més actual del projecte.

Per actualitzar el teu repositori local amb els canvis remots, utilitza:

```bash
git pull
```

Aquesta comanda descarregarà i combinarà els canvis del repositori remot amb el teu repositori local, assegurant que estiguis al dia amb la versió més recent.

