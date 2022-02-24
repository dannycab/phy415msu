BOOK_DIR := ./MMIPbook
BUILD_DIR := /_build/html

web:
	ghp-import -n -p -f ${BOOK_DIR}${BUILD_DIR}

rebuild:
	jupyter-book build ${BOOK_DIR}

fullrebuild:
	jupyter-book build --all ${BOOK_DIR}
