all: test

test: build
	python src/main.py

build:
	mkdir -p output
