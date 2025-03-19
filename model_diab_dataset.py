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
