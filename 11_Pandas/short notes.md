# PANDAS TUTORIAL

# Loading data
- pd.read_csv() # Reads a csv file as pandas Dataframe

# DataFrame basic overview
- df.describe()
- df.info()
- df.head(5) # Read first 5 rows with all columns

# Accessing data from a DataFrame
- df[['col1_name','col2_name']] # Reads both columns from the DataFrame df
- df.iloc[0:4,0] # Reads the first five rows and first column
- df.loc[0,'col1_name'] # Same as iloc, but with as textual column names
- df.iterrows() # Creates a generator, which can be used to easily iterate through the columns

# Sorting
- df.sort_values(['col1', 'col2'], ascending=[1,0]) # Sorts by col1 in ascending manner. If col1 for multiple rows are the same, it will sort those columns by col2 in descending manner.

# Manipulating columns
- df['new_col'] = df['col1'] + df['col2'] # Create a new column
    - df['new_col'] = df.iloc[:,0: 10].sum(axis=1) # Create a new col, which is the sum of all the 10 columns
- df.drop(columns = ['new_col'])

# Save 
- df.to_csv('name', index=False) # Save as csv

# Filtering rows
- df.loc[(df['name'] = 'Tom') & (df['age'] = '10')] # Select all rows with the conditions specified. Don't forget the stupid extra paranthesis
- df.loc[df['name] == 'cow', ['age', 'good']] = [100,True]# Set age to 100 and good to True if name is cow 
- df.groupby(['age']).mean() # Takes the mean for all columns for the rows with each discrete age value
![Alt text](image.png)

- 
# Using regular Expressions
- df.loc[df['col1'].str.contains('cow|goat',regex = True)] # Uses re module and selects all rows where cow or goat is present
- 

# Reading df as chunks
- for df in pd.read_csv('cow.txt', chunksize=100) # Read 100 rows at a time
      print(df)

``

