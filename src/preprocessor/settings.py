import json
from pathlib import Path
from typing import TypeGuard, TypedDict, cast

from util.split_range import split_range

"""
version and level filter are non inclusive range
-1 in version and level filter indicates unbounded range
empty difficulty_filter indicates no filtered difficulties
"""


class PreprocessorSettings(TypedDict):
    version_filter: tuple[int, int]
    level_filter: tuple[int, int]
    difficulty_filter: list[str]
    filter_utage: bool


def is_valid_json(json_object: object) -> TypeGuard[dict[str, object]]:
    return isinstance(json_object, dict) and (
        (
            "version_filter" in json_object
            and isinstance(json_object["version_filter"], str)
        )
        or (
            "level_filter" in json_object
            and isinstance(json_object["level_filter"], str)
        )
        or (
            "difficulty_filter" in json_object
            and isinstance(json_object["difficulty_filter"], list)
        )
        or (
            "filter_utage" in json_object
            and isinstance(json_object["filter_utage"], bool)
        )
    )


def return_settings() -> PreprocessorSettings:
    src_root = Path("../")
    build_files = src_root.glob("**/build.json")

    for f in build_files:
        with open(f) as file:
            json_object: object = cast(object, json.load(file))
            settings = parse_settings(json_object)
            if settings is not None:
                return settings

    return PreprocessorSettings(
        version_filter=(-1, -1),
        level_filter=(-1, -1),
        difficulty_filter=[],
        filter_utage=True,
    )


def parse_settings(json_object: object) -> PreprocessorSettings | None:
    if not isinstance(json_object, dict):
        return None

    settings: PreprocessorSettings
    settings_found: bool = False

    if "version_filter" in json_object and isinstance(
        json_object["version_filter"], str
    ):
        settings_found = True
        version_range = split_range(json_object["version_filter"])

    if "level_filter" in json_object and isinstance(json_object["level_filter"], str):
        settings_found = True

    if "difficulty_filter" in json_object and isinstance(
        json_object["difficulty_filter"], list
    ):
        settings_found = True

    if "filter_utage" in json_object and isinstance(json_object["filter_utage"], bool):
        settings_found = True

    return None if not settings_found else settings
