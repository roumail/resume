.PHONY: all html pdf clean publish

all: html pdf

html:
    pandoc -s -o resume.html --css styles.css resume.md

pdf:
    pandoc -s -o resume.pdf --css styles.css resume.md

clean:
    rm -f resume.html resume.pdf

publish:
    git push origin main:gh-pages
