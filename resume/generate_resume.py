import json
import os
from importlib import resources
from pathlib import Path

import typer
from jinja2 import Environment, FileSystemLoader, select_autoescape
from loguru import logger

from resume import PACKAGE_NAME

app = typer.Typer()


def configure_jinja():
    template_dir = resources.files(PACKAGE_NAME).joinpath("etc/templates")
    env = Environment(
        loader=FileSystemLoader(searchpath=str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    return env


def load_data(fpath):
    if not fpath.exists():
        raise FileNotFoundError(f"No file found at: {fpath}")
    with open(fpath, "r") as f:
        return json.load(f)


# Load all data
def load_contexts(data_dir):
    base_path = Path(data_dir)
    sidebar_path = base_path / "sidebar/sidebar.json"
    summary_path = base_path / "main_content_data/summary.json"
    main_content_path = base_path / "main_content_data/projects.json"
    job_history_path = base_path / "main_content_data/job_history.json"
    og_tags_path = base_path / "og_tags.json"

    og_tags_data = load_data(og_tags_path)
    contexts = {
        "sidebar": load_data(sidebar_path),
        "summary": load_data(summary_path)["summary"],
        "resume_title": "Rohail Taimour",
        "og_tags": og_tags_data,
        "projects": load_data(main_content_path),
        "job_history": load_data(job_history_path),
    }

    return contexts


@app.command()
def main(
    data_dir: str = typer.Option(
        ...,
        help="Path to the directory containing json files for sidebar and main_content data",
    ),
    output_dir: str = typer.Option(
        default=None, help="directory where we create the index.html"
    ),
):
    if output_dir is None:
        output_dir = os.getcwd()
    logger.info(f"Output directory: {output_dir}")
    contexts = load_contexts(data_dir)
    env = configure_jinja()
    template = env.get_template("base.jinja2")
    output = template.render(**contexts)
    path2out = Path(output_dir, "index.html")
    if path2out.exists():
        raise FileExistsError(
            f"index.html already exists at:{path2out}. Remove file and try again"
        )

    # Save the rendered HTML to a file
    with open(path2out, "w") as f:
        f.write(output)


if __name__ == "__main__":
    app()
