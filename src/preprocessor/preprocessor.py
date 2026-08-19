from pathlib import Path
from typing import TypedDict

from misc.data import data_directory
from misc.settings import misc_settings
from preprocessor.settings import preprocessorSettings


class SimaiData(TypedDict):
    chart_name: str
    chart_difficulty: str
    chart_level: float
    chart_bpm: float
    chart: str


def main():
    files = filter_charts(data_directory / "preprocessed_charts")
    normalize_charts(files)
    split_charts()
    return


# Filters out the data and return a list of files that require normalization
def filter_charts(out_dir: Path) -> list[Path]:
    version_filter = preprocessorSettings["version_filter"]
    level_filter = preprocessorSettings["level_filter"]
    diffifculty_filter = preprocessorSettings["difficulty_filter"]
    filter_utage = preprocessorSettings["filter_utage"]
    chart_directory = misc_settings["chart_directory"]

    indexed_charts: list[Path] = []
    for walking_dir, _, file_names in chart_directory.walk():
        indexed_charts.extend(
            [
                walking_dir / chart
                for chart in filter(lambda x: x == "maidata.txt", file_names)
            ]
        )

    for chart_file in indexed_charts:
        metadata: SimaiData

    return []


def read_simai_data(chart_file: Path) -> SimaiData:
    raise Exception("Unable to read chart")


def normalize_charts(files: list[Path]):
    return


def split_charts():
    return


if __name__ == "__main__":
    main()
