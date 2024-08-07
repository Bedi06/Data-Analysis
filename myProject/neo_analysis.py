import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Function to clean and standardise date strings
def clean_date(date_str):
    # regex to extract the date and time part before '±'
    match = re.match(r'(\d{4}-[A-Za-z]{3}-\d{2} \d{2}:\d{2})', date_str)
    if match:
        return match.group(1)
    else:
        return None

# Function to parse the cleaned date strings into datetime objects
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y-%b-%d %H:%M', errors='coerce')
    except ValueError:
        return pd.NaT

# # Loading data from the CSV file into a DataFrame
df = pd.read_csv('neo_data.csv')

# Cleaning and standardising the date strings in the 'Close-Approach (CA) Date' column
df['Close-Approach (CA) Date'] = df['Close-Approach (CA) Date'].apply(clean_date)

# Converting the cleaned date strings into datetime objects
df['Close-Approach (CA) Date'] = df['Close-Approach (CA) Date'].apply(parse_date)

# Printing the first few rows of the cleaned and parsed dates to verify
print(df[['Close-Approach (CA) Date']].head())

# Ensuring the 'CA DistanceMinimum (au)' column contains numeric values
df['CA DistanceMinimum (au)'] = pd.to_numeric(df['CA DistanceMinimum (au)'], errors='coerce')

# Calculating the percentage change in distance between close approaches
df['Percentage Change in Distance'] = df['CA DistanceMinimum (au)'].pct_change() * 100

# Printing DataFrame to check results
print(df)

# Collecting Data into lists for future uses
ca_dates = df['Close-Approach (CA) Date'].tolist()
ca_distances_min = df['CA DistanceMinimum (au)'].tolist()

# Outputting the total number of close approaches in the terminal
total_approaches = len(df)
print(f'Total Number of Close Approaches: {total_approaches}')

# Creating a summary DataFrame with key statistics and save it to a new CSV file
summary_df = pd.DataFrame({
    'Total Approaches': [total_approaches],
    'Average Minimum Distance (au)': [df['CA DistanceMinimum (au)'].mean()],
    'Highest Minimum Distance (au)': [df['CA DistanceMinimum (au)'].max()],
    'Lowest Minimum Distance (au)': [df['CA DistanceMinimum (au)'].min()]
})
summary_df.to_csv('neo_summary.csv', index=False)

# Sorting the DataFrame by date to prepare for analysis of percentage changes
df = df.sort_values('Close-Approach (CA) Date')

# Printing the dates and percentage changes in distance for review

print(df[['Close-Approach (CA) Date', 'Percentage Change in Distance']])

# Calculating and print the average, highest, and lowest distances
average_distance = df['CA DistanceMinimum (au)'].mean()
highest_distance = df['CA DistanceMinimum (au)'].max()
lowest_distance = df['CA DistanceMinimum (au)'].min()

print(f'Average Minimum Distance: {average_distance:.4f} au')
print(f'Highest Minimum Distance: {highest_distance:.4f} au')
print(f'Lowest Minimum Distance: {lowest_distance:.4f} au')


# Visualisation: Plotting the minimum distance of close approaches over time
# Static Line Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='Close-Approach (CA) Date', y='CA DistanceMinimum (au)', data=df)
plt.title('Minimum Distance of Close Approaches Over Time')
plt.xlabel('Date')
plt.ylabel('Minimum Distance (au)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram of Minimum Distances
plt.figure(figsize=(10, 6))
sns.histplot(df['CA DistanceMinimum (au)'], bins=20, kde=True)
plt.title('Histogram of Minimum Distances of Close Approaches')
plt.xlabel('Minimum Distance (au)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot of V relative vs. V infinity
if 'V relative(km/s)' in df.columns and 'V infinity(km/s)' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='V relative(km/s)', y='V infinity(km/s)', data=df)
    plt.title('Scatter Plot of Relative Speed vs. Infinity Speed')
    plt.xlabel('V relative (km/s)')
    plt.ylabel('V infinity (km/s)')
    plt.show()
else:
    print("Columns 'V relative(km/s)' and/or 'V infinity(km/s)' not found in the data.")
