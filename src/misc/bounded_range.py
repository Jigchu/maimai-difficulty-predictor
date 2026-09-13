from math import inf
from typing import Callable, NamedTuple

"""
A non inclusive range of positive numbers
"""


class BoundedRange(NamedTuple):
    lower: float
    upper: float

    def contains(self, f: float):
        return f > self.lower and f < self.upper


def split_range(range_str: str) -> list[str]:
    segments: list[str] = [range_str[0]]
    segment_index: int = 0
    prev_char = range_str[0]

    range_str = range_str[1:]
    for char in range_str:
        if prev_char.isalnum() != char.isalnum():
            segments.append("")
            segment_index += 1
        segments[segment_index] += char
        prev_char = char

    return [segment.strip() for segment in segments]


def parse_range(
    range_segments: list[str],
    segment_to_number: Callable[[str], float],
    inclusive_upper: Callable[[float], float],
    inclusive_lower: Callable[[float], float],
) -> BoundedRange:
    lower = True
    inclusive = False
    equal = False
    lower_bound = -inf
    upper_bound = inf

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
                    segment = segment_to_number(segment)
                else:
                    segment = float(segment)

                if equal:
                    lower_bound = inclusive_lower(segment)
                    upper_bound = inclusive_upper(segment)
                elif lower and not inclusive:
                    lower_bound = segment
                elif lower and inclusive:
                    lower_bound = inclusive_lower(segment)
                elif not lower and not inclusive:
                    upper_bound = segment
                elif not lower and inclusive:
                    upper_bound = inclusive_upper(segment)

    return BoundedRange(lower=lower_bound, upper=upper_bound)
