# Kinldy ignore these lines if you are using a local environment
from google.colab import drive
drive.mount('/content/drive')

# Importing dependencies
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# path to the dataset
file_path = '/content/drive/MyDrive/Volunteership/Diabetes_dataset/data.csv'
try:
  data = pd.read_csv(file_path)
except FileNotFoundError:
  print(f"Error: File not found at {file_path}")
data.head()

# List of irrelevant columns in the dataset
irr_columns = ['encounter_id',
                  'patient_nbr',
                  'race','payer_code']

# Dropping irrelevant columns
data = data.drop(columns=irr_columns)

# Function to calculate and visualize the null/missing values in the dataset
def calculate_null_percentage(data):
    data.replace('?', np.nan, inplace=True) #replacing ? with NaN for ease
    null_percentages = {col: data[col].isnull().sum() / data.shape[0] * 100 for col in data.columns}
    null_values_percentage = pd.DataFrame.from_dict(null_percentages, orient='index', columns=['Null Percentage'])

    # Visulaizing null percentages as a bar plot
    null_percentages_series = pd.Series(null_percentages).sort_values()
    plt.figure(figsize=(12, 8))
    null_percentages_series.plot(kind='barh', fontsize=8)
    plt.title('Percentage of Null Values per Column')
    plt.xlabel('Percentage of Null Values')
    plt.ylabel('Columns')
    plt.savefig('null_values_percentage.png')  # Save the plot

    return data, null_percentages, null_percentages_series

# Apply the function to the dataset
data, null_percentages, null_percentages_series = calculate_null_percentage(data)

# Drop columns with more than 50% missing values
data = data.drop(columns=null_percentages_series[null_percentages_series >= 50].index)

print("Columns retained:", data.columns)
