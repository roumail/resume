import json
import os


def load_sidebar_data():
    with open("data/sidebar/sidebar.json", "r") as f:
        return json.load(f)


def load_section_data(section):
    with open(f"data/main_content_data/{section}/projects.json", "r") as f:
        return json.load(f)


def load_main_content_data():
    main_content_data = {"name": "Rohail Taimour", "sections": []}
    # Load summary from summary.json if it exists
    summary_path = os.path.join("data/main_content_data", "summary.json")
    with open(summary_path, "r") as f:
        summary_data = json.load(f)
        main_content_data["summary"] = summary_data.get("summary", "")

    for section in os.listdir("data/main_content_data"):
        if section != "summary.json":
            section_data = load_section_data(section)
            main_content_data["sections"].append(section_data)

    return main_content_data
