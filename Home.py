import streamlit as st
from PIL import Image
import os
import re

def home_page():
    st.title("AI-Based Inventory Optimization System For Restaurants")
    st.markdown("---")

    #st.image("abc.jpg", use_column_width=True)
    # absolute path to this file
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    # absolute path to this file's root directory
    PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
    # absolute path of directory_of_interest
    dir_of_interest = os.path.join(PARENT_DIR, "resources") 
    
    IMAGE_DATA_PATH = os.path.join(dir_of_interest, "abc.jpg")
    
    photo_url = Image.open('resources/abc.jpg')
    st.image(photo_url, width=300)   
    
    st.write("Welcome to the AI-Based Inventory Optimization application! This application uses machine learning models to predict menu item demand based on various factors such as day of the week, holiday, and weather conditions.")
    
    st.write("To get started, use the sidebar to navigate to different sections of the application.")
    
    st.markdown("---")
    
    st.header("How it Works")
    st.write("1. **Predict Demand:** Enter the day of the week, holiday, and weather condition to predict the menu item that is likely to have high demand.")
    st.write("2. **Optimize Inventory:** Based on the predicted demand, optimize your inventory to ensure sufficient stock of popular menu items and reduce wastage.")
    st.write("3. **Increase Efficiency:** By accurately predicting demand and managing inventory effectively, streamline operations and increase overall efficiency of your restaurant.")
    
    st.markdown("---")
    
    st.header("About the Project")
    st.write("This project leverages machine learning techniques to provide predictive insights into menu item demand, helping restaurant owners optimize their inventory and improve operational efficiency.")
    st.write("Built using Streamlit, Pandas, and scikit-learn, this application demonstrates the power of AI in solving real-world business challenges.")
    
    st.markdown("---")
    
    st.header("Meet the Team")
    st.write("**Project Lead:** John Doe")
    st.write("**Data Scientist:** Jane Smith")
    st.write("**Software Engineer:** Michael Johnson")

# Main function to run the Streamlit app
def main():
    home_page()

if __name__ == "__main__":
    main()
