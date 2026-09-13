import re
from pathlib import Path

from pydantic import BaseModel

from misc.data import data_directory, difficulty_list
from misc.settings import misc_settings
from preprocessor.settings import preprocessorSettings


class SimaiData(BaseModel):
    chart_name: str = ""
    chart_difficulty: str = ""
    chart_level: float = 0
    chart: str = ""


class RawSimaiData(BaseModel):
    title: str = ""
    lv_2: str = ""
    inote_2: str = ""
    lv_3: str = ""
    inote_3: str = ""
    lv_4: str = ""
    inote_4: str = ""
    lv_5: str = ""
    inote_5: str = ""
    lv_6: str = ""
    inote_6: str = ""
    lv_7: str = ""
    inote_7: str = ""


def main():
    chart_files = filter_charts(data_directory / "preprocessed_charts")
    return


# Filters the charts and returns a set of paths sorted by difficulty
def filter_charts(out_dir: Path) -> dict[str, list[Path]]:
    version_filter = preprocessorSettings["version_filter"]

    chart_directory = misc_settings["chart_directory"]
    _, version_directories, _ = chart_directory.walk().__next__()
    indexed_charts: list[Path] = []

    version_directories = [
        chart_directory / dir
        for dir in version_directories
        if version_filter.contains(int(dir.split(".")[0]))
    ]

    for version_directory in version_directories:
        for current_directory, _, file_names in version_directory.walk():
            indexed_charts.extend(
                [
                    current_directory / file_name
                    for file_name in file_names
                    if file_name == "maidata.txt"
                ]
            )

    if not out_dir.exists():
        out_dir.mkdir()

    difficulty_filter = preprocessorSettings["difficulty_filter"]
    processed_files: dict[str, list[Path]] = {
        difficulty_list[difficulty - 2]: [] for difficulty in difficulty_filter
    }
    for chart_file in indexed_charts:
        raw_data = read_simai_data(chart_file)
        dict_simai_data = raw_data.model_dump()
        processed_charts = process_simai_data(dict_simai_data)
        for chart in processed_charts:
            file_name = (
                f"{chart.chart_name}_{chart.chart_difficulty}_{chart.chart_level}.txt"
            )
            chart_file = out_dir / normalize_file_name(file_name)
            if not chart_file.exists():
                chart_file.touch()
            _ = chart_file.write_text(chart.model_dump_json(), encoding="utf-8")
            processed_files[chart.chart_difficulty].append(chart_file)

    return processed_files


def read_simai_data(chart_file: Path) -> RawSimaiData:
    raw_chart = chart_file.read_text(encoding="utf-8")
    simai_data: dict[str, str] = {}

    field_name = ""
    field_value = ""
    for line in raw_chart.split(sep="\n"):
        if line == "":
            continue
        if line[0] == "&":
            if field_name != "":
                simai_data[field_name] = field_value
            sep_index = line.find("=")
            field_name = line[1:sep_index]
            field_value = line[sep_index + 1 :]
            continue
        field_value += line
    simai_data[field_name] = field_value

    validated_data = RawSimaiData.model_validate(simai_data)

    return validated_data


def process_simai_data(simai_data: dict[str, str]) -> list[SimaiData]:
    level_filter = preprocessorSettings["level_filter"]
    difficulty_filter = preprocessorSettings["difficulty_filter"]

    processed_charts: list[SimaiData] = []
    for difficulty in difficulty_filter:
        if simai_data[f"lv_{difficulty}"] == "":
            continue
        difficulty_level = normalize_chart_level(simai_data[f"lv_{difficulty}"])
        if not level_filter.contains(difficulty_level):
            continue
        chart = simai_data[f"inote_{difficulty}"]
        chart_data = SimaiData(
            chart_name=simai_data["title"],
            chart_difficulty=difficulty_list[difficulty - 2],
            chart_level=difficulty_level,
            chart=chart,
        )
        processed_charts.append(chart_data)

    return processed_charts


def normalize_chart_level(chart_level: str) -> float:
    chart_level = chart_level.replace("?", "")  # Remove Utage difficulty mark
    chart_level = chart_level.replace("+", ".6")  # X+ charts are X.6 and higher

    base_chart_level = int(chart_level.split(".")[0])
    plus_chart_level = base_chart_level + 0.6

    chart_constant = float(chart_level)

    return base_chart_level if chart_constant < plus_chart_level else plus_chart_level


# This just removes all illegal characters
def normalize_file_name(chart_name: str) -> str:
    return re.sub(r"[/\"<>:|?*]", "", chart_name)


if __name__ == "__main__":
    main()
