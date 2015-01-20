NAME =	level

all:	build

build:
	fig build

shell:	build
	fig run $(NAME) /bin/bash

up:	build
	fig up
