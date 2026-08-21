from pathlib import Path
from pydantic import BaseModel
import re

from misc.settings import misc_settings

data_directory: Path = Path()
difficulty_list: list[str] = ["basic", "advanced", "expert", "master", "re:master", "utage"]
_version_list: list[str] = []


class VersionListBuildFields(BaseModel):
    chart_directory: str


def get_data_directory() -> Path:
    project_root = Path(__file__).resolve().parent.parent.parent
    data_dir = project_root / "data/"
    data_dir.mkdir()

    return data_directory


def update_version_list():
    version_list_file = data_directory / "version_list.txt"
    version_list_file.touch()

    chart_directory = misc_settings["chart_directory"]

    versions = chart_directory.walk().__next__()[1]
    regex = re.compile("[^a-zA-Z]")
    versions = [regex.sub("", version) for version in versions]

    _ = version_list_file.write_text("\n".join(versions).lower())

    return


def load_version_list() -> list[str]:
    version_list_file = data_directory / "version_list.txt"
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
    data_directory = get_data_directory()
    _version_list = load_version_list()
