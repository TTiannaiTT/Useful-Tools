# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np

# Set data (7 methods)
data = {
    'group': ['Identity', 'NDA', 'EventDrop', 'EvAug (ours)', 'EventMix', 'EventAugmentation', 'EventRPG', 'ShapeAug', 'ShapeAug++'],
    'ANN on \n DVS128 Gesture': [95.49, None, 96.18, 98.26, 91.80, 88.75, None,None, None],
    'ANN on \n N-Caltech101': [79.58, None, None, 90.16, 89.20, 87.61, None, None, None],
    'SNN on \n DVS128 Gesture': [93.75, 95.83, 94.44, 98.62, 96.75, 96.25, 96.53, 91.70, 92.40],
    'SNN on \n N-Caltech101': [79.10, 83.70, None, 91.13, 79.47, 75.25, 85.62, 68.70, 72.40],
}


# Convert to DataFrame
df = pd.DataFrame(data)

# Subtract 'Identity' values from all rows
identity_values = df.iloc[0, 1:]  # The first row (Identity values)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda col: col - identity_values[col.name])

# ---------- Step 1: Create the background

# Variable categories
categories = list(df.columns[1:])
N = len(categories)

# Set angles for each category
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the radar chart
fig, ax = plt.subplots(figsize=(11, 11), subplot_kw={'polar': True})

# Offset for the first axis and set direction
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axis per variable and add labels
plt.xticks(angles[:-1], categories, fontsize=15)

# Draw y-labels
ax.set_rlabel_position(0)
plt.yticks([-10, 0, 5, 15], ["-10", "0", "5", "15"], color="grey", size=7)
plt.ylim(-10, 15)

# ---------- Step 2: Plot data

# Function to handle missing values
def handle_missing(values):
    return [v if v is not None else np.nan for v in values]

# Academic color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']  # Extended to 9 colors
fill_colors = ['#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d']#lighter variants for fill

# Labels for each method
labels = df['group'].tolist()

for i, row in df.iterrows():
    values = row.drop('group').values.flatten().tolist()
    values = handle_missing(values)
    values += values[:1]  # Ensure it closes the loop

    # Special styling for EventAug (ours)
    if row['group'] == 'EvAug (ours)':
        ax.plot(angles, values, linewidth=2.5, linestyle='solid', label=labels[i], color='#d62728')  # Highlighted line
        ax.fill(angles, [v if not np.isnan(v) else 0 for v in values], color='#E6F5D0', alpha=0.6)  # Highlighted fill
    else:
        # Plot line
        ax.plot(angles, values, linewidth=1.5, linestyle='solid', label=labels[i], color=colors[i])
        # Fill area, exclude NaN
        ax.fill(angles, [v if not np.isnan(v) else 0 for v in values], color=fill_colors[i], alpha=0.3)

# Highlight missing data points
for angle, category in zip(angles[:-1], categories):
    for i, row in df.iterrows():
        value = row[category]
        if pd.isna(value):
            # Mark missing value with "X"
            ax.text(angle, 0, 'X', ha='center', va='center', fontsize=10, color=colors[i], alpha=0.7)

# Add legend
# plt.legend(loc='upper right', bbox_to_anchor=(1.1, 0.22), fontsize=15)
handles, labels = ax.get_legend_handles_labels()
order = [0, 1, 2, 8, 4, 5, 6, 7, 3]  # Define the desired order
plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper right', bbox_to_anchor=(1.1, 0.22), fontsize=15)

# Highlight missing data points
for angle, category in zip(angles[:-1], categories):
    for i, row in df.iterrows():
        value = row[category]
        if pd.isna(value):
            # Mark missing value with "X"
            ax.text(angle, 0, 'X', ha='center', va='center', fontsize=10, color=colors[i], alpha=0.7)

# Save the plot
plt.savefig('./fig/radar_chart_academic_colors.png', dpi=300)
plt.show()
