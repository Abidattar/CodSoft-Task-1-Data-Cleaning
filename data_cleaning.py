
# CODSOFT DATA ANALYST INTERNSHIP
# TASK 1: DATA CLEANING & PREPROCESSING

import pandas as pd
import numpy as np

# STEP 1: Create Dataset

data = {
    'Employee_ID': [101, 102, 103, 104, 101, 106, 107, 108, 109, 110],
    'Name': ['Rahul', ' Priya ', 'Ali', 'Sneha', 'Rahul',
             'Vikram', 'Meena', 'Arjun', 'Sara', 'John'],
    'Age': [25, np.nan, 23, 28, 25, np.nan, 30, 27, 24, 29],
    'Gender': ['M', 'F', 'Male', 'Female', 'M',
               'M', 'F', 'male', 'F', 'Male'],
    'City': ['Bangalore', 'Delhi', 'Mumbai', 'bangalore',
             'Bangalore', 'Delhi', 'Mumbai', 'PUNE',
             ' pune ', 'Delhi'],
    'Salary': [30000, 25000, 29000, np.nan, 30000,
               35000, np.nan, 32000, 28000, 40000],
    'Joining_Date': ['2024-01-10', '2024-02-15',
                     '2024-03-20', '2024-04-10',
                     '2024-01-10', '2024-05-12',
                     '2024-06-18', '2024-07-22',
                     'invalid', '2024-09-01']
}

df = pd.DataFrame(data)

print("\n--- ORIGINAL DATASET ---")
print(df)

# STEP 2: Inspect Dataset

print("\n--- DATASET INFORMATION ---")
df.info()

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include='all'))

# STEP 3: Identify Missing Values

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# STEP 4: Identify Duplicate Records

print("\n--- DUPLICATE RECORDS ---")
print(df[df.duplicated()])
print("Total duplicates:", df.duplicated().sum())

# STEP 5: Remove Extra Spaces

df['Name'] = df['Name'].str.strip()
df['City'] = df['City'].str.strip()

# STEP 6: Correct Inconsistent Entries

df['Gender'] = df['Gender'].replace({
    'M': 'Male',
    'F': 'Female',
    'male': 'Male',
    'female': 'Female'
})

df['City'] = df['City'].str.title()

print("\n--- CORRECTED ENTRIES ---")
print(df[['Name', 'Gender', 'City']])

# STEP 7: Handle Missing Values

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# STEP 8: Remove Duplicate Records

df = df.drop_duplicates()

# STEP 9: Correct Data Types

df['Age'] = df['Age'].astype(int)
df['Salary'] = df['Salary'].astype(int)

df['Joining_Date'] = pd.to_datetime(
    df['Joining_Date'],
    errors='coerce'
)

# STEP 10: Remove Invalid Dates

df = df.dropna(subset=['Joining_Date'])

# STEP 11: Display Final Cleaned Dataset

print("\n--- FINAL CLEANED DATASET ---")
print(df)

print("\n--- FINAL MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- FINAL DUPLICATES ---")
print(df.duplicated().sum())

print("\n--- FINAL DATA TYPES ---")
print(df.dtypes)

# STEP 12: Save Cleaned Dataset

df.to_csv('cleaned_dataset.csv', index=False)

print("\nProject completed successfully!")
print("Cleaned dataset saved as cleaned_dataset.csv")
