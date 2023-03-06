# markdown-cv

A curriculum vitae maintained in markdown, html and CSS for styling. Rendered to HTML and PDF using `jekyll` and `wkhtmltopdf`.

## Customization

The `index.md` file is to be edited and `styles.css` for making a nice rendering CV.

## Distribution

To transform your markdown CV into a beautiful and shareable HTML page, you have two options:

### I. Use Github Pages to publish it online

1. Create a new branch called `gh-pages`, or update existing one if already exists.
2. Head to *yourusername*.github.io/markdown-cv to see your CV live.

Any change you want to make to your CV from then on would have to be done on the `gh-pages` branch and will be immediately rendered by Github Pages.

### II. Build it locally and print a PDF

1. To [install jekyll](https://jekyllrb.com/docs/installation/), run `gem install bundler jekyll` from the command line.
3. [Clone](https://help.github.com/en/articles/cloning-a-repository) your fork of markdown-cv to your local machine.
3. Type `jekyll serve` to render your CV at http://localhost:4000.
4. You can edit the `index.md` file and see the changes live in your browser.
5. To print a PDF, we use `wkhtmltopdf`

You can also use make all to generate a csv once you're happy with your changes

## Author

Rohail Taimour
