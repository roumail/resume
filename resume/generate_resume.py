import importlib.resources as pkg_resources
import os

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

from resume.load_data import load_main_content_data, load_sidebar_data


def main():
    load_dotenv()
    BASE_DIR = os.getenv("BASE_DIR")
    if not BASE_DIR:
        raise ("BASE_DIR cannot be None")
    # Define the data for the sidebar and main content
    sidebar_data = load_sidebar_data()

    main_content_data = load_main_content_data()

    # Configure Jinja and ready the template
    # Read the template from the package's 'etc' directory
    with pkg_resources.path("resume.etc", "cv_template.jinja2") as template_path:
        # Configure Jinja and ready the template
        env = Environment(loader=FileSystemLoader(searchpath=str(template_path.parent)))
        template = env.get_template("cv_template.jinja2")

    # Render the template with data
    output = template.render(sidebar=sidebar_data, main_content=main_content_data)

    # Save the rendered HTML to a file
    with open(f"{BASE_DIR}/output.html", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
