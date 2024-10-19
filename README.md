# resume

A python package containing the jinja templates for maintaining my CV. The CV
content is rendered to `html` and served locally using `jekyll` and converted to
`pdf` using `wkhtmltopdf`.

## Installation

To install the package for local work, you can use `uv pip install -e ."[dev]"`.

## Releasing a new package version

Use `git tag -a "v{VERSION_NUMBER}" -m "{MESSAGE}"` to create a tag and push it.

This push will be detected by the github action `release.yaml` and an artifact
would be released for this version.

## Updating CV online and getting a local copy.

Refer to the [`cv-data`](https://github.com/roumail/cv-data) repository for
instructions on how to do this.

## Author

Rohail Taimour
