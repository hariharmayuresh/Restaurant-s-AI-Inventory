import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from PIL import Image
import os
import re

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "Demand prediction dataset (Up3).csv")

df = pd.read_csv(DATA_PATH)


# Load the dataset
#df = pd.read_csv("resources/Demand prediction dataset (Up3).csv")
df.rename(columns={'Holiday/Event': 'Holiday'}, inplace=True)
df = df.fillna('NO')
df = df.drop(['Date', 'Quantity Sold', 'Sales Amount (INR)'], axis=1)

# Preprocessing
X_categorical = df[['Day of the week', 'Holiday', 'Weather Condition']]
y = df['Menu Item']

# One-hot encode categorical variables
column_transformer = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), [0, 1, 2])
    ],
    remainder='passthrough'
)
X_encoded = column_transformer.fit_transform(X_categorical)

# Train the model
model = RandomForestClassifier()
model.fit(X_encoded, y)

# Function to predict menu item
def predict_menu(day, holiday, weather):
    input_data = column_transformer.transform([[day, holiday, weather]])
    prediction = model.predict(input_data)
    return prediction[0]

# Create Streamlit app
def main():
    st.title("Menu Item Demand Prediction") 

    # Day of the week dropdown
    day = st.selectbox("Day of the Week:", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Holiday dropdown
    holiday = st.selectbox("Holiday:", ["New Year's Day", 'NO', 'Weekend', 'Pongal', 'Makar Sankranti', 'Republic Day', "Valentine's Day", 'Holi', 'Gudi Padwa', "April Fools' Day", 'Ram Navami', 'Good Friday', 'Easter Sunday', 'Ambedkar Jayanti', 'Hanuman Jayanti', 'Buddha Purnima', 'May Day', "Mother's Day", 'Eid al-Fitr', "Father's Day", 'Bakri Id', 'Raksha Bandhan', 'Janmashtami', 'Independence Day','Ganesh Chaturthi', 'Onam', 'Hindi Diwas', 'Navratri'])

    # Weather condition dropdown
    weather = st.selectbox("Weather Condition:", ['Clear', 'Foggy', 'Rainy'])

    # Predict button
    if st.button("Predict"):
        prediction = predict_menu(day, holiday, weather)
        st.write("Predicted Menu Item:", prediction)

if __name__ == "__main__":
    main()