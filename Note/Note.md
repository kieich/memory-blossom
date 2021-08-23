## Current Issues
- Some data are missing.
- Compute the mean and standard deviation for Python datetime
    - [computing the mean for python datetime](https://stackoverflow.com/questions/50358564/computing-the-mean-for-python-datetime)
    - [take standard deviation of datetime in python](https://stackoverflow.com/questions/15719928/take-standard-deviation-of-datetime-in-python)
- Since pandas represents timestamps in nanosecond resolution, the timespan that can be represented using a 64-bit integer is limited to approximately 584 years. (Source: [stack overflow](https://stackoverflow.com/questions/32888124/pandas-out-of-bounds-nanosecond-timestamp-after-offset-rollforward-plus-adding-a))
    ```
    In [54]: pd.Timestamp.min
    Out[54]: Timestamp('1677-09-22 00:12:43.145225')
    In [55]: pd.Timestamp.max
    Out[55]: Timestamp('2262-04-11 23:47:16.854775807')
    ```
- Would it be possible to switch x and y assignments on bee swarm plot and box and whisker plot?
    - [Seaborn boxplot: TypeError: unsupported operand type(s) for /: 'str' and 'int'](https://stackoverflow.com/questions/39937140/seaborn-boxplot-typeerror-unsupported-operand-types-for-str-and-int)
<br>


