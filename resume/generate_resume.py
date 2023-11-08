import os

from dotenv import load_dotenv

from resume.load_data import load_contexts
from resume.render import configure_jinja


def main():
    load_dotenv()
    BASE_DIR = os.getenv("BASE_DIR")
    if not BASE_DIR:
        raise ("BASE_DIR cannot be None")
    contexts = load_contexts()
    env = configure_jinja()
    template = env.get_template("base.jinja2")
    output = template.render(**contexts)
    # Save the rendered HTML to a file
    with open(f"{BASE_DIR}/output.html", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
