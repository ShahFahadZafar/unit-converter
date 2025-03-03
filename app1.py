
import streamlit as st
import pandas as pd

# Load existing data or create a new DataFrame
data_file = "data.csv"
try:
    df = pd.read_csv(data_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Email", "Age", "City"])

st.title("Data Entry App")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter Details")
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    age = st.number_input("Enter your age:", min_value=0, step=1)
    city = st.text_input("Enter your city:")
    
    if st.button("Submit"):
        if name and email and age and city:
            new_data = pd.DataFrame([[name, email, age, city]], columns=["Name", "Email", "Age", "City"])
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(data_file, index=False)
            st.success("Data saved successfully!")
        else:
            st.error("Please fill out all fields.")

with col2:
    st.subheader("Stored Data")
    st.dataframe(df)
