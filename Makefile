BOOK_DIR := ./MMIPbook
BUILD_DIR := /_build/html

pdf:
	jupyter-book build ${BOOK_DIR} --builder pdflatex

web:
	ghp-import -n -p -f ${BOOK_DIR}${BUILD_DIR}

update:
	jupyter-book build ${BOOK_DIR}

rebuild:
	jupyter-book build --all ${BOOK_DIR}

all: rebuild pdf rebuild web
