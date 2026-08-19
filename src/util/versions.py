from pathlib import Path
from pydantic import BaseModel
import re

from util.build_file import retrieve_build_files

_version_list: list[str] = []

class VersionListBuildFields(BaseModel):
    chart_directory: str

def update_version_list():
    project_root = Path(__file__).resolve().parent.parent.parent
    data_directory = Path(project_root, Path("data/"))
    data_directory.mkdir()

    version_list = Path(data_directory, Path("version_list.txt"))
    version_list.touch()

    chart_directory = Path(data_directory, Path("maimai_charts/"))
    build_files = retrieve_build_files()
    for file in build_files:
        json_fields = VersionListBuildFields.model_validate_json(file.read_text())
        chart_directory = Path(data_directory, Path(json_fields.chart_directory))

    versions = chart_directory.walk().__next__()[1]
    regex = re.compile("[^a-zA-Z]")
    versions = [regex.sub("", version) for version in versions]

    with open(version_list, mode="w") as version_file:
        _ = version_file.write("\n".join(versions).lower())

    return

def load_version_list() -> list[str]:
    project_root = Path(__file__).resolve().parent.parent.parent
    version_list_file = Path(project_root, Path("build/"), Path("version_list.txt"))
    if not version_list_file.exists():
        update_version_list()

    with open(version_list_file) as f:
        version_list = f.read().split("\n")

    return version_list

# Returns -1 if version name cannot be found
def version_to_int(version_name: str) -> int:
    if len(_version_list) == 0:
        raise Exception("_version_list is empty")

    return _version_list.index(version_name.lower())

if __name__:
    _version_list = load_version_list()
