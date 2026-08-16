# Preprocessor
The preprocessor has 3 functions:
1. Filter unwanted charts
2. Normalize chart data
3. Set training and test sets

## Settings
### `version_filter`
`version_filter` has 2 modes of input, by name or by number of the version. For example to specify the PRISM version of maimai, you can either use `PRISM` or `24`, which is the version number for PRISM. To specify the version filter range you can use typical notation, `<` and other similar symbols. For a bounded range you can use the placeholder `x`. For example, a bounded range between PRISM and CIRCLE can be written as so `24 < x < 26`

### `level_filter`
As the name suggests, `level_filter` filters by level. In this case level is the numerical rating of the chart. You can use similar notation to `version_filter` for `level_filter`. For example, to indicate a difficulty level between `7+` to `13` inclusive use `7+ <= x <= 13`.

### `difficulty_filter`
Filters by difficulty. For this just indiciate the wanted difficulties using a list of their names, for example `["Expert", "Advanced", "Re:Master"]` capitalization and the colon in `Re:Master` can be excluded/included.

### `filter_utage`
A toggle to determine if `utage` difficulty charts should be filtered out. Due to the nature of `utage` charts essentially being joke charts, this is enabled by default.
