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
    main_content_path = base_path / "main_content_data/projects.json"
    job_history_path = base_path / "main_content_data/job_history.json"
    og_tags_path = base_path / "og_tags.json"

    og_tags_data = load_data(og_tags_path)
    contexts = {
        "sidebar": load_data(sidebar_path),
        "summary": load_data(summary_path)["summary"],
        "resume_title": "Rohail Taimour",
        "og_tags": og_tags_data,
        "projects": load_data(main_content_path),
        "job_history": load_data(job_history_path),
    }

    return contexts
