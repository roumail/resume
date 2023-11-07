import json
from pathlib import Path


def load_sidebar_data():
    with open("data/sidebar/sidebar.json", "r") as f:
        sidebar_data = json.load(f)
        return sidebar_data


def load_section_data(section):
    with open(f"data/main_content_data/{section}/projects.json", "r") as f:
        return json.load(f)


def load_main_content_data():
    main_content_data = {"name": "Rohail Taimour", "sections": []}
    # Load summary from summary.json
    summary_path = Path("data/main_content_data/summary.json")
    with open(summary_path, "r") as f:
        summary_data = json.load(f)
        main_content_data["summary"] = summary_data.get("summary", "")

    # Load other sections
    main_content_dir = Path("data/main_content_data")
    sections = sorted(
        (x for x in main_content_dir.iterdir() if x.name.split("_")[0].isdigit()),
        key=lambda x: int(x.name.split("_")[0]),
    )

    for section in sections:
        section_name = section.name
        if section_name != "summary.json" and "personal" not in section_name:
            section_data = load_section_data(section_name)
            main_content_data["sections"].append(section_data)

    # append personal section at the end
    personal_path = Path("data/main_content_data/3_personal/projects.json")
    with open(personal_path, "r") as f:
        personal_data = json.load(f)
        main_content_data["personal_projects"] = personal_data.get("projects", [])

    return main_content_data
