# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Suppress warnings for clean output
import warnings
warnings.filterwarnings("ignore")

# Load dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Dataset is clean; no missing values to handle

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Group by species and calculate mean of numerical columns
grouped = df.groupby('species').mean()
print("\nMean values per species:")
print(grouped)

# Task 3: Data Visualization
# Set seaborn style
sns.set(style='whitegrid')

# 1. Line chart (simulating time with index for demo purposes)
plt.figure(figsize=(10,5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['sepal width (cm)'], label='Sepal Width')
plt.title('Sepal Length & Width Over Index (Simulated Time)')
plt.xlabel('Index')
plt.ylabel('Measurement (cm)')
plt.legend()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(7,5))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'], palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3. Histogram of petal length
plt.figure(figsize=(7,5))
sns.histplot(df['petal length (cm)'], bins=20, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: Sepal length vs petal length
plt.figure(figsize=(7,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Findings/Observations
print("\nObservations:")
print("- Setosa flowers tend to have smaller petal lengths.")
print("- There is a strong positive correlation between sepal length and petal length.")
print("- Versicolor and virginica species have overlapping sepal and petal lengths, but virginica has generally larger petals.")
