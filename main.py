import pandas as pd

# Load the dataset with low_memory=False to handle large datasets without mixed type issues
file_path = 'D:\\Ein Stuff\\Real-Time_Traffic_Incident_Reports_20241011.csv' 
df = pd.read_csv(file_path, low_memory=False)

# Clean up column names (strip leading/trailing spaces) and standardize
df.columns = df.columns.str.strip()

# Drop rows with missing data in any column
df_cleaned = df.dropna()

# Convert "Published Date" and "Status Date" to datetime format
df_cleaned['Published Date'] = pd.to_datetime(df_cleaned['Published Date'], errors='coerce')
df_cleaned['Status Date'] = pd.to_datetime(df_cleaned['Status Date'], errors='coerce')

# Remove duplicates based on "Traffic Report ID" to ensure unique incident reports
df_cleaned = df_cleaned.loc[~df_cleaned.duplicated(subset='Traffic Report ID')]

# Standardize text formatting for "Issue Reported" and "Status"
df_cleaned['Issue Reported'] = df_cleaned['Issue Reported'].str.lower().str.strip()
df_cleaned['Status'] = df_cleaned['Status'].str.lower().str.strip()

# Remove rows with invalid lat/long (if any)
df_cleaned = df_cleaned[(df_cleaned['Latitude'].between(-90, 90)) & (df_cleaned['Longitude'].between(-180, 180))]

# Reset the index of the cleaned dataframe
df_cleaned.reset_index(drop=True, inplace=True)

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('cleaned_traffic_incident_data.csv', index=False)

# Print a preview of the cleaned data
print(df_cleaned.head())
