import os

from dotenv import load_dotenv

from resume.load_data import (
    load_freelance_projects,
    load_personal_projects,
    load_sidebar_data,
    load_summary,
    load_ucb_projects,
)
from resume.render import configure_jinja


def main():
    load_dotenv()
    BASE_DIR = os.getenv("BASE_DIR")
    if not BASE_DIR:
        raise ("BASE_DIR cannot be None")
    # Define the data for the sidebar and main content
    sidebar_data = load_sidebar_data()

    # Configure Jinja and ready the template
    env = configure_jinja()
    template = env.get_template("base.jinja2")

    # Set up context for projects
    freelance_projects_context = {
        "section_title": "Freelance projects (Oct 2022-present)",
        "projects": load_freelance_projects(),
    }
    ucb_projects_context = {
        "section_title": "Data science projects at IT AI team, UCB Pharmaceutical (2016‑Oct 2022)",
        "projects": load_ucb_projects(),
    }
    personal_projects_context = {
        "section_title": "Personal Projects",
        "projects": load_personal_projects(),
    }
    output = template.render(
        sidebar=sidebar_data,
        summary=load_summary(),
        freelance_projects_context=freelance_projects_context,
        ucb_projects_context=ucb_projects_context,
        personal_projects_context=personal_projects_context,
        resume_title="Rohail Taimour",
    )
    # Save the rendered HTML to a file
    with open(f"{BASE_DIR}/output.html", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
