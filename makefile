all: test

test: build
	python src/main.py

build: clean
	mkdir -p output output_for_dotan

clean:
	rm -rf input_for_mallet.mallet output/* output_for_dotan/*
