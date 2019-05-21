# Examples

### Uprime Parameter Options

Default option `method = all` uses all available data to perform u'-chart calculations.
```python
from uprime import Uprime

up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            method = 'all')
            
up_df = up.frame()
```
\
This configuration performs u'-chart calculations using the previous rolling 30 periods for each subgroup.\
This method can be used for processes when the mean is expected to shift over time.\
(Note: This will omit the first 30 subgroups from the output DataFrame, because there is not enough history available to perform the calculations.)
```python
up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            method = 'rolling', periods = 30)
```
\
Use only the initial 30 periods to perform calculations for all subgroups.\
This method can be used in situations when the process is known to be in control for the first 30 periods and is not anticipated that the mean of the process will shift over time.
```python
up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            method = 'initial', periods = 30)
```
\
Change width of control limits with `sd_sensitivity` argument.\
The value is the number of standard deviations away from the mean to set the control limits.\
(Default is 3. Must be greater than 0. Float is acceptable)
```python
up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            sd_sensitivity = 3)
```
\
Ignore "out-of-control" subgroups in calculation of future control limits with `ignore_ooc = True`.\
Here, "out-of-control" is defined as outside of control limits.\
(Default is True. This argument is only used when `method = rolling`)
```python
up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            method = 'rolling', periods = 30, ignore_ooc = True)
```
\
When using this module as an alerting tool, `ooc_rule` contols whether to consider only the lower control limit ('low'), only the upper control limit ('high'), or the default: either ('either').\
`realert_interval` suppresses consecutive alerts that happen within the specified interval of periods.\
Example: If `realert_interval = 3` and there are 8 consecutive points that fall outside control limits (according to the selected `ooc_rule`), an alert will only be triggered in the 1st, 4th, and 7th periods.\
(Note: `realert_interval` only suppresses _consecutive_ alerts.  Any potential alert occuring immediately following an in-control subgroup will always result in an alert.)\
`alert_name` is passed to every row in the returned DataFrame and is useful if you will be appending the results to a data structure that contains u'-chart calculation results for multiple metrics.
```python
up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            ooc_rule = 'either', realert_intveral = 7, alert_name = 'your_alert_name')
```
\
Assume a 'binomial' or 'Poisson' distribution of the underlying data for the purpose of computing sigma_z (the ratio of total process variation to within-subgroup variation).\
When 'binomial' or 'Poisson' is specified, a 'sigma_z' column will be included in the DataFrame (`self.chart_df`) returned by the `chart()` method.\
When `method = rolling`, a different sigma_z value is calculated for each row and averaged to compute `self.sigma_z`.\
Otherwise, sigma_z is the same for all rows.\
(Default is None, meaning the computation will be skipped unless 'binomial' or 'Poisson' is specified)
```python
up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name',
            assumed_distribution = 'Poisson')
```

### Built in Charting Method

To visualize the u'-chart calculations, use the `chart()` method.\
`chart()` returns a `<class 'matplotlib.figure.Figure'>` for the u'-chart.\
The `frame()` method must be run prior to the `chart()` method because `chart()` uses `self.chart_df` which is created by `frame()`.\
The `show` argument determines whether or not to display the chart. The `<class 'matplotlib.figure.Figure'>` object will always be returned.
```python
from uprime import Uprime

up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name')
            
up.frame()

up.chart(show = True, plot_title = "u'-chart")
```
\
To edit the plot before displaying, `import matplotlib.pyplot as plt` then save the results of the `chart()` method to a variable.\
Next, make your edits before calling plt.show()
```python
from uprime import Uprime
import matplotlib.pyplot as plt

up = Uprime(df, 'sort_column_name', 'occurrences_column_name', 'subgroup_size_column_name')
            
up.frame()

up_chart = up.chart()

# EDIT PLOT HERE

plt.show()
```