import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#essential for numerical computations, data manipulation, and visualization.

# Load data on tips
tips_df = sns.load_dataset('tips')

#prints the first five rows to preview the data.
print(tips_df.head())

#Creates a rug plot, displaying individual data points of the tip column along the x-axis.
sns.rugplot(tips_df['tip'])

#Creates a bar plot showing the median total_bill for each sex category in the dataset.
sns.barplot(x='sex',y='total_bill',data=tips_df, estimator=np.median)

  
#Sets the figure size for the plot to 14x9 inches and applies the 'darkgrid' aesthetic style to all subsequent plots.
plt.figure(figsize=(14,9))
sns.set_style('darkgrid')

#Creates a box plot showing the distribution of total_bill across days of the week, with separate boxes for each sex
sns.boxplot(x='day',y='total_bill',data=tips_df, hue='sex')

#Automatically positions the legend in the best location based on the plotted data
plt.legend(loc=0)

#Sets the figure size for the next plot to 8x5 inches
plt.figure(figsize=(8,5))

#Generates a strip plot showing individual data points for total_bill per day,
#with points slightly jittered for better visibility and separated by sex.
sns.stripplot(x='day',y='total_bill',data=tips_df, jitter=True, 
              hue='sex', dodge=True)



#Creates a violin plot showing the distribution of total_bill per day (as a density plot) 
# and overlays a swarm plot in white to highlight individual data points.
sns.violinplot(x='day',y='total_bill',data=tips_df)
sns.swarmplot(x='day',y='total_bill',data=tips_df, color='white')


tips_df.head()

#Sets the visualization context to poster for larger plots and increases the font scale to 1.4 for better readability.
sns.set_context('poster', font_scale=1.4)

#Creates multiple linear regression plots (one for each day)
#to show the relationship between total_bill and tip, grouped by sex.
sns.lmplot(x='total_bill', y='tip', data=tips_df, col='day', hue='sex',
          height=8, aspect=0.6)

#Displays all the plots generated in the code.
plt.show()


