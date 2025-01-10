import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle

# Load the trained model
model = tf.keras.models.load_model('model.keras')

# Load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Function to get the season based on the month
def get_season(month):
    if month in [3, 4, 5]:  # Summer: Mar, Apr, May
        return 'Summer'
    elif month in [6, 7, 8]:  # Monsoon: Jun, Jul, Aug
        return 'Monsoon'
    elif month in [9, 10, 11]:  # Autumn: Sep, Oct, Nov
        return 'Autumn'
    else:  # Winter: Dec, Jan, Feb
        return 'Winter'

# Function to get the time of day based on the hour
def get_time_of_day(hour):
    if 4 <= hour < 12:  
        return 'Morning'
    elif 12 <= hour < 16:  
        return 'Afternoon'
    elif 16 <= hour < 21:  
        return 'Evening'
    else:  
        return 'Night'

# Function to preprocess the data
def preprocess_data(data):
    # Drop the EnergyConsumption column if it exists
    if 'EnergyConsumption' in data.columns:
        data = data.drop('EnergyConsumption', axis=1)

    # Get Season and TimeOfDay from the month and hour
    data['Season'] = data['Month'].apply(get_season)
    data = data.drop('Month', axis=1)
    columns = ['Season'] + [col for col in data.columns if col != 'Season']
    data = data[columns]
    
    data['TimeOfDay'] = data['Hour'].apply(get_time_of_day)
    data = data.drop('Hour', axis=1)
    columns = ['Season', 'TimeOfDay'] + [col for col in data.columns if col not in ['Season', 'TimeOfDay']]
    data = data[columns]
    
    data.drop('DayOfWeek', axis=1, inplace=True)
    
    categorical_features = ['Season', 'TimeOfDay', 'Holiday', 'HVACUsage', 'LightingUsage']
    data = pd.get_dummies(data, columns=categorical_features, drop_first=True)
    
    # Ensure the new data has the same columns as the training data
    required_columns = [
        'Temperature', 'Humidity', 'SquareFootage', 'Occupancy', 'RenewableEnergy', 'Season_Monsoon', 
        'Season_Summer', 'Season_Winter', 'TimeOfDay_Evening', 'TimeOfDay_Morning', 'TimeOfDay_Night', 
        'Holiday_Yes', 'HVACUsage_On', 'LightingUsage_On'
    ]
    
    # Add missing columns with default value 0
    missing_cols = set(required_columns) - set(data.columns)
    for col in missing_cols:
        data[col] = 0
    
    # Ensure the columns are in the required order
    data = data[required_columns]
    
    # Scale the data
    scaled_data = scaler.transform(data)
    
    return scaled_data

# Streamlit interface
st.title("Energy Consumption Prediction")

# CSV file upload
st.subheader("Upload CSV for Prediction")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    input_data = pd.read_csv(uploaded_file)

    # Display the uploaded CSV data
    st.write("Uploaded Data:")
    st.write(input_data)

    # When the user clicks on the "Predict" button
    if st.button("Predict"):
        # Preprocess the input data
        processed_data = preprocess_data(input_data)
        
        # Predict energy consumption
        predictions = model.predict(processed_data)
        
        # Add prediction column to the DataFrame
        input_data['Prediction'] = predictions.flatten()

        # Display the updated DataFrame with predictions
        st.write("Data with Predictions:")

        # Color the 'Prediction' column based on value
        def color_predictions(val):
            if val < 65:  # Example threshold, adjust based on your data
                color = 'background-color: yellow'
            elif val < 88:
                color = 'background-color: green'
            else:
                color = 'background-color: red'
            return color
        
        # Apply the color function to the 'Prediction' column
        st.write(input_data.style.applymap(color_predictions, subset=['Prediction']))
