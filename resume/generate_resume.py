import importlib.resources as pkg_resources

from jinja2 import Environment, FileSystemLoader
from load_data import load_main_content_data, load_sidebar_data

# Define the data for the sidebar and main content
sidebar_data = load_sidebar_data()
breakpoint()

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
with open(
    "/Users/rohailtaimour/home/2_AREAS/CV-APPLICATIONS/markdown-cv/output.html", "w"
) as f:
    f.write(output)
