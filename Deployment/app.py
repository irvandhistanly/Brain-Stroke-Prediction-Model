# Import Library
import streamlit as st

# Import custom pages
import eda_irvandhi
import prediction_irvandhi

# Set page title
st.title('BRAIN STROKE PREDICTION')

# Define icons for sidebar options
icons = {
    'EDA': '📊',
    'Model Prediction': '🔍'
}

# Function to display sidebar options with icons
def display_sidebar_option(option):
    return f"{icons[option]} {option}"

# Set sidebar options with icons
navigasi = st.sidebar.radio('Navigation', ('EDA', 'Model Prediction'), format_func=display_sidebar_option)

# Display selected page based on user's choice
if navigasi == 'EDA':
    eda_irvandhi.run()
else:
    prediction_irvandhi.run()
