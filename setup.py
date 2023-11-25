import mysql.connector
from datetime import datetime
import pandas as pd

class MovieBookingDBSetup:
    host = "localhost"
    user = "root"
    password = "MySQLPassword"
    db = "moviebookingdb"

    def create_movie_booking_database(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            port=3306,
            password=self.password
        )
        c = db.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS moviebookingdb")
        c.close()
        db.close()

    def create_all_tables(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        self.create_movies_table(db)
        self.create_theaters_table(db)
        self.create_bookings_table(db)
        self.create_payments_table(db)
        self.create_users_table(db)
        self.create_employee_table(db)
        self.create_department_table(db)
        db.close()

    def create_employee_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Employee (
                        EmployeeID INTEGER UNSIGNED PRIMARY KEY,
                        FirstName VARCHAR(255),
                        LastName VARCHAR(255),
                        Address VARCHAR(255),
                        PhoneNo VARCHAR(10),
                        Email VARCHAR(255),
                        Position VARCHAR(255),
                        Salary DECIMAL(10,2),
                        ManagerID INTEGER UNSIGNED,
                        FOREIGN KEY (ManagerID) REFERENCES Employee(EmployeeID)
                            ON DELETE SET NULL
                            ON UPDATE CASCADE
                    )""")
        c.close()

    def create_department_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Department (
                        DepartmentID INTEGER PRIMARY KEY,
                        DepartmentName VARCHAR(255)
                    )""")
        c.close()

    def create_movies_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Movies (
                    MovieID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Title VARCHAR(255),
                    Duration INTEGER,
                    Genre VARCHAR(255),
                    Lang VARCHAR(255),
                    Price DECIMAL(10, 2) 
                )""")
        c.close()

    def create_theaters_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Theaters (
                    TheaterID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Name VARCHAR(255),
                    Location VARCHAR(255),
                    MovieID INTEGER,
                    MovieName VARCHAR(255),
                    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
                )""")
        c.close()

    def create_bookings_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Bookings (
                        BookingID INTEGER PRIMARY KEY AUTO_INCREMENT,
                        MovieID INTEGER,
                        TheaterID INTEGER,
                        SeatNumber VARCHAR(10),
                        BookingDate DATETIME,
                        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
                            ON DELETE CASCADE
                            ON UPDATE CASCADE,
                        FOREIGN KEY (TheaterID) REFERENCES Theaters(TheaterID)
                            ON DELETE CASCADE
                            ON UPDATE CASCADE
                    )""")
        c.close()

    def create_payments_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Payments (
                        PaymentID INTEGER PRIMARY KEY AUTO_INCREMENT,
                        BookingID INTEGER,
                        Amount DECIMAL(10, 2),
                        PaymentDate DATETIME,
                        FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
                            ON DELETE CASCADE
                            ON UPDATE CASCADE
                    )""")
        c.close()

    def create_users_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Users (
                        UserID INTEGER PRIMARY KEY AUTO_INCREMENT,
                        CustomerName VARCHAR(255),
                        ContactNo VARCHAR(10) UNIQUE,
                        Pass_word VARCHAR(25),
                        Time_of_Signup DATETIME
                    )""")
        c.close()

    def before_user_insert_trigger(self, db):
        c = db.cursor()
        c.execute("""CREATE TRIGGER IF NOT EXISTS before_user_insert
                    BEFORE INSERT ON Users
                    FOR EACH ROW
                    BEGIN
                    SET NEW.Time_of_signup = NOW();
                    END;
        """)
        c.close()

    def additional_trigger_example(self, db):
        c = db.cursor()
        c.execute("""
            CREATE TRIGGER IF NOT EXISTS before_payment_insert
            BEFORE INSERT ON Payments
            FOR EACH ROW
            BEGIN
                SET NEW.PaymentDate = NOW();
            END;
        """)
        c.close()

    def create_all_triggers(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        self.before_user_insert_trigger(db)
        self.additional_trigger_example(db)
        db.close()

# Usage
movieBookingDBSetup = MovieBookingDBSetup()
movieBookingDBSetup.create_movie_booking_database()
movieBookingDBSetup.create_all_tables()
movieBookingDBSetup.create_all_triggers()
