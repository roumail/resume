.PHONY: all serve pdf clean publish

all: clean serve pdf

serve:
	jekyll serve

pdf: 
	wkhtmltopdf localhost:4000 output.pdf

clean:
	rm -f output.pdf

publish:
	git push origin main:gh-pages