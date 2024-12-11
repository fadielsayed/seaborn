import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

# Load the dataset
crash_df = sns.load_dataset('car_crashes')
print(crash_df.head())


# Create a distribution plot
sns.displot(crash_df['not_distracted'], kde=False, bins=25)

# Jointplot compares 2 distributions and plots a scatter plot by default
# As we can see as people tend to speed they also tend to drink & drive
sns.jointplot(x='speeding', y='alcohol', data=crash_df, kind='reg')

sns.kdeplot(crash_df['alcohol'])

# Pair Plot plots relationships across the entire data frames numerical values
sns.pairplot(crash_df)


# Show the plot
plt.show()

