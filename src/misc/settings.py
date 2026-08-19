from pathlib import Path
from typing import TypedDict

from pydantic import BaseModel

from misc.build_file import retrieve_build_files


class MiscSettings(TypedDict):
    chart_directory: Path


class MiscJSONFields(BaseModel):
    chart_directory: str = ""


def return_settings() -> MiscSettings:
    build_files = retrieve_build_files()
    for file in build_files:
        settings = parse_settings(file.read_text())
        if settings is not None and settings["chart_directory"].exists():
            return settings

    project_root = Path(__file__).resolve().parent.parent.parent
    chart_directory = Path(project_root, Path("data/maimai_charts/"))
    chart_directory.mkdir(parents=True)

    return MiscSettings(chart_directory=chart_directory)


def parse_settings(json_str: str) -> None | MiscSettings:
    json_fields = MiscJSONFields.model_validate_json(json_str)
    if json_fields.chart_directory == "":
        return None
    return MiscSettings(chart_directory=Path(json_fields.chart_directory).resolve())


if __file__:
    misc_settings = return_settings()
