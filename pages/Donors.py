import os
import pandas as pd
import streamlit as st

def main():
    st.title("Blood Matching and Donor Finding")

    # Path to the csv
    csv_file = 'data/donors.csv'

    # Load the dataset
    if os.path.isfile(csv_file):
        donors_df = pd.read_csv(csv_file)
    else:
        st.error('Donors data not found! Please add donors first.')
        st.stop()

    # Blood group compatibility rules
    compatible_blood_groups = {
        'A': ['A', 'AB'],
        'B': ['B', 'AB'],
        'AB': ['AB'],
        'O': ['A', 'B', 'AB', 'O']
    }

    def is_compatible(donor, recipient):
        if recipient['blood_group'] in compatible_blood_groups[donor['blood_group']]:
            # Check Rh factor compatibility
            if recipient['rh_factor'] == '+' or (recipient['rh_factor'] == '-' and donor['rh_factor'] == '-'):
                return True
        return False

    def find_compatible_donors(recipient):
        compatible_donors = []
        for _, donor in donors_df.iterrows():
            if is_compatible(donor, recipient):
                compatible_donors.append({
                    'id': donor['id'],
                    'name': donor['name'],
                    'blood_group': donor['blood_group'],
                    'rh_factor': donor['rh_factor'],
                    'phone_number': donor['phone_number'],
                    'location': donor['location'],
                    'unit': donor['unit'],
                    'last_donation_date': donor['last_donation_date']
                })
        return compatible_donors

    st.header('Find Compatible Donors')

    # User input for recipient's blood group and Rh factor
    blood_group = st.selectbox('Select your blood group', ['A', 'B', 'AB', 'O'])
    rh_factor = st.selectbox('Select your Rh factor', ['+', '-'])

    if st.button('Find Compatible Donors'):
        recipient = {
            'blood_group': blood_group,
            'rh_factor': rh_factor
        }

        matches = find_compatible_donors(recipient)

        if matches:
            st.write('Compatible donors found:')
            st.write(matches)
        else:
            st.write('No compatible donors found.')

if __name__ == "__main__":
    main()