import streamlit as st

# Create a list of page names
pages = ["Home", "About", "Contact"]

# Add a selectbox to let the user choose a page
selected_page = st.sidebar.selectbox("Select a Page", pages)

# Depending on the selected page, display different content
if selected_page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page. This is the main page of your app.")

elif selected_page == "About":
    st.title("About Page")
    st.write("This is the About Page. Here you can provide information about your app or yourself.")

elif selected_page == "Contact":
    st.title("Contact Page")
    st.write("You can use this page to provide contact information.")

# You can add more pages and content as needed