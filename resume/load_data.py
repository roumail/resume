import json
from pathlib import Path


def load_data(fpath):
    if not fpath.exists():
        raise FileNotFoundError(f"No file found at: {fpath}")
    with open(fpath, "r") as f:
        return json.load(f)


# Load all data
def load_contexts(data_dir):
    base_path = Path(data_dir)
    sidebar_path = base_path / "sidebar/sidebar.json"
    summary_path = base_path / "main_content_data/summary.json"
    main_content_path = base_path / "main_content_data/professional_projects.json"
    personal_projects_path = base_path / "main_content_data/personal_projects.json"

    main_content_data = load_data(main_content_path)["projects"]
    contexts = {
        "sidebar": load_data(sidebar_path),
        "summary": load_data(summary_path)["summary"],
        "personal_projects_context": {
            "section_title": "Personal Projects",
            "projects": load_data(personal_projects_path)["personal_projects"],
        },
        "resume_title": "Rohail Taimour",
    }

    # Dynamically load each project section
    for section in main_content_data:
        for key, value in section.items():
            contexts[f"{key}_context"] = {
                "section_title": value["section_title"],
                "projects": value["items"],
            }

    return contexts
