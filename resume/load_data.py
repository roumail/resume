import json


def load_data(fpath):
    with open(fpath, "r") as f:
        return json.load(f)


def load_sidebar_data():
    sidebar_data = load_data("data/sidebar/sidebar.json")
    return sidebar_data


def load_freelance_projects():
    projects = load_data("data/main_content_data/freelance_projects.json")
    return projects["freelance_projects"]


def load_ucb_projects():
    projects = load_data("data/main_content_data/ucb_projects.json")
    return projects["ucb_projects"]


def load_personal_projects():
    projects = load_data("data/main_content_data/personal_projects.json")
    return projects["personal_projects"]
