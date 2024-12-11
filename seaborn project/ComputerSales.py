import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file
cs_df = pd.read_csv('computersales.csv')

# Check the first few rows to understand the dataset
print(cs_df.head())

# Distribution plot
# Replace 'Sex' with the correct column name
sns.displot(cs_df['Sex'], kde=False, bins=10)

# Joint plot
# Replace 'Product' and 'Age' with the correct column names
sns.jointplot(x='Product Type', y='Age', data=cs_df, kind='scatter')

# KDE plot
# Replace 'Profit' with the correct column name
sns.kdeplot(cs_df['Profit'])

# Pair plot
sns.pairplot(cs_df)

# Show the plots
plt.show()
