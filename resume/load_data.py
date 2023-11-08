import json
from pathlib import Path


def load_data(base_path, relative_path):
    full_path = Path(base_path, relative_path)
    if not full_path.exists():
        raise FileNotFoundError(f"The file {full_path} does not exist.")
    with open(full_path, "r") as f:
        return json.load(f)


# Load all data
def load_contexts(data_dir):
    base_path = Path(data_dir)
    sidebar_path = base_path / "sidebar/sidebar.json"
    summary_path = base_path / "main_content_data/summary.json"
    freelance_projects_path = base_path / "main_content_data/freelance_projects.json"
    ucb_projects_path = base_path / "main_content_data/ucb_projects.json"
    personal_projects_path = base_path / "main_content_data/personal_projects.json"

    contexts = {
        "sidebar": load_data(sidebar_path),
        "summary": load_data(summary_path)["summary"],
        "freelance_projects_context": {
            "section_title": "Freelance projects (Oct 2022-present)",
            "projects": load_data(freelance_projects_path)["freelance_projects"],
        },
        "ucb_projects_context": {
            "section_title": "Data science projects at IT AI team, UCB Pharmaceutical (2016‑Oct 2022)",
            "projects": load_data(ucb_projects_path)["ucb_projects"],
        },
        "personal_projects_context": {
            "section_title": "Personal Projects",
            "projects": load_data(personal_projects_path)["personal_projects"],
        },
        "resume_title": "Rohail Taimour",
    }
    return contexts
