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
Filters by difficulty. For this just indicate the wanted difficulties using a list of their names, for example `["Expert", "Advanced", "Re:Master"]`. Capitalization can be excluded/included. `Easy` charts will never be counted as they are unplayable after `FINALE`. `Utage` charts however can be included if wanted.

### `training_testing_split`
A 2 float list stating the percentage split of charts to training and testing respectively. For example, `[80, 20]` would allocate 80% of the indexed charts for training and 20% of the charts for testing. If the sum of the 2 numbers do not equal 100%, the rest of the charts will go to either training or testing sets depending on `testing_split_bias`

### `testing_split_bias`
A boolean indicating whether chart splitting will bias the testing set. To elaborate, it determines where excess/remainding charts are placed. For example, if `training_testing_split` is `[50, 50]`, and there are an odd number of charts that are indexed. The remaining one chart will go to the testing set if `testing_split_bias` is `true` and the training set if not
