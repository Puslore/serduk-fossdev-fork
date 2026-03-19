.PHONY: another-app
# not all targets are listened in PHONY

# Might be correct, but 'build' and 'app' are different
build: main.c
	gcc main.c -o app

# Correct no PHONY
app: main.c
	gcc main.c -o app

# Incorent listed in Phony
another-app: main.c
	gcc main.c -o another-app