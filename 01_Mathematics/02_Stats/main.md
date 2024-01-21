# Statistics

Statistics is a branch of mathematics that involves collecting, analyzing, interpreting, presenting, and organizing data. It provides methods for making inferences and decisions in the presence of uncertainty.

It provides the theoretical foundation and practical tools for understanding, analyzing, and improving the performance of machine learning models in various stages of the data science workflow.

- describe() method in pandas DataFrame can be used to create a statistical summary of the dataset.

# Some important Terms

Mean: The average of a column
`df.col_name.mean()`

Median: Middle value. Not swayed by outliers
`df.col_name.medan()`

**If the distribution is gaussian, mean is a meaningful one value representation of the data, else median is.**

Mode: Most frequent value
`df.col_name.mode()`

Variance: spread of distribution
`df.col_name.var()`

Standard deviation: Square root of variance
`df.col_name.std()`

Cumulative Distibution function (CDF)
It is a function that gives the probability that a random variable takes on a value less than or equal to a specific value.

# Relationship Between Variables

## Correlation
It expresses the relationship between two variables as a number between -1 and 1.
`sns.heatmap(data.corr(),annot= True,linewidths=0.5,fmt = ".1f",ax=ax)`

- 1 means that the features are perfectly positively corelated.
- 0 means no relation
- -.3 means slight negative corelation

It's important to note that correlation does not imply causation. Even if two variables are correlated, it doesn't necessarily mean that one causes the other to change. Correlation only measures the strength and direction of a linear relationship between two variables.

## Covariance

measure of the tendency of two variables to vary together
Covariance is zero if they are orthogonal.

# Normal(Gaussian) Distribution and z-score¶

bell shaped distribution
