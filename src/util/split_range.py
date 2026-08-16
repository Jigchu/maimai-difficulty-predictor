def split_range(range_str: str) -> list[str]:
    segments: list[str] = []
    segment_index: int = 0
    prev_char = ""

    for char in range_str:
        if prev_char.isalnum() != char.isalnum():
            segments.append("")
            segment_index += 1
        segments[segment_index] += char
        prev_char = char

    return [segment.strip() for segment in segments]
