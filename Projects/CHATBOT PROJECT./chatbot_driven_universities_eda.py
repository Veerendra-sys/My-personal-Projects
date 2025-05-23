# -*- coding: utf-8 -*-
"""Chatbot-Driven Universities EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FbNRQHuhJwwBlNgWUhFt50uQFvzqrz1w
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

try:
    # Try reading with the original encoding
    df = pd.read_csv("/content/AI_Chatbots_Students_Attitude_Dataset_EN.csv", encoding='latin-1')
except pd.errors.ParserError:
    # If it fails, try reading with a different delimiter and error handling
    df = pd.read_csv("/content/AI_Chatbots_Students_Attitude_Dataset_EN.csv", encoding='latin-1', delimiter=';', on_bad_lines='skip')  # or try delimiter='\t' for tab-separated files
df

df.head()

df.tail()

df.columns

df.isnull().sum()

df.isnull().sum().sum()

df.info()

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

grouped_df = df.groupby(['Q1', 'Q4']).agg('count')

plt.figure(figsize=(14, 6))
pivot_table = df.pivot_table(index='Q1', columns='Q4', values='Q5.1', aggfunc='count')
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt="g")
plt.title('Response Count Heatmap for Education Level and Frequency of Responses')
plt.xlabel('Frequency (Q4)')
plt.ylabel('Education Level (Q1)')
plt.show()

"""The heatmap visualizes the response count for different education levels and their frequency of responses. The data is structured in a tabular format where the rows represent education levels (Bachelor and Master), and the columns represent response frequencies (Never, Rarely, Sometimes, Very Often, Often). Each cell contains a number that indicates how many individuals from a particular education level selected a specific frequency.

To create this heatmap, the data is first organized into a Pandas DataFrame. Seaborn's heatmap() function is then used to generate the visualization, where annot=True ensures that the count values are displayed within each cell. The color scheme, set with cmap="coolwarm", helps in distinguishing high and low values, where dark red indicates a high count (e.g., 53 responses for "Sometimes" at the Bachelor's level), and dark blue represents a low count (e.g., 1 response for "Never" at the Master's level).

Data Distribution Analysis
"""

df['Q1'].value_counts().plot(kind='bar')

df.describe()

#Co-relation Analysis
plt.figure(figsize=(10,6))
# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Visualize agreement levels (Q5.1 - Q5.5) using a stacked bar chart
# Aggregate the data for visualization
response_counts = df[['Q1', 'Q4', 'Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5']].melt(
    id_vars=['Q1', 'Q4'], value_vars=['Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5'],
    var_name='Question', value_name='Response'
)

# Check if the melt operation was successful
print(response_counts.head())

# Plot stacked bar chart of response types
plt.figure(figsize=(14, 6))
response_order = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']
sns.countplot(data=response_counts, x='Question', hue='Response',
              order=['Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5'],
              hue_order=response_order, palette='coolwarm')

plt.title('Distribution of Agreement Levels Across Questions (Q5.1 to Q5.5)')
plt.xlabel('Questions (Q5.1 to Q5.5)')
plt.ylabel('Count of Responses')
plt.legend(title='Response Level')
plt.xticks(rotation=45)
plt.show()

# Visualize agreement levels (Q5.1 - Q5.5) using a stacked bar chart
# Aggregate the data for visualization
response_counts = df[['Q1', 'Q4', 'Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5']].melt(
    id_vars=['Q1', 'Q4'], value_vars=['Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5'],
    var_name='Question', value_name='Response'
)

# Check if the melt operation was successful
print(response_counts.head())

# Plot stacked bar chart of response types
plt.figure(figsize=(14, 6))
response_order = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']

# Use a different plot type for better visualization, like a grouped bar chart
ax = sns.countplot(data=response_counts, x='Question', hue='Response',
                   order=['Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5'],
                   hue_order=response_order, palette='coolwarm')


plt.title('Distribution of Agreement Levels Across Questions (Q5.1 to Q5.5)')
plt.xlabel('Questions (Q5.1 to Q5.5)')
plt.ylabel('Count of Responses')
plt.legend(title='Response Level', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.xticks(rotation=45, ha='right')  # Rotate and adjust x-axis labels

# Improve spacing between bars
ax.containers[0]
ax.bar_label(ax.containers[0])

plt.show()

print(df[['Q5.1', 'Q5.2', 'Q5.3', 'Q5.4', 'Q5.5']].describe())

# Analyze and visualize response trends for different demographic groups
# For example, looking at how often respondents from different educational levels select "Agree"
agree_responses = response_counts[response_counts['Response'] == 'Agree'].groupby(['Q1', 'Q4']).size().unstack()

agree_responses.plot(kind='bar', stacked=True, colormap='viridis', figsize=(14, 6))
plt.title('Agreement Responses by Education Level and Frequency')
plt.xlabel('Education Level and Frequency (Q4)')
plt.ylabel('Number of "Agree" Responses')
plt.xticks(rotation=0)
plt.legend(title='Frequency (Q4)', loc='upper right')
plt.show()

"""This stacked bar chart shows the distribution of "Agree" responses by education level. The Bachelor group has significantly more responses across different frequency levels ("Never," "Rarely," "Sometimes," "Often"), while the Master group has very few responses, only in the "Often" category. This suggests a possible imbalance in the number of respondents between the two education levels.









"""