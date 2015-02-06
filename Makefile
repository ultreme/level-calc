NAME =	level
FIG ?= fig.yml


all:	build

build:
	fig -f $(FIG) build

shell:	build
	fig -f $(FIG) run $(NAME) /bin/bash

up:	build
	fig -f $(FIG) up
