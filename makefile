all: test

test: build
	python src/main.py

build: clean
	mkdir -p output

clean:
	rm -rf input_for_mallet.mallet output/*
