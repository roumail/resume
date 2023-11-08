import json


def load_data(fpath):
    with open(fpath, "r") as f:
        return json.load(f)


def load_sidebar_data():
    sidebar_data = load_data("data/sidebar/sidebar.json")
    return sidebar_data


def load_summary():
    projects = load_data("data/main_content_data/summary.json")
    return projects["summary"]


def load_freelance_projects():
    projects = load_data("data/main_content_data/freelance_projects.json")
    return projects["freelance_projects"]


def load_ucb_projects():
    projects = load_data("data/main_content_data/ucb_projects.json")
    return projects["ucb_projects"]


def load_personal_projects():
    projects = load_data("data/main_content_data/personal_projects.json")
    return projects["personal_projects"]


# Load all data
def load_contexts():
    contexts = {
        "sidebar": load_sidebar_data(),
        "summary": load_summary(),
        "freelance_projects_context": {
            "section_title": "Freelance projects (Oct 2022-present)",
            "projects": load_freelance_projects(),
        },
        "ucb_projects_context": {
            "section_title": "Data science projects at IT AI team, UCB Pharmaceutical (2016‑Oct 2022)",
            "projects": load_ucb_projects(),
        },
        "personal_projects_context": {
            "section_title": "Personal Projects",
            "projects": load_personal_projects(),
        },
        "resume_title": "Rohail Taimour",
    }
    return contexts
