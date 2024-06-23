import streamlit as st
#import os
#import sys
from streamlit_option_menu import option_menu
from pages import Bloodmatching, Donors


st.set_page_config(
    page_title="Blood matching and Donor Management",
)

class MultiPage:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title = "Blood matching and Donor Management",
                Options = [ 'Bloodmatching', 'Donor',],
                default_index = 0
            )
            
            if app =='Bloodmatching':
                Bloodmatching.app()
            if app == 'Donors':
                Donors.app()

# Create an instance of the MultiPage class
app = MultiPage()

# Add applications to the MultiPage instance
app.add_app("Blood Matching", Bloodmatching.main)
app.add_app("Donor Management", Donors.main)


if __name__ == "__main__":
    app.run()
#sys.path.append(os.path.dirname(os.path.abspath(r'C:\\Users\ADMIN\course\Bloodmatching\Bloodmatching.py')))

#from pages import Bloodmatching, Donors


#st.sidebar.title('Navigation')
#page = st.sidebar.radio('Select a page:', ['Manage Donors', 'Search Donors'])

#if page == 'Manage Donors':
    #Bloodmatching.main()

#elif page == 'Search Donors':
 #  Donors.main()