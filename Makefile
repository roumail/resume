.PHONY: all serve pdf clean publish

all: clean serve pdf

serve:
	jekyll serve

pdf: 
	wkhtmltopdf localhost:4000 output.pdf

clean:
	rm -f output.pdf

update-gh-pages:
	git checkout gh-pages
	git reset --hard main
	git push origin gh-pages

publish:
	git push origin main:gh-pages