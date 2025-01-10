# Energy-consumption-prediction-using-keras

Project Description
This project focuses on predicting energy consumption using a neural network model built with the Keras Sequential API. The primary goal is to develop a model that accurately predicts energy usage based on various factors such as time, environmental conditions, and building-specific attributes. After training the model, it is deployed in a Streamlit app, allowing users to upload new data in CSV format for prediction. This application simplifies the prediction process, providing insights into energy usage for better energy management and optimization.

Dataset Description
The dataset consists of 5000 records and 12 columns. Below are the details of the dataset:
Month: Represents the month of the year (1–12). Useful for categorizing month data into seasons.
Hour: Hourly readings of the day (0–23), useful for categorizing time data into morning, afternoon, evening, and night.
DayOfWeek: Categorical variable indicating the day of the week (e.g., Monday, Tuesday).
Holiday: Boolean categorical variable indicating whether the day is a holiday.
Temperature: Numerical variable representing the temperature in degrees Celsius.
Humidity: Numerical variable showing the humidity level as a percentage.
SquareFootage: Numerical variable measuring the area of the building or space.
Occupancy: Numerical variable representing the number of people in the area.
HVACUsage: Categorical variable indicating the usage of Heating, Ventilation, and Air Conditioning systems.
LightingUsage: Categorical variable indicating the usage of lighting systems.
RenewableEnergy: Numerical variable representing the percentage contribution of renewable energy sources.
EnergyConsumption: Numerical target variable representing the total energy consumed.

Deployment Details
The trained model was saved for future use and deployed as part of a Streamlit web application. The app accepts new input data in CSV format, processes it, and provides predictions for energy consumption. This interactive tool enables users to make real-time predictions, enhancing its practical utility for energy management in dynamic scenarios.
