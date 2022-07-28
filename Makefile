BOOK_DIR := ./MMIPbook
BUILD_DIR := /_build/html
TEX_DIR := /_build/latex
PDF_FILE := Mathematical_Modeling_in_Physics.pdf

pdf:
	jupyter-book build ${BOOK_DIR} --builder pdflatex

web:
	ghp-import -n -p -f ${BOOK_DIR}${BUILD_DIR}

update:
	jupyter-book build ${BOOK_DIR}

rebuild:
	jupyter-book build --all ${BOOK_DIR}

viewhtml:
	open ${BOOK_DIR}${BUILD_DIR}/index.html

viewpdf:
	open ${BOOK_DIR}${TEX_DIR}/${PDF_FILE}

all: rebuild pdf rebuild web
