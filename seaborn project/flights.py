import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 


#Sets the figure size for subsequent plots to 8x6 inches 
#and adjusts the visualization context to paper with slightly larger fonts (scaled by 1.4).
plt.figure(figsize=(8,6))
sns.set_context('paper', font_scale=1.4)

# Loads the flights dataset (a built-in Seaborn dataset) and prints the first five rows to preview the data structure.
flights = sns.load_dataset("flights")
print(flights.head())

#Transforms the flights dataset into a pivot table where months are rows,
#years are columns, and the values represent the number of passengers.
flights = flights.pivot_table(index='month', columns='year', values='passengers')


#Creates a heatmap to visualize the pivot table, 
#using shades of blue to represent passenger numbers and separating cells with white lines.
sns.heatmap(flights, cmap='Blues', linecolor='white', linewidth=1)

#Repeats the setup for figure size and visualization context to prepare for the next set of plots.
plt.figure(figsize=(8,6))
sns.set_context('paper', font_scale=1.4)


#Loads the iris dataset (another built-in Seaborn dataset) for analyzing measurements of different iris flower species.
iris = sns.load_dataset("iris")


#Creates a clustered heatmap of the flights data, 
#grouping similar rows and columns, and standardizing the data to compare scales.
sns.clustermap(flights,cmap="Blues", standard_scale=1)


#Sets up the figure size and context for the following pair plot.
plt.figure(figsize=(8,6))
sns.set_context('paper', font_scale=1.4)

#Initializes a PairGrid object to compare specific pairs of variables in the iris dataset, with points colored by the species.
iris_g = sns.PairGrid(iris, hue="species",
                      x_vars=["sepal_length", "sepal_width"],
                      y_vars=["petal_length", "petal_width"])

#Plots scatter plots for each pair of variables specified in the PairGrid.
iris_g.map(plt.scatter)

# Add a legend last
iris_g.add_legend()

#Displays all the visualizations created in the code.
plt.show()
