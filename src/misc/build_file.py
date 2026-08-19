from pathlib import Path

def retrieve_build_files() -> list[Path]:
    src_root = Path(__file__).resolve().parent.parent
    build_files = list(src_root.glob("**/build.json"))

    return build_files
