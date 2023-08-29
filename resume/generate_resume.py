import importlib.resources as pkg_resources

from jinja2 import Environment, FileSystemLoader

# Define the data for the sidebar and main content
sidebar_data = {
    "photo": "data/closeup-Photo.jpeg",
    "title": "Python/R Software Engineer | Contract Data Scientist | Statistician | AI/Machine Learning Specialist",
    # ... other fields
}

main_content_data = {
    "name": "Rohail Taimour",
    "summary": "Experienced data scientist with an expertise...",
    "sections": [
        {
            "title": "Freelance projects (Oct 2022-present)",
            "entries": [
                {
                    "project_title": "Automated SQL Script Generation for Cross-Platform Data Migration",
                    # ... other fields
                },
                # ... other entries
            ],
        },
        # ... other sections
    ],
}

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
