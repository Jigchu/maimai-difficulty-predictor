from typing import TypedDict

from pydantic import BaseModel

from util.build_file import retrieve_build_files
from util.bounded_range import BoundedRange, parse_range, split_range
from util.versions import version_to_int


class PreprocessorSettings(TypedDict):
    version_filter: BoundedRange
    level_filter: BoundedRange
    difficulty_filter: list[str]
    filter_utage: bool

class PreprocessorJSONFields(BaseModel):
    version_filter: str = ""
    level_filter: str = ""
    difficulty_filter: list[str] = []
    filter_utage: bool = True

def return_settings() -> PreprocessorSettings:
    build_files = retrieve_build_files()
    for file in build_files:
        json_string = file.read_text()
        settings = parse_settings(json_string)
        if (settings is not None):
            return settings

    return PreprocessorSettings(
        version_filter=BoundedRange(-1, -1),
        level_filter=BoundedRange(-1, -1),
        difficulty_filter=[],
        filter_utage=True,
    )


def parse_settings(json_string: str) -> PreprocessorSettings | None:
    settings: PreprocessorSettings = PreprocessorSettings(
        version_filter=BoundedRange(-1, -1),
        level_filter=BoundedRange(-1, -1),
        difficulty_filter=[],
        filter_utage=True,
    )

    settings_found: bool = False
    json_fields = PreprocessorJSONFields.model_validate_json(json_string)

    if json_fields.version_filter != "":
        settings_found = True
        version_range = split_range(json_fields.version_filter)

        settings["version_filter"] = parse_range(
            range_segments=version_range,
            segment_to_number=version_to_int,
            inclusive_upper=lambda x: x + 1,
            inclusive_lower=lambda x: x - 1,
        )

    if json_fields.level_filter != "":
        settings_found = True
        level_range = split_range(json_fields.level_filter)

        settings["level_filter"] = parse_range(
            range_segments=level_range,
            segment_to_number=lambda x: float(x),
            inclusive_upper=lambda x: x + 0.5,
            inclusive_lower=lambda x: x - 0.5,
        )

    if len(json_fields.difficulty_filter) != 0:
        settings_found = True
        settings["difficulty_filter"] = json_fields.difficulty_filter

    if json_fields.filter_utage != True:
        settings_found = True
        settings["filter_utage"] = json_fields.filter_utage

    return None if not settings_found else settings

if __file__:
    preprocessorSettings = return_settings()
