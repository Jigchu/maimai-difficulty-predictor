from typing import Callable


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

"""
Returns non inclusive range where [0] is upper and [1] is lower bound. -1 signifies 
unbounded/no bounds. inclusive_upper and inclusive_lower are called to normalise 
inclusive bounds to non-inclusive bounds
"""
def parse_range(
    range_segments: list[str],
    segment_to_int: Callable[[str], int],
    inclusive_upper: Callable[[int], int],
    inclusive_lower: Callable[[int], int]
) -> tuple[int, int]:
    lower = True
    inclusive = False
    equal = False
    lower_bound = upper_bound = -1

    for segment in range_segments:
        match segment:
            case "<":
                lower = False
            case "<=":
                lower = False
                inclusive = True
            case ">":
                lower = True
            case ">=":
                lower = True
                inclusive = True
            case "=":
                equal = True
            case "x":
                pass
            case _:
                if not segment.isnumeric():
                    segment = segment_to_int(segment)
                else:
                    segment = int(segment)

                if equal:
                    lower_bound = upper_bound = segment
                elif lower and not inclusive:
                    lower_bound = segment
                elif lower and inclusive:
                    lower_bound = inclusive_lower(segment)
                elif not lower and not inclusive:
                    upper_bound = segment
                elif not lower and inclusive:
                    upper_bound = inclusive_upper(segment)

    return (lower_bound, upper_bound)
