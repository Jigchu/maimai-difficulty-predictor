# Miscellaneous Functions
Miscellaneous functions used by various components

## Settings
### `chart_directory`
`chart_directory` is a setting that denotes the absolute path to directory with the maimai chart data.

## Unused Settings
### `training_testing_split`
A 2 float list stating the percentage split of charts to training and testing respectively. For example, `[80, 20]` would allocate 80% of the indexed charts for training and 20% of the charts for testing. If the sum of the 2 numbers do not equal 100%, the rest of the charts will go to either training or testing sets depending on `testing_split_bias`

### `testing_split_bias`
A boolean indicating whether chart splitting will bias the testing set. To elaborate, it determines where excess/remainding charts are placed. For example, if `training_testing_split` is `[50, 50]`, and there are an odd number of charts that are indexed. The remaining one chart will go to the testing set if `testing_split_bias` is `true` and the training set if not
