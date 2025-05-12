# --- Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

sns.set(style='whitegrid')

#Task 1: Load and Explore the Dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("✅ Dataset loaded successfully.")
except Exception as e:
    print("❌ Error loading dataset:", e)

print("\n🔍 First few rows of the dataset:")
print(df.head())


print("\n📊 Data Types:")
print(df.dtypes)

print("\n🧼 Missing Values:")
print(df.isnull().sum())

#Task 2: Basic Data Analysis

print("\n📈 Basic Statistics:")
print(df.describe())

print("\n📚 Mean values grouped by target (species index):")
print(df.groupby('target').mean())

df['species'] = df['target'].map(dict(zip(range(3), iris.target_names)))

print("\n📚 Mean values grouped by species name:")
print(df.groupby('species').mean())

# Task 3: Data Visualization


sdf['index'] = range(len(df))  

plt.figure(figsize=(10, 5))
plt.plot(df['index'], df['sepal length (cm)'], label='Sepal Length', color='blue')
plt.plot(df['index'], df['petal length (cm)'], label='Petal Length', color='orange')
plt.title('📈 Sepal and Petal Length Over Index')
plt.xlabel('Index (Simulated Time)')
plt.ylabel('Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='species', y='petal length (cm)', estimator='mean', palette='Set2')
plt.title('📊 Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
sns.histplot(df['sepal width (cm)'], kde=True, bins=20, color='skyblue')
plt.title('📉 Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
plt.title('🔵 Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()


print("\n✅ Key Observations:")
print("- Setosa has significantly smaller petal size compared to the other species.")
print("- Virginica has the largest petals overall.")
print("- Sepal and petal lengths show strong positive correlation.")
print("- Visualizations help distinguish species based on measurable features.")
