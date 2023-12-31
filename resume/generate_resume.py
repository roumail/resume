import os
from pathlib import Path

import typer
from loguru import logger

from resume.load_data import load_contexts
from resume.render import configure_jinja

app = typer.Typer()


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
