# Documentació del Mòdul

## Requisits
- pandoc
- Eisvogel (plantilla pandoc)
- TeX Live / MikTeX amb `lualatex`

## Compilació
Per generar el PDF:

```bash
make
```

o bé directament:

```bash
pandoc plantillaDAM.md src/00_portada.md src/01_intro.md src/02_tema1.md src/99_bibliografia.md -o curs2425/Prog_DAM.pdf --template eisvogel --pdf-engine=lualatex
```

El fitxer PDF apareixerà a `curs2425/Prog_DAM.pdf`.
