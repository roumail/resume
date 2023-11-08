import os

from dotenv import load_dotenv

from resume.load_data import load_main_content_data, load_sidebar_data
from resume.render import configure_jinja


def main():
    load_dotenv()
    BASE_DIR = os.getenv("BASE_DIR")
    if not BASE_DIR:
        raise ("BASE_DIR cannot be None")
    # Define the data for the sidebar and main content
    sidebar_data = load_sidebar_data()

    main_content_data = load_main_content_data()

    # Configure Jinja and ready the template
    env = configure_jinja()
    template = env.get_template("base.jinja2")
    output = template.render(
        sidebar=sidebar_data,
        main_content=main_content_data,
        resume_title="Rohail Taimour",
    )
    # Save the rendered HTML to a file
    with open(f"{BASE_DIR}/output.html", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
