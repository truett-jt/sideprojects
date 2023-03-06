import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas dataframe
df = pd.read_csv('/Users/truetttrotter/Desktop/Real World Python/apple_health_export/Apple Health Data - Sheet1.csv')

# Select only the variables of interest
sleep_data = df[['Exercise Minutes', 'Move Calories', 'Deep Sleep', 'Core Sleep', 'REM Sleep', 'Awake']]

# Calculate the correlation matrix
corr_matrix = sleep_data.corr()

# Plot a heatmap of the correlation matrix for Move Calories
sns.heatmap(corr_matrix.loc[['Exercise Minutes', 'Move Calories'], ['Deep Sleep', 'Core Sleep', 'REM Sleep', 'Awake']],
            annot=True, cmap='coolwarm')

# Show the plot
plt.title("Correlation of Move Calories/Exercise Minutes and Sleep Type")
plt.show()








