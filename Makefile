##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## Makefile
##

all:
	cp 104intersection.py 104intersection
	chmod +x 104intersection

clean:
	find -type f -name 104intersection -delete

fclean: clean

re: fclean
	all