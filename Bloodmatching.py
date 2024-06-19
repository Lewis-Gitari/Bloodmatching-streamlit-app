import pandas as pd
import streamlit as st
import os

os.makedirs('data', exist_ok=True)
csv_file = 'donors.csv'
if not os.path.isfile(csv_file):
    donors_df = pd.DataFrame(columns=[
        'id', 'name', 'blood_group', 'rh_factor', 
         'phone_number', 'Pints', 'Unit','Deployment','last_donation_date'
    ])
    donors_df.to_csv(csv_file, index=False)
else:
    donors_df = pd.read_csv(csv_file)

# Title

st.markdown(
    """
    <style>
    .main {
        background-image: url("blood.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Blood Group Matching and Donor Management')

# Form to add a new donor
st.header('Add a New Donor')
with st.form('add_donor_form'):
    id = st.text_input('Unique ID')
    name = st.text_input('Name')
    blood_group = st.selectbox('Blood Group', ['A', 'B', 'AB', 'O'])
    rh_factor = st.selectbox('Rh Factor', ['+', '-'])
    location = st.text_input('Location')
    phone_number = st.text_input('Phone Number')
    pints = st.number_input('Unit', min_value=0, step=1)
    unit = st.text_input('unit')
    last_donation_date = st.date_input('Last Donation Date')

    submit_button = st.form_submit_button('Add Donor')

if submit_button:
    # Create a new donor entry
    new_donor = pd.DataFrame ([{
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
    #donors_df = donors_df.append(new_donor, ignore_index=True)
    donors_df = pd.concat([donors_df, new_donor], ignore_index=True)
    
    
    # Save updated DataFrame to CSV
    donors_df.to_csv(csv_file, index=False)
    
    st.success('Donor added successfully!')

# Display the donors list
st.header('Current Donors')
st.dataframe(donors_df)



# Blood group compatibility rules
compatible_blood_groups = {
    'A': ['A', 'AB'],
    'B': ['B', 'AB'],
    'AB': ['AB'],
    'O': ['A', 'B', 'AB', 'O']
}
def is_compatible (donor, recipient):
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
                'id': donor ['id'],
                'name' : donor['name'],
                'blood_group' : donor['blood_group'],
                'rh_factor' : donor['rh_factor'],
                'phone_number' : donor['phone_number'],
                'location' : donor['location'],
                'unit' : donor['unit'],
                'last_donation_date' : donor['last_donation_date']
                })
    return compatible_donors



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
