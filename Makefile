all: engine

engine: build/engine.cpp
	g++-11 $< -o $@