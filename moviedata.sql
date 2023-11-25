USE moviebookingdb;

-- Insert sample data into Employee table
INSERT INTO Employee (EmployeeID, FirstName, LastName, Address, PhoneNo, Email, Position, Salary, ManagerID)
VALUES
    (1, 'John', 'Doe', '123 Main St', '555-1234', 'john.doe@email.com', 'Manager', 60000.00, NULL),
    (2, 'Jane', 'Smith', '456 Oak St', '555-5678', 'jane.smith@email.com', 'Employee', 45000.00, 1),
    (3, 'Bob', 'Johnson', '789 Pine St', '555-9876', 'bob.johnson@email.com', 'Employee', 50000.00, 1),
    (4, 'Alice', 'Williams', '101 Maple St', '555-4321', 'alice.williams@email.com', 'Manager', 70000.00, NULL),
    (5, 'Charlie', 'Brown', '202 Elm St', '555-8765', 'charlie.brown@email.com', 'Employee', 48000.00, 4),
	(6, 'Eva', 'Green', '303 Pine St', '555-1122', 'eva.green@email.com', 'Manager', 72000.00, NULL),
    (7, 'Michael', 'Johnson', '404 Elm St', '555-3344', 'michael.johnson@email.com', 'Employee', 49000.00, 6),
    (8, 'Sophia', 'Anderson', '505 Maple St', '555-5566', 'sophia.anderson@email.com', 'Employee', 52000.00, 6),
    (9, 'William', 'White', '606 Oak St', '555-7788', 'william.white@email.com', 'Manager', 75000.00, NULL),
    (10, 'Olivia', 'Wilson', '707 Main St', '555-9900', 'olivia.wilson@email.com', 'Employee', 51000.00, 9);
-- Insert sample data into Department table
INSERT INTO Department (DepartmentID, DepartmentName)
VALUES
    (1, 'HR'),
    (2, 'IT'),
    (3, 'Finance'),
    (4, 'Marketing'),
    (5, 'Operations'),
     (6, 'Sales'),
    (7, 'Customer Service'),
    (8, 'Research and Development'),
    (9, 'Legal'),
    (10, 'Public Relations');
-- Insert sample data into User table
INSERT INTO Users (UserID, CustomerName, ContactNo, Pass_word)
VALUES
    (1, 'Customer1', 1234567890, 'password1'),
    (2, 'Customer2', 2345678901, 'password2'),
    (3, 'Customer3', 3456789012, 'password3'),
    (4, 'Customer4', 4567890123, 'password4'),
    (5, 'Customer5', 5678901234, 'password5'),
    (6, 'Customer6', 6789012345, 'password6' ),
    (7, 'Customer7', 7890123456, 'password7' ),
    (8, 'Customer8', 8901234567, 'password8'),
    (9, 'Customer9', 9012345678, 'password9'),
    (10, 'Customer10', 4345678987, 'password10');

-- Insert sample data into Movies table
INSERT INTO Movies (MovieID, Title, Duration, Genre, Lang, Price)
VALUES
    (1, 'Inception', 120, 'Action', 'English', 400.00),
    (2, 'The Shawshank Redemption', 142, 'Drama', 'English', 599.00),
    (3, 'The Dark Knight', 152, 'Action', 'English', 499.00),
    (4, 'Pulp Fiction', 154, 'Crime', 'English', 259.00),
    (5, 'The Matrix', 136, 'Sci-Fi', 'English', 350.00),
    (6, 'Interstellar', 169, 'Sci-Fi', 'English', 499.00),
    (7, 'The Godfather', 175, 'Crime', 'English', 599.00),
    (8, 'Titanic', 195, 'Romance', 'English', 459.00),
    (9, 'Avatar', 162, 'Adventure', 'English', 599.00),
    (10, 'Joker', 122, 'Crime', 'English', 459.00);


-- Insert sample data into Theaters table
INSERT INTO Theaters (TheaterID, Name, Location, MovieID, MovieName)
VALUES
    (1, 'Theater A', 'City1', 1, 'Inception'),
    (2, 'Theater B', 'City2', 2, 'The Shawshank Redemption'),
    (3, 'Theater C', 'City3', 3, 'The Dark Knight'),
    (4, 'Theater D', 'City4', 1, 'Inception'),
    (5, 'Theater E', 'City5', 2, 'The Shawshank Redemption'),
    (6, 'City6 Theater F', 'City6', 6, 'Interstellar'),
    (7, 'City7 Theater G', 'City7', 7, 'The Godfather'),
    (8, 'City8 Theater H', 'City8', 8, 'Titanic'),
    (9, 'City9 Theater I', 'City9', 9, 'Avatar'),
    (10, 'City10 Theater J', 'City10', 10, 'Joker');
-- Insert sample data into Bookings table
INSERT INTO Bookings (BookingID, MovieID, TheaterID, SeatNumber, BookingDate)
VALUES
    (1, 1, 1, 'A1', '2023-01-10 14:00:00'),
    (2, 2, 2, 'B2', '2023-02-15 15:30:00'),
    (3, 3, 3, 'C3', '2023-03-20 18:45:00'),
    (4, 4, 4, 'D4', '2023-04-25 12:15:00'),
    (5, 5, 5, 'E5', '2023-05-30 20:00:00'),
    (6, 6, 6,'F6', '2023-06-10 14:00:00'),
    (7, 7, 7,'G7', '2023-07-15 15:30:00'),
    (8, 8, 8,'H8', '2023-08-20 18:45:00'),
    (9, 9, 9,'I9', '2023-09-25 12:15:00'),
    (10, 10, 10,'J10', '2023-10-30 20:00:00');

    -- Insert sample data into Payments table
INSERT INTO Payments (PaymentID, BookingID, Amount, PaymentDate)
VALUES
    (1, 1, 150.00, '2023-01-10 14:30:00'),
    (2, 2, 200.00, '2023-02-15 16:00:00'),
    (3, 3, 250.00, '2023-03-20 19:15:00'),
    (4, 4, 300.00, '2023-04-25 13:45:00'),
    (5, 5, 305.00, '2023-05-30 21:30:00'),
     (6, 6, 210.00, '2023-06-10 14:30:00'),
    (7, 7, 270.00, '2023-07-15 16:00:00'),
    (8, 8, 320.00, '2023-08-20 19:15:00'),
    (9, 9, 390.00, '2023-09-25 13:45:00'),
    (10, 10, 400.00, '2023-10-30 21:30:00');
