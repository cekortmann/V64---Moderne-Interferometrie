all: build/v64.pdf

build/v64.pdf: v64.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v64.tex
	lualatex  --output-directory=build v64.tex
	biber build/v64.bcf
	lualatex  --output-directory=build v64.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all