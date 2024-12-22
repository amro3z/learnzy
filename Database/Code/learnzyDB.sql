create database learnzydb;
use learnzydb;

-- Create Users table 
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('student', 'instructor') DEFAULT 'student',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Categories table 
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Courses table 
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) DEFAULT 0.00,
    instructor_id INT NOT NULL,
    category_id INT NOT NULL,
    video_url VARCHAR(255),
    image_url VARCHAR(255), 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Create Enrollments table 
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create Payments table 
CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create Reviews table 
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Inserting ata
INSERT INTO Users (name, email, password, role) VALUES
('Ahmed Ali', 'ahmed.ali@example.com', 'password123', 'instructor'),
('Sara Mohamed', 'sara.mohamed@example.com', 'password456', 'instructor'),
('Omar Hany', 'omar.hany@example.com', 'password789', 'student'),
('Learnzy', 'Learnzy@example.com', '123', 'student');

INSERT INTO Categories (name) VALUES
('Programming'),
('Design'),
('Marketing'),
('Business'),
('Photography');

INSERT INTO Courses (title, description, price, instructor_id, category_id) VALUES
('Introduction to Python', 'Learn Python from scratch.', 50.00, 1, 1),
('Advanced JavaScript', 'Master advanced concepts in JavaScript.', 75.00, 1, 1),
('Graphic Design Basics', 'Learn the principles of graphic design.', 40.00, 2, 2),
('Digital Marketing 101', 'Understand the fundamentals of digital marketing.', 60.00, 2, 3),
('Photography for Beginners', 'Master basic photography skills.', 30.00, 2, 5);

ALTER TABLE Reviews 
MODIFY rating DOUBLE(3, 1);
select * from users;
INSERT INTO Reviews (user_id, course_id, rating, comment) 
VALUES (3, 1, 4, 'Great course, learned a lot!'), (3, 2, 5, 'Excellent content and teaching quality!') ,  (3, 3, 4.5, 'Love it!');

SELECT * FROM Users;

SELECT * FROM Categories;

SELECT * FROM Courses;

SELECT * FROM Enrollments;

SELECT * FROM Payments;

SELECT * FROM Reviews;