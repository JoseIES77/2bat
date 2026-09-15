Per a publicar:

mkdocs gh-deploy --force

REPO: https://joseies77.github.io/2bat/

pandoc 4_Bulleti2.md -o 4_Bulleti2.pdf --pdf-engine=lualatex



Flux de compilació


# 1. Compilar el projecte pare
cd /mkdocs
mkdocs build -d ../curs25-26_portal/docs/


# 2. Compilar cada subproyecto hacia el docs/ del portal
cd u1
mkdocs build -d ../../curs25-26_portal/docs/u1

cd ../u2
mkdocs build -d ../../curs25-26_portal/docs/u2


# 3. Compilar el portal
cd ../curs25-26_portal
mkdocs build