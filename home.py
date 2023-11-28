import mysql.connector as sql
import streamlit as st
import pandas as pd

# Database connection
conn = sql.connect(host='localhost', user='root', password='MySQL Paasword', database='moviebookingdb')
cursor = conn.cursor()

# Add some CSS styles
import mysql.connector as sql
import streamlit as st
import pandas as pd

# Database connection
conn = sql.connect(host='localhost', user='root', password='Sama123#$#sama', database='moviebookingdb')
cursor = conn.cursor()

# Add some CSS styles
st.markdown(
    """
    <style>
        body {
            background-color: #000 !important;  /* Set background color to black */
            color: #ffd700 !important;  /* Set text color to gold */
            font-family: 'Arial', sans-serif;
        }
        .css-1evk8u1 {
            background-color: #333 !important;  /* Set sidebar background color to dark gray */
        }
        .css-1aumxhk {
            color: #fff !important;  /* Set sidebar text color to white */
        }
        .css-hi6a2p {
            color: #004080 !important;  /* Set header text color to a specific shade of blue */
        }
        .dataframe {
            border-collapse: collapse;
            margin: 10px 0;
            font-size: 14px;
            text-align: left;
            width: 100%;
            overflow: hidden;
            word-break: break-word;
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and header
st.title("Movie Ticket Booking System")
st.header("Welcome to the Movie Ticket Booking Database")

# Sidebar with options
st.sidebar.header("Options")
selected_option = st.sidebar.radio("Select Option", ["Home", "Movies"])

# Home page content
if selected_option == "Home":
    st.write("This is the home page. Choose an option from the sidebar.")

# Example for "Movies" page
elif selected_option == "Movies":
    st.header("Movies List")
    # Retrieve movies from the database
    cursor.execute("SELECT * FROM movies")
    movies_data = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    movies_df = pd.DataFrame(movies_data, columns=columns)
    st.dataframe(movies_df)

# Close the database connection
conn.close()
