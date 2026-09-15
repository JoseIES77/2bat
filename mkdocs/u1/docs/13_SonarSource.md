# Què és SonarSource i com enllaçar el teu repositori de GitHub

## Què és SonarSource?

**SonarSource** és una empresa que proporciona eines per a la qualitat del codi, amb una gran atenció a la seguretat i la netedat del codi font. La seva eina més coneguda és **SonarQube**, que permet analitzar codi font per detectar problemes de qualitat, com errors de seguretat, codi duplicat, bugs, i "code smells" (problemes de mantenibilitat).

SonarQube ajuda els desenvolupadors a millorar la qualitat del seu codi i a garantir que el seu projecte mantingui una bona estructura i seguretat a mesura que es desenvolupa.

El problema de SonarQube és que has de tindre'l allotjat en un servidor o al teu local, però SonarSource ens ofereix una sol·lució **SaaS** que solventa açò.

!!!note "Sabieu..."
      Que és **SaaS**?


## Com enllaçar el teu repositori de GitHub amb SonarQube

Per integrar SonarQube amb el teu repositori de GitHub, segueix aquests passos:

### Crea un compte a SonarSource

1. Visita la pàgina web de **[SonarSource](https://www.sonarsource.com/)**.
2. Registra't amb el teu correu electrònic i crea el teu compte.

### Crea un projecte a SonarQube

1. Un cop registrat i iniciat sessió, crea un nou projecte des del tauler de control de SonarQube.
2. Assigna un nom al teu projecte i selecciona el tipus de codi que vols analitzar (per exemple, Java, Python, JavaScript, etc.).
3. SonarQube generarà un token d’autenticació que necessitaràs per enllaçar el teu repositori de GitHub.

### Enllaçar SonarQube amb GitHub

1. A SonarQube, ves a la configuració del projecte i busca la secció **GitHub Integration**.
2. Segueix les instruccions per autoritzar SonarQube a accedir al teu compte de GitHub.
3. Una vegada autoritzat, SonarQube podrà analitzar el teu codi i generar informes de qualitat directament des de GitHub.

Amb aquesta configuració, SonarQube realitzarà un seguiment del teu projecte, mostrant resultats detallats sobre la qualitat del codi i ajudant-te a mantenir el projecte en bon estat.

## Avantatges d'utilitzar SonarQube

- **Millora de la qualitat del codi**: Identifica problemes de qualitat de codi abans que arriben a producció.
- **Seguretat**: Detecta vulnerabilitats i errors de seguretat en el codi.
- **Automatització**: Automatitza l'anàlisi de codi amb GitHub Actions i SonarQube.
- **Visualització clara**: Proporciona informes detallats i fàcils de comprendre per als desenvolupadors.

Per més informació sobre SonarQube i com integrar-lo amb GitHub, pots consultar la seva documentació oficial a: [SonarQube Documentation](https://docs.sonarqube.org/latest/).



## 6. Tipus de problemes reportats per SonarSource

**SonarSource**, a través de **SonarQube**, reporta diversos tipus de problemes al codi font. Aquests problemes poden ser de diversos tipus, i es classifiquen principalment en:

### 1. Bugs (Errors de codi)
   - **Definició**: Són defectes o problemes en el codi que poden fer que el sistema no funcioni com s'espera o generin comportaments inesperats. 
   - **Exemples**:
     - Variables no inicialitzades.
     - Condicions que no són mai vertaderes o mai falses.
     - Codi redundant o innecessari.
     - Accessos a recursos que poden generar excepcions (com intentar accedir a un objecte nul).

### 2. Vulnerabilitats de seguretat
   - **Definició**: Són vulnerabilitats que poden ser explotades per atacs, comprometen la seguretat de l'aplicació i poden provocar filtracions de dades o altres tipus de breches de seguretat.
   - **Exemples**:
     - Injeccions SQL.
     - No validació d'entrada, com a injeccions de comandaments o scripts maliciosos.
     - Ús incorrecte de les contrasenyes o gestió insegura de credencials.
     - Falta de xifrat de dades sensibles.

### 3. Code Smells (Olor de codi)
   - **Definició**: Els *code smells* són indicadors de que el codi pot tenir problemes de mantenibilitat, llegibilitat o eficàcia, però no necessàriament són errors crítics. Són signes de que el codi podria ser refactoritzat per millorar-ne la qualitat.
   - **Exemples**:
     - Funcions o mètodes que fan massa coses (funcions llargues).
     - Duplicació de codi.
     - Usar noms de variables o funcions poc descriptius.
     - Codi mort que mai s'executa.
     - Alta complexitat ciclomàtica (un codi excessivament complex que és difícil de seguir i mantenir).

### 4. Problemes de mantenibilitat
   - **Definició**: Són problemes que afecten la facilitat amb què el codi es pot mantenir, actualitzar i ampliar amb el temps.
   - **Exemples**:
     - Manca de comentaris o documentació en el codi.
     - Funcions o mètodes que realitzen tasques molt específiques o que són difícils d'entendre.
     - Massa dependències entre diferents parts del codi.
     - Classes o mètodes que són massa grans o complexes.

### 5. Problemes d'estil
   - **Definició**: Aquest tipus de problemes es relacionen amb la coherència en l'estil de codi seguit pel projecte, seguint les bones pràctiques establertes pel llenguatge de programació.
   - **Exemples**:
     - Manca d'espais en blanc entre operadors.
     - Nombratge inconsistente de variables o classes.
     - Ús inadequat d'estils i convencions de codi (com un nombre excessiu de línies en una funció, o l'ús de noms de funció poc clars).
     - Falta de consistència en l'indentació o en l'ús de l'espai entre els elements del codi.

### 6. Problemes de rendiment
   - **Definició**: Aquests problemes estan relacionats amb el rendiment de l'aplicació i la seva eficiència. Són qüestions que poden afectar la velocitat d'execució del codi o consumir recursos excessius.
   - **Exemples**:
     - Ús ineficient de recursos (per exemple, iteracions excessives o ús inadequat de memòria).
     - Codi que provoca la càrrega excessiva del processador.
     - Algoritmes subòptims.

### 7. Problemes d'accessibilitat
   - **Definició**: Són problemes que poden afectar la capacitat d'una persona amb discapacitat d'accedir al contingut o a les funcionalitats d'una aplicació web.
   - **Exemples**:
     - Falta de descripcions adequades per a imatges (atribut `alt`).
     - Errors en l'estructura de la pàgina que dificultin la navegació amb teclat o lectors de pantalla.
     - Falta de contrast adequat entre text i fons.
     - Elements interactius que no tenen una etiqueta o un focus adequat per als usuaris amb discapacitat visual.

### 8. Cobertura de proves insuficienta
   - **Definició**: Son problemes relacionats amb la cobertura de les proves (unitàries, d'integració, etc.), indicant que el codi no està suficientment cobert per proves automàtiques.
   - **Exemples**:
     - Manca de proves per a mètodes o funcions importants.
     - Alt percentatge de codi que no està cobert per proves unitàries.

### Resum dels tipus de problemes que SonarSource pot detectar:

- **Bugs**: Errors que poden afectar la funcionalitat.
- **Vulnerabilitats**: Problemes de seguretat que poden posar en perill l'aplicació.
- **Code Smells**: Problemes de mantenibilitat i llegibilitat del codi.
- **Mantenibilitat**: Codi difícil de mantenir o entendre.
- **Estilístics**: Problemes de coherència i estil del codi.
- **Rendiment**: Problemes que poden afectar l'eficiència de l'aplicació.
- **Accessibilitat**: Dificultats per a usuaris amb discapacitat.
- **Cobertura de proves**: Nivell de cobertura de les proves automàtiques.

Aquesta classificació i detecció de problemes ajuda els equips de desenvolupament a mantenir el codi net, segur i eficient, evitant futurs errors i facilitant la col·laboració i el manteniment dels projectes.

## Per a practicar

Descarrega el següent script en python polsant [aci](script_errades.py), afegeix-lo al teu repositori, i mira en [SonarSource](https://www.sonarsource.com/) el resultat de l'anàlisi. Series capaç d'interpretar els resultats?