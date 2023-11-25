import mysql.connector as sql
import streamlit as st
import pandas as pd

conn = sql.connect(host='localhost', user='root', password='MySQLPassword', database='moviebookingdb')
cursor = conn.cursor()

# Function to validate user login
def validate_user(phno, password):
    query = "SELECT * FROM users WHERE ContactNo = %s AND pass_word = %s"
    cursor.execute(query, (phno, password))
    result = cursor.fetchall()
    return len(result) > 0

# Function to display movie information
def movie_t():
    st.title("Movie Table")
    cursor.execute("SELECT * FROM Movies")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["MovieID", "Title", "Duration", "Genre", "Lang", "Price"])
        st.dataframe(df)
    else:
        st.write("No data found in the Movie table.")

# Function to display movie and theater information
def movie_theater_info():
    st.title("Movie and Theater Information")
    cursor.execute("""
        SELECT m.MovieID, m.Title AS MovieTitle, m.Duration, m.Genre, m.Lang, t.TheaterID, t.Name, t.Location
        FROM Movies m
        JOIN Theaters t ON m.MovieID = t.MovieID
    """)
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["MovieID", "Movie Title", "Duration", "Genre", "Language", "TheaterID", "Theater Name", "Location"])
        st.dataframe(df)
    else:
        st.write("No data found in the Movie and Theater tables.")

# Function for ticket booking
def book_ticket():
    st.title("Book Tickets")
    movie_id = st.number_input("Enter Movie ID for the movie you want to book")
    theater_id = st.number_input("Enter Theater ID", min_value=1)
    seat_number = st.text_input("Enter Seat Number")
    num_tickets = st.number_input("Enter the number of tickets", min_value=1)

    # Fetch the price from the Movies table based on the selected movie
    cursor.execute("SELECT Price FROM Movies WHERE MovieID = %s", (movie_id,))
    price_result = cursor.fetchone()
    if price_result:
        price = price_result[0]
    else:
        st.error("Error fetching movie price.")
        return

    total_price = num_tickets * price

    st.write(f"Ticket Price: ₹{price} per ticket")
    st.write(f"Total Price for {num_tickets} tickets: ₹{total_price}")

    if st.button("Book Tickets"):
        try:
            # Perform ticket booking logic (you may need to adjust this based on your database schema)
            cursor.execute("INSERT INTO Bookings (MovieID, TheaterID, SeatNumber, BookingDate) VALUES (%s, %s, %s, NOW())",
                           (movie_id, theater_id, seat_number))
            conn.commit()

            # Fetch the details of the booked ticket for confirmation
            cursor.execute("SELECT * FROM Bookings WHERE MovieID = %s AND TheaterID = %s AND SeatNumber = %s",
                           (movie_id, theater_id, seat_number))
            booked_ticket = cursor.fetchone()

            # Add payment information to the Payment table
            cursor.execute("INSERT INTO Payments (BookingID, Amount, PaymentDate) VALUES (%s, %s, NOW())",
                           (booked_ticket[0], total_price))
            conn.commit()

            st.success("Tickets booked successfully! Total Price: ₹{}".format(total_price))
            st.write("Booking Details:")
            st.write(f"Booking ID: {booked_ticket[0]}")
            st.write(f"Movie ID: {booked_ticket[1]}")
            st.write(f"Theater ID: {booked_ticket[2]}")
            st.write(f"Seat Number: {booked_ticket[3]}")
            st.write(f"Booking Date: {booked_ticket[4]}")

        except Exception as e:
            st.error(f"Error: {e}")

# Function for viewing booking history
def view_booking_history(customer_ph):
    st.title("Booking History")
    
    # Fetch booking history based on the customer's phone number
    cursor.execute("""
        SELECT b.BookingID, m.Title AS MovieTitle, t.Name AS TheaterName, b.SeatNumber, b.BookingDate, p.Amount
        FROM Bookings b
        JOIN Movies m ON b.MovieID = m.MovieID
        JOIN Theaters t ON b.TheaterID = t.TheaterID
        JOIN Payments p ON b.BookingID = p.BookingID
        WHERE b.CustomerPhone = %s
    """, (customer_ph,))
    
    booking_history = cursor.fetchall()

    if booking_history:
        df = pd.DataFrame(booking_history, columns=["BookingID", "Movie Title", "Theater Name", "Seat Number", "Booking Date", "Amount"])
        st.dataframe(df)
    else:
        st.write("No booking history found for this customer.")

# Function for customer login
# Function for customer login
def customer_login():
    st.title("Customer Login Page")

    if 'customer_login' not in st.session_state:
        st.session_state.customer_login = False

    customer_ph = None  # Initialize customer_ph outside the conditional block

    if not st.session_state.customer_login:
        customer_ph = st.text_input("Enter Customer Phone Number:")
        customer_password = st.text_input("Enter Customer Password:", type="password")

        if st.button("Login"):
            if validate_user(customer_ph, customer_password):
                st.session_state.customer_login = True
            else:
                st.warning("Username does not exist. Please Sign up")

    if st.session_state.customer_login:
        if st.button("Logout"):
            st.session_state.customer_login = False

    if st.session_state.customer_login:
        menu = ["Movies", "Movie and Theater Info", "Book Tickets", "Booking History"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Movies":
            movie_t()
        elif choice == "Movie and Theater Info":
            movie_theater_info()
        elif choice == 'Book Tickets':
            book_ticket()
        elif choice == "Booking History":
            if customer_ph is not None:
                view_booking_history(customer_ph)

# Main function
customer_login()

# Close the database connection
conn.close()
 