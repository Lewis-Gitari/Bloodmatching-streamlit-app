import pandas as pd
import streamlit as st
import os

def main():
    st.title("Blood Matching and Donor Management")

    os.makedirs('data', exist_ok=True)
    csv_file = os.path.join('data', 'donors.csv')
    
    if not os.path.isfile(csv_file):
        donors_df = pd.DataFrame(columns=[
            'id', 'name', 'blood_group', 'rh_factor', 
            'location', 'phone_number', 'pints', 'unit', 'last_donation_date'
        ])
        donors_df.to_csv(csv_file, index=False)
    else:
        donors_df = pd.read_csv(csv_file)

    # Title
    st.title('Blood Donor Management')

    # Form to add a new donor
    st.header('Add a New Donor')
    with st.form('add_donor_form'):
        id = st.text_input('Unique ID')
        name = st.text_input('Name')
        blood_group = st.selectbox('Blood Group', ['A', 'B', 'AB', 'O'])
        rh_factor = st.selectbox('Rh Factor', ['+', '-'])
        location = st.text_input('Location')
        phone_number = st.text_input('Phone Number')
        pints = st.number_input('Pints', min_value=0, step=1)
        unit = st.text_input('Unit')
        last_donation_date = st.date_input('Last Donation Date')

        submit_button = st.form_submit_button('Add Donor')

    if submit_button:
        # Create a new donor entry
        new_donor = pd.DataFrame([{
            'id': id,
            'name': name,
            'blood_group': blood_group,
            'rh_factor': rh_factor,
            'location': location,
            'phone_number': phone_number,
            'pints': pints,
            'unit': unit,
            'last_donation_date': last_donation_date
        }])
        
        # Append new donor to the DataFrame
        donors_df = pd.concat([donors_df, new_donor], ignore_index=True)
        
        # Save updated DataFrame to CSV
        donors_df.to_csv(csv_file, index=False)
        
        st.success('Donor added successfully!')

    # Display the donors list
    st.header('Current Donors')
    st.dataframe(donors_df)

if __name__ == "__main__":
    main()