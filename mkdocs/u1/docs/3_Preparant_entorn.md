
# Preparar l'entorn per treballar amb Python

## Què necessitem instal·lar?

Abans de començar a escriure codi Python, és important tenir l'entorn de treball preparat. A continuació, et mostrem els passos per instal·lar tot el que necessites per començar a programar en Python a Linux.

---

## 1. Instal·lar Python

El primer pas és instal·lar Python al teu ordinador. Segueix aquests passos:

### Descarregar i Instal·lar Python a Linux

1. **Descarregar Python**:
   - Python ja està preinstal·lat en moltes distribucions de Linux. Però si necessites instal·lar-lo o actualitzar-lo, pots fer-ho mitjançant el gestor de paquets de la teva distribució.

2. **Instal·lació a Ubuntu/Debian**:
   - Obre una terminal i escriu les següents comandes per instal·lar Python:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

3. **Comprovar la instal·lació**:
   Un cop instal·lat, comprova que tot ha anat bé escrivint a la terminal:
   ```bash
   python3 --version
   ```
   Si tot està bé, veuràs la versió de Python instal·lada.

---

## 2. Instal·lar Gestor de Paquets (pip)

Python ve amb un gestor de paquets anomenat **pip**, que et permet instal·lar biblioteques i eines externes. Per verificar si **pip** està instal·lat, escriu:

```bash
pip3 --version
```

Si no tens **pip** instal·lat, pots fer-ho amb la següent comanda:

```bash
sudo apt install python3-pip
```

---

## 3. Instal·lar un entorn de desenvolupament (IDE)

Per escriure codi Python de manera còmoda, és important utilitzar un editor de codi o un entorn de desenvolupament integrat (IDE). Alguns dels més populars són:

- **Visual Studio Code (VS Code)**:
   Un editor lleuger però potent. Per instal·lar-lo, utilitza:
   ```bash
   sudo apt install code
   ```

- **PyCharm**:
   Un IDE dissenyat específicament per a Python. El pots descarregar des de [PyCharm](https://www.jetbrains.com/pycharm/).

- **Jupyter Notebook**:
   Ideal per a la ciència de dades i l'anàlisi interactiva de dades. Per instal·lar Jupyter, escriu:
   ```bash
   pip3 install notebook
   ```

---

## 4. Entorns Virtuals en Python

### Què és un entorn virtual?

Un **entorn virtual** és una eina que et permet crear un espai aïllat per al teu projecte de Python, de manera que les biblioteques i dependències d’un projecte no interfereixin amb les d’altres projectes. Això és especialment important quan treballes amb diferents projectes que poden necessitar versions de biblioteques diferents. 

### Per què és important utilitzar entorns virtuals?

1. **Aïllament de dependències**: Amb els entorns virtuals, cada projecte pot tenir les seves pròpies versions de biblioteques i paquets sense afectar altres projectes. Això evita conflictes entre diferents versions de biblioteques.

2. **Portabilitat**: Si utilitzes un entorn virtual, pots generar un fitxer anomenat `requirements.txt` que conté totes les dependències d’un projecte. Així, altres persones o tu mateix, podràs instal·lar totes les dependències necessàries simplement amb una comanda.

3. **Facilitat de manteniment**: Els entorns virtuals ajuden a mantenir el teu sistema net i organitzat, evitant que s'instal·lin biblioteques de manera global que podrien interferir amb altres projectes.

### Com crear un entorn virtual a Linux

1. **Crear un entorn virtual**:
   - Obre la terminal i navega fins al directori del teu projecte. Un cop dins, crea un entorn virtual amb la següent comanda:
   ```bash
   python3 -m venv nom_del_entorn
   ```
   Això crearà un directori anomenat `nom_del_entorn` amb tots els arxius necessaris per al teu entorn virtual.

2. **Activar l'entorn virtual**:
   - Per activar l'entorn virtual, escriu:
   ```bash
   source nom_del_entorn/bin/activate
   ```
   Un cop activat, veuràs que el nom de l'entorn virtual apareix a la terminal, indicant que estàs treballant dins d'aquest entorn.

3. **Instal·lar biblioteques dins de l'entorn virtual**:
   - Ara que l'entorn virtual està actiu, pots instal·lar qualsevol biblioteca necessària mitjançant **pip**. Per exemple:
   ```bash
   pip install numpy
   ```

4. **Desactivar l'entorn virtual**:
   - Quan acabis de treballar, pots desactivar l'entorn virtual escrivint:
   ```bash
   deactivate
   ```

---

## 5. Instal·lar biblioteques essencials

Un cop tinguis Python i pip instal·lats, pots instal·lar diverses biblioteques que són essencials per treballar amb Python. Algunes de les biblioteques més populars són:

- **NumPy**: Per treballar amb arrays i operacions matemàtiques.
  ```bash
  pip3 install numpy
  ```

- **Pandas**: Per treballar amb dades en forma de taules (DataFrames).
  ```bash
  pip3 install pandas
  ```

- **Matplotlib**: Per crear gràfics i visualitzacions de dades.
  ```bash
  pip3 install matplotlib
  ```

- **Scikit-learn**: Per treballar en aprenentatge automàtic.
  ```bash
  pip3 install scikit-learn
  ```

- **TensorFlow o PyTorch**: Per treballar en intel·ligència artificial.
  ```bash
  pip3 install tensorflow
  ```

---

## Conclusió

Ara que tens tot l'entorn preparat, ja estàs llest per començar a escriure i executar codi Python! Només cal obrir el teu editor preferit, activar l'entorn virtual per al teu projecte, i començar a programar. No oblides instal·lar les biblioteques necessàries per a cada projecte i mantenir els entorns virtuals aïllats per evitar conflictes entre dependències.

--- 