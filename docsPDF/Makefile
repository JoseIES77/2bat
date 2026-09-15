.PHONY: all clean

all: curs2425/Prog_DAM.pdf

curs2425/Prog_DAM.pdf: plantillaSMX.md $(wildcard src/*.md)
	mkdir -p curs2425
	pandoc plantillaSMX.md \
	  -o curs2425/doc_smx.pdf \
	  --template eisvogel \
	  --pdf-engine=lualatex

clean:
	rm -f curs2425/*.pdf
