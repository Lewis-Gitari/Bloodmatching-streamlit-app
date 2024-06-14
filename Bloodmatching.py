import pandas as pd
import streamlit as st

donors = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Donor A', 'Donor B', 'Donor C'],
    'blood_group': ['A', 'B', 'O'],
    'rh_factor': ['+', '-', '+']
})

recipients = pd.DataFrame({
    'id': [101, 102, 103],
    'name': ['Recipient X', 'Recipient Y', 'Recipient Z'],
    'blood_group': ['A', 'AB', 'O'],
    'rh_factor': ['+', '+', '-']
})

# Blood group compatibility rules
compatible_blood_groups = {
    'A': ['A', 'AB'],
    'B': ['B', 'AB'],
    'AB': ['AB'],
    'O': ['A', 'B', 'AB', 'O']
}
def compatible_blood_groups (donor, recipient):
    if recipient['blood_group'] in compatible_blood_groups[donor['blood_group']]:
        # Check Rh factor compatibility
        if recipient['rh_factor'] == '+' or (recipient['rh_factor'] == '-' and donor['rh_factor'] == '-'):
            return True
    return False

def find_compatible_donors(recipient):
    compatible_donors = []
    for _, donor in donors.iterrows():
        if compatible_blood_groups(donor, recipient):
            compatible_donors.append(donor)
    return compatible_donors


# Streamlit app
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
st.title('Blood Group Matching')

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
