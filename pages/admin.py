import mysql.connector as sql
import streamlit as st
import pandas as pd

conn = sql.connect(host='localhost', user='root',
                   password='Mysql Password', database='moviebookingdb')

cursor = conn.cursor()

def delete_row(table_name, row_id_column, delete_row_id):
    try:
        cursor.execute(
            f"DELETE FROM {table_name} WHERE {row_id_column} = %s", (delete_row_id,))
        conn.commit()
        st.success(
            f"Row with {row_id_column} {delete_row_id} deleted successfully.")
    except Exception as e:
        st.error(f"Error: {e}")


def employee():
    st.title("Employee Table")
    cursor.execute("SELECT * FROM Employee")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["EmployeeID", "FirstName", "LastName",
                          "Address", "PhoneNo", "Email", "Position", "Salary", "ManagerID"])
        st.dataframe(df)
    else:
        st.write("No data found in the Employee table.")

    if 'add_employee' not in st.session_state:
        st.session_state.add_employee = False

    if st.button("add employee"):
        st.session_state.add_employee = True

    if st.session_state.add_employee:
        employee_id = st.number_input("Enter the employee ID")
        first_name = st.text_input("Enter the first name")
        last_name = st.text_input("Enter the last name")
        address = st.text_input("Enter the address")
        phone_no = st.text_input("Enter the phone number")
        email = st.text_input("Enter the email")
        position = st.text_input("Enter the position")
        salary = st.number_input("Enter the salary")
        manager_id = st.number_input("Enter the manager ID")

        if st.button("add"):
            try:
                cursor.execute("INSERT INTO Employee (EmployeeID, FirstName, LastName, Address, PhoneNo, Email, Position, Salary, ManagerID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (employee_id, first_name, last_name, address, phone_no, email, position, salary, manager_id))
                conn.commit()
                st.success("Employee added")
                st.session_state.add_employee = False
            except Exception as e:
                st.error(f"Error: {e}")

    st.subheader("Delete Employee Entry")
    delete_row_id = st.number_input("Enter the EmployeeID to delete:")
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Employee", "EmployeeID", delete_row_id)


def department():
    st.title("Department Table")
    cursor.execute("SELECT * FROM Department")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["DepartmentID", "DepartmentName"])
        st.dataframe(df)
    else:
        st.write("No data found in the Department table.")

    if 'add_dept' not in st.session_state:
        st.session_state.add_dept = False

    if st.button("add dept"):
        st.session_state.add_dept = True

    if st.session_state.add_dept:
        dept_id = st.number_input("enter the dept id")
        dept_name = st.text_input("enter the dept name")
        if st.button("add"):
            try:
                cursor.execute(
                    "INSERT INTO Department (DepartmentID, DepartmentName) VALUES (%s,%s)", (dept_id, dept_name))
                conn.commit()
                st.success("dept added")
                st.session_state.add_dept = False
            except Exception as e:
                st.error(f"Error: {e}")
    st.subheader("Delete Department Entry")
    delete_row_id = st.number_input("Enter the DepartmentID to delete:")
    delete_button = st.button("Delete")

    if delete_button:
        try:
            cursor.execute(
                "DELETE FROM Department WHERE DepartmentID = %s", (delete_row_id,))
            conn.commit()
            st.success(
                f"Row with DepartmentID {delete_row_id} deleted successfully.")
        except Exception as e:
            st.error(f"Error: {e}")



def booking():
    st.title("Booking Table")
    cursor.execute("SELECT * FROM Bookings")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=[
                          "BookingID", "MovieID", "TheaterID", "SeatNumber", "BookingDate"])
        st.dataframe(df)
    else:
        st.write("No data found in the Bookings table.")

    if 'add_booking' not in st.session_state:
        st.session_state.add_booking = False

    if st.button("Add Booking"):
        st.session_state.add_booking = True

    if st.session_state.add_booking:
        movie_id = st.number_input("Enter the Movie ID")
        theater_id = st.number_input("Enter the Theater ID")
        seat_number = st.text_input("Enter the Seat Number")
        booking_date = st.date_input("Enter the Booking Date")

        if st.button("Add"):
            try:
                cursor.execute(
                    "INSERT INTO Bookings (MovieID, TheaterID, SeatNumber, BookingDate) VALUES (%s, %s, %s, %s)",
                    (movie_id, theater_id, seat_number, booking_date)
                )
                conn.commit()
                st.success("Booking added")
                st.session_state.add_booking = False
            except Exception as e:
                st.error(f"Error: {e}")

    st.subheader("Delete Booking Entry")
    delete_row_id = st.number_input("Enter the BookingID to delete:")
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Bookings", "BookingID", delete_row_id)

def payment():
    st.title("Payment Table")
    
    # Join Payments and Bookings tables
    query = """
        SELECT Payments.PaymentID, Payments.BookingID, Payments.Amount, Payments.PaymentDate, Bookings.MovieID, Bookings.TheaterID, Bookings.SeatNumber, Bookings.BookingDate
        FROM Payments
        LEFT JOIN Bookings ON Payments.BookingID = Bookings.BookingID
    """
    
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["PaymentID", "BookingID", "Amount", "PaymentDate", "MovieID", "TheaterID", "SeatNumber", "BookingDate"])
        st.dataframe(df)
    else:
        st.write("No data found in the Payments and Bookings tables.")

    if 'add_payment' not in st.session_state:
        st.session_state.add_payment = False

    if st.button("Add Payment"):
        st.session_state.add_payment = True

    if st.session_state.add_payment:
        booking_id = st.number_input("Enter the Booking ID")
        amount = st.number_input("Enter the payment amount")
        payment_date = st.date_input("Enter the payment date")

        if st.button("Process Payment"):
            try:
                # Placeholder: Perform payment processing here (e.g., connect to a payment gateway)
                # For demonstration purposes, we'll assume the payment is successful.
                payment_id = insert_payment_data(booking_id, amount, payment_date)
                st.success(f"Payment successful. Payment ID: {payment_id}")
                st.session_state.add_payment = False
            except Exception as e:
                st.error(f"Error processing payment: {e}")

    st.subheader("Delete Payment Entry")
    delete_row_id = st.number_input("Enter the PaymentID to delete:")
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Payments", "PaymentID", delete_row_id)

# Function to insert payment data into the Payments table
def insert_payment_data(booking_id, amount, payment_date):
    try:
        cursor.execute(
            "INSERT INTO Payments (BookingID, Amount, PaymentDate) VALUES (%s, %s, %s)",
            (booking_id, amount, payment_date)
        )
        conn.commit()
        return cursor.lastrowid  # Return the ID of the inserted payment
    except Exception as e:
        conn.rollback()
        raise e

def produces():
    st.title("Produces Table")
    cursor.execute("SELECT * FROM Produces")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["DepartmentID", "ProductID"])
        st.dataframe(df)
    else:
        st.write("No data found in the Produces table.")

    if 'add_produces' not in st.session_state:
        st.session_state.add_produces = False

    if st.button("add produces"):
        st.session_state.add_produces = True

    if st.session_state.add_produces:
        department_id = st.number_input("Enter the department ID")
        product_id = st.number_input("Enter the product ID")

        if st.button("add"):
            try:
                cursor.execute("INSERT INTO Produces (DepartmentID, ProductID) VALUES (%s, %s)",
                               (department_id, product_id))
                conn.commit()
                st.success("Produces added")
                st.session_state.add_produces = False
            except Exception as e:
                st.error(f"Error: {e}")
    # Add delete functionality
    st.subheader("Delete Produces Entry")
    delete_row_id = st.number_input("Enter the DepartmentID to delete:")
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Produces", "DepartmentID", delete_row_id)


def supplies():
    st.title("Supplies Table")
    cursor.execute("SELECT * FROM Supplies")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(
            result, columns=["SupplierID", "ProductID", "SupplyPrice", "SupplyDate"])
        st.dataframe(df)
    else:
        st.write("No data found in the Supplies table.")

    if 'add_supplies' not in st.session_state:
        st.session_state.add_supplies = False

    if st.button("add supplies"):
        st.session_state.add_supplies = True

    if st.session_state.add_supplies:
        supplier_id = st.number_input("Enter the supplier ID")
        product_id = st.number_input("Enter the product ID")
        supply_price = st.number_input("Enter the supply price")
        supply_date = st.date_input("Enter the supply date")

        if st.button("add"):
            try:
                cursor.execute("INSERT INTO Supplies (SupplierID, ProductID, SupplyPrice, SupplyDate) VALUES (%s, %s, %s, %s)",
                               (supplier_id, product_id, supply_price, supply_date))
                conn.commit()
                st.success("Supplies added")
                st.session_state.add_supplies = False
            except Exception as e:
                st.error(f"Error: {e}")
    # Add delete functionality
    st.subheader("Delete Supplies Entry")
    delete_row_id = st.number_input("Enter the SupplierID to delete:")
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Supplies", "SupplierID", delete_row_id)


def add_employee_with_manager(employee_id, manager_id):
    try:
        # Define the stored procedure SQL query
        sql_query = """
            CREATE PROCEDURE InsertManagerIfNotNull(IN new_employee_id INT, IN new_manager_id INT)
            BEGIN
                IF new_manager_id IS NOT NULL THEN
                    INSERT INTO Manages (ManagerID, EmployeeID) VALUES (new_manager_id, new_employee_id);
                END IF;
            END;
        """

        # Execute the stored procedure creation query
        cursor.execute(sql_query)
        conn.commit()

        # Execute the stored procedure and insert into Employee table
        cursor.callproc('InsertManagerIfNotNull', (employee_id, manager_id))
        conn.commit()

        st.success("Employee added")
        st.session_state.add_employee = False
    except Exception as e:
        st.error(f"Error: {e}")
def movie():
    st.title("Movie Table")
    cursor.execute("SELECT * FROM Movies")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["MovieID", "Title", "Duration", "Genre", "Lang", "Price"])
        st.dataframe(df)
    else:
        st.write("No data found in the Movie table.")

    if 'add_movie' not in st.session_state:
        st.session_state.add_movie = False
    if 'update_movie' not in st.session_state:
        st.session_state.update_movie = False

    if st.button("Add Movie"):
        st.session_state.add_movie = True
    if st.button("Update Movie"):
        st.session_state.update_movie = True

    if st.session_state.add_movie:
        title = st.text_input("Enter the movie title")
        duration = st.number_input("Enter the movie duration")
        genre = st.text_input("Enter the movie genre")
        Language = st.text_input("Enter the movie language")
        price = st.number_input("Enter Price")

        if st.button("Add"):
            try:
                cursor.execute(
                    "INSERT INTO Movies (Title, Duration, Genre, Lang, Price) VALUES (%s, %s, %s, %s, %s)",
                    (title, duration, genre, Language, price)
                )
                conn.commit()
                st.success("Movie added")
                st.session_state.add_movie = False
            except Exception as e:
                st.error(f"Error: {e}")

    # Allow the user to input new data
    if st.session_state.update_movie:
        update_movie_id = st.number_input(
            "Enter the MovieID to update:", step=1.0, format="%s")
        cursor.execute(
            "SELECT * FROM Movies WHERE MovieID = %s", (update_movie_id,))
        existing_data = cursor.fetchone()

        if existing_data:
            # Display the existing data for the user to modify
            st.subheader("Existing Movie Data")
            existing_df = pd.DataFrame([existing_data], columns=[
                "MovieID", "Title", "Duration", "Genre", "Lang", "Price"])
            st.dataframe(existing_df)

            # Allow the user to input new data
            new_title = st.text_input("Enter the new movie title", existing_data[1])
            new_duration = st.number_input(
                "Enter the new movie duration", float(existing_data[2]))
            new_genre = st.text_input(
                "Enter the new movie genre", existing_data[3])
            new_language = st.text_input(
                "Enter the new movie language", existing_data[4])
            new_price = st.number_input(
                "Enter the new movie price", float(existing_data[5]))

            # Update the data in the database
            update_data = (new_title, new_duration, new_genre, new_language, new_price, update_movie_id)
            update_query = "UPDATE Movies SET Title=%s, Duration=%s, Genre=%s, Lang=%s, Price=%s WHERE MovieID=%s"
            if st.button("Commit"):
                try:
                    cursor.execute(update_query, update_data)
                    conn.commit()
                    st.success("Movie data updated successfully.")
                    st.session_state.update_movie = False
                except Exception as e:
                    st.error(f"Error updating data: {e}")
        else:
            st.warning(f"No data found for MovieID {update_movie_id}.")

    # Add delete functionality
    st.subheader("Delete Movie Entry")
    delete_row_id = st.number_input("Enter the Movie to delete:", step=1)
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Movies", "MovieID", delete_row_id)



def users():
    st.title("Users Table")
    cursor.execute("SELECT *FROM Users")
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=[
                          "UserID", "CustomerName", "ContactNo", "Password", "Time_of_Signup"])
        st.dataframe(df)
    else:
        st.write("No data found in the Users table.")

    if 'add_user' not in st.session_state:
        st.session_state.add_user = False
    if 'update_user' not in st.session_state:
        st.session_state.update_user = False

    if st.button("Add User"):
        st.session_state.add_user = True
    if st.button("Update User"):
        st.session_state.update_user = True

    if st.session_state.add_user:
        customer_name = st.text_input("Enter the customer name")
        contact_no = st.text_input("Enter the contact number")
        password = st.text_input("Enter the password", type="password")

        if st.button("Add"):
            try:
                cursor.execute("INSERT INTO Users (CustomerName, ContactNo, Pass_word, Time_of_Signup) VALUES (%s, %s, %s, NOW())",
                               (customer_name, contact_no, password))
                conn.commit()
                st.success("User added")
                st.session_state.add_user = False
            except Exception as e:
                st.error(f"Error: {e}")

    # Allow the user to input new data
    if st.session_state.update_user:
        update_user_id = st.number_input(
            "Enter the UserID to update:", step=1, format="%d")
        cursor.execute(
            "SELECT * FROM Users WHERE UserID = %s", (update_user_id,))
        existing_data = cursor.fetchone()

        if existing_data:
            # Display the existing data for the user to modify
            st.subheader("Existing User Data")
            existing_df = pd.DataFrame([existing_data], columns=[
                "UserID", "CustomerName", "ContactNo", "Password", "Time_of_Signup"])
            st.dataframe(existing_df)

            # Allow the user to input new data
            new_customer_name = st.text_input("Enter the new customer name", existing_data[1])
            new_contact_no = st.text_input(
                "Enter the new contact number", existing_data[2])
            new_password = st.text_input(
                "Enter the new password", existing_data[3])

            # Update the data in the database
            update_data = (new_customer_name, new_contact_no, new_password, update_user_id)
            update_query = "UPDATE Users SET CustomerName=%s, ContactNo=%s, Pass_word=%s WHERE UserID=%s"
            if st.button("Commit"):
                try:
                    cursor.execute(update_query, update_data)
                    conn.commit()
                    st.success("User data updated successfully.")
                    st.session_state.update_user = False
                except Exception as e:
                    st.error(f"Error updating data: {e}")
        else:
            st.warning(f"No data found for UserID {update_user_id}.")

    # Add delete functionality
    st.subheader("Delete User Entry")
    delete_row_id = st.number_input("Enter the UserID to delete:", step=1)
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("Users", "UserID", delete_row_id)

# Function for managing Theaters
def theater():
    st.title("Theater Table")
    cursor.execute("SELECT * FROM theaters")  # Update table name to "theaters"
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["TheaterID", "Name", "Location","MovieID","MovieName"])
        st.dataframe(df)
    else:
        st.write("No data found in the Theaters table.")

    if 'add_theater' not in st.session_state:
        st.session_state.add_theater = False
    if 'update_theater' not in st.session_state:
        st.session_state.update_theater = False

    if st.button("Add Theater"):
        st.session_state.add_theater = True
    if st.button("Update Theater"):
        st.session_state.update_theater = True

    if st.session_state.add_theater:
        theater_name = st.text_input("Enter the theater name")
        location = st.text_input("Enter the location")
        mov_id=st.number_input("Enter Movie ID")
        mov_name=st.text_input("Enter MOvie Name")

        if st.button("Add"):
            try:
                cursor.execute(
                    "INSERT INTO theaters (Name, Location,MovieID,MovieName) VALUES (%s, %s,%s,%s)",  # Update table name to "theaters"
                    (theater_name, location,mov_id,mov_name)
                )
                conn.commit()
                st.success("Theater added")
                st.session_state.add_theater = False
            except Exception as e:
                st.error(f"Error: {e}")

    # Allow the user to input new data
    if st.session_state.update_theater:
        update_theater_id = st.number_input(
            "Enter the TheaterID to update:", step=1, format="%d")
        cursor.execute(
            "SELECT * FROM theaters WHERE TheaterID = %s", (update_theater_id,))
        existing_data = cursor.fetchone()

        if existing_data:
            # Display the existing data for the user to modify
            st.subheader("Existing Theater Data")
            existing_df = pd.DataFrame([existing_data], columns=[
                "TheaterID", "Name", "Location", "MovieID", "MovieName"])
            st.dataframe(existing_df)

            # Allow the user to input new data
            new_theater_name = st.text_input("Enter the new theater name", existing_data[1])
            new_location = st.text_input(
                "Enter the new location", existing_data[2])
            new_movie_id = st.number_input(
                "Enter the new Movie ID", existing_data[3])
            new_movie_name = st.text_input(
                "Enter the new Movie Name", existing_data[4])

            # Update the data in the database
            update_data = (new_theater_name, new_location, new_movie_id, new_movie_name, update_theater_id)
            update_query = "UPDATE theaters SET Name=%s, Location=%s, MovieID=%s, MovieName=%s WHERE TheaterID=%s"
            if st.button("Commit"):
                try:
                    cursor.execute(update_query, update_data)
                    conn.commit()
                    st.success("Theater data updated successfully.")
                    st.session_state.update_theater = False
                except Exception as e:
                    st.error(f"Error updating data: {e}")
        else:
            st.warning(f"No data found for TheaterID {update_theater_id}.")

    # Add delete functionality
    st.subheader("Delete Theater Entry")
    delete_row_id = st.number_input("Enter the TheaterID to delete:", step=1)
    delete_button = st.button("Delete")

    if delete_button:
        delete_row("theaters", "TheaterID", delete_row_id)  # Update table name to "theaters"

def admin_login():
    st.title("Admin Login Page")
    if 'admin_login' not in st.session_state:
        st.session_state.admin_login = False
    if not st.session_state.admin_login:
        admin_username = st.text_input("Enter Admin Username:")
        admin_password = st.text_input(
            "Enter Admin Password:", type="password")
        if st.button("login"):
            if admin_username == 'admin' and admin_password == 'admin123':
                st.success('successfully logged in as admin')
                st.session_state.admin_login = True
            else:
                st.error("Invalid credentials")

    if st.session_state.admin_login:
        if st.button("Logout"):
            st.session_state.admin_login = False
    if st.session_state.admin_login:
        menu = ["Employees", "Departments",
                 "Theaters", "Users", "Booking", "Movie",
                "Payment"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Employees":
            employee()
        if choice == 'Departments':
            department()
        if choice == "Theaters":
            theater()
        if choice == "Users":
            users()
        if choice == "Movie":
            movie()
        if choice == "Booking":
            booking()
        if choice == "Payment":
            payment()

        # login_button = st.button("Login")
        # if login_button and admin_username == "admin" and admin_password == "admin_password":
        #     st.session_state.admin_login = True
        #     return "admin", None
        # elif login_button:
        #     st.warning("Invalid credentials")


admin_login()
