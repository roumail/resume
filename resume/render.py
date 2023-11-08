from importlib import resources

from jinja2 import Environment, FileSystemLoader, select_autoescape

from resume.etc.constants import PACKAGE_NAME


def configure_jinja():
    template_dir = resources.files(PACKAGE_NAME).joinpath("etc/templates")
    env = Environment(
        loader=FileSystemLoader(searchpath=str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    return env
