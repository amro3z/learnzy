# Online Learning Platform

## Project Idea and Scope

Create a responsive and engaging platform for online learning, targeting individuals looking to upskill in technology and programming. The platform includes functionalities such as course browsing and contact support. It enables users to learn skills on demand and offers course creators a simple way to distribute content.

---

## User Personas

### Goals:
- Learn web development basics to create projects.
- Explore advanced JavaScript concepts.

### Weakness Points:
- Finds most platforms cluttered and overwhelming.
- Needs a beginner-friendly layout.

---

## Functional Requirements

### Login Page
- Two login pages: one for students and one for instructors.

### Register Page
- Two register pages: one for students and one for instructors.

### Instructor Page
- Allows instructors to add or remove courses.

### Profile Page
- Displays the username for both students and instructors.
- Lists enrolled courses for students.
- Shows added courses for instructors.

### Home Page
- Displays available courses with descriptions and images.
- Links to course details and "Learn More" sections.
- Includes a search icon for finding courses.

### Course Pages
- Show course descriptions, instructor details, and pricing.
- Display course videos.

### Authentication
- Secure login and registration forms.
- Toggle between login and registration views.

### Contact Us
- Form for users to send messages (fields: name, email, and message).
- Displays contact information for direct communication.

---

## Non-Functional Requirements

### Performance
- Pages should load within 3 seconds under normal conditions.

### Usability
- Simple, intuitive navigation for non-technical users.
- Responsive design for desktop and mobile devices.

### Security
- Passwords must be encrypted before storage.

---

## Programming Languages Used

- **Python**: For backend development.
- **HTML, CSS, and JS**: For frontend development.
- **MySQL**: For database management.

---

## Diagrams and Screenshots

### Sequence Diagram
- (![image](https://github.com/user-attachments/assets/2a943382-f7ca-4bab-9d21-1a07f0ee0830)
)

### Class Diagram
- (![image](https://github.com/user-attachments/assets/4fb59373-e81a-405d-bdab-206ae8db5a96)
)

### Use Case Diagram
- (![image](https://github.com/user-attachments/assets/1a48a812-2c4c-4105-a0f0-469b2d1cfda4)
)

### Website Screenshots
- (![image](https://github.com/user-attachments/assets/73130d1f-24e7-46e3-a303-66a196229f8e)
  )
- (![image](https://github.com/user-attachments/assets/055cbe22-c356-4062-a7bb-4c70cb933023)
)
- (![image](https://github.com/user-attachments/assets/fa50e8eb-fade-40a9-9f44-2a8e8c797c94)
)
- (![image](https://github.com/user-attachments/assets/f634145b-1588-46c7-b6c5-7913d2b1139f)
)
- (![image](https://github.com/user-attachments/assets/ec5e537a-f441-471b-a3de-f63430fa2746)
)
- (![image](https://github.com/user-attachments/assets/cd622922-022a-4fd0-81f3-9948cfa4a865)
  )
- (![image](https://github.com/user-attachments/assets/7c255d0f-84cb-4f5c-8b45-f22e4093d36b)
  )
- (![image](https://github.com/user-attachments/assets/e0ff8902-1f31-4b17-bd61-327c9b282beb)
  )

- (![image](https://github.com/user-attachments/assets/4857ac3a-c0d7-407b-93c4-7cc084b32ae9)
  )

- (![image](https://github.com/user-attachments/assets/452d1e85-ef1b-406c-9994-8f2f7e562231)
  )
- (![image](https://github.com/user-attachments/assets/2ea70f60-e6e6-4f59-9d53-d3865d90a91a)
)
- (![image](https://github.com/user-attachments/assets/a76e51bb-f738-42eb-9fbe-bfbb2856fc4d)
)


---

## Test Cases and Their Screenshots

### Test Case 1: User Login
**Scenario**: Verify that a user can log in successfully.  
**Steps**:
1. Navigate to the login page.
2. Enter valid credentials (username and password).
3. Click the "Login" button.  
**Expected Result**:
- Dashboard displayed if the user exists.
- Error message "Invalid Username or password" if the user does not exist.
- ![image](https://github.com/user-attachments/assets/736be30a-d94c-41c5-bfbe-30fd8a74ab2f)


---

### Test Case 2: User Sign-Up
**Scenario**: Verify that a user can sign up successfully.  
**Steps**:
1. Navigate to the sign-up page.
2. Enter valid user details (username, email, password, etc.).
3. Click the "Sign Up" button.  
**Expected Result**:
- Redirect to the dashboard if sign-up is successful.
- Error message for issues (e.g., duplicate username).
- ![image](https://github.com/user-attachments/assets/8175cf1c-66f8-4344-b0f3-a39aebf52466)


---

### Test Case 3: Enroll in a Course
**Scenario**: Verify that a student can enroll in a course.  
**Steps**:
1. Log in as a student.
2. Navigate to the list of available courses.
3. Click "Enroll" on a course.  
**Expected Result**:
- Confirmation message if enrollment is successful.
- Error message for failure (e.g., invalid course ID).
- ![image](https://github.com/user-attachments/assets/a5fdb2d5-50c2-4341-bb15-195fd30a1f5a)


---

### Test Case 4: Watch a Course Video
**Scenario**: Verify that only enrolled students can watch course videos.  
**Steps**:
1. Log in as a student.
2. Attempt to watch a video from a course.  
**Expected Result**:
- Video plays for enrolled students.
- Prompt to enroll for non-enrolled students.
- ![image](https://github.com/user-attachments/assets/60136a67-0189-41c0-a31a-658d8fff6c58)


---

### Test Case 5: Add a Course (Instructor)
**Scenario**: Verify that an instructor can add a new course.  
**Steps**:
1. Log in as an instructor.
2. Navigate to the "Add Course" page.
3. Fill in course details (title, description, etc.) and submit.  
**Expected Result**:
- Confirmation message "Course added" for success.
- Appropriate error message for failure.
- ![image](https://github.com/user-attachments/assets/fbb8a2c3-db17-489a-8fd5-303955ef2cc5)


---

### Test Case 6: Delete a Course (Instructor)
**Scenario**: Verify that an instructor can delete a course.  
**Steps**:
1. Log in as an instructor.
2. Navigate to the list of created courses.
3. Select a course and click "Delete."  
**Expected Result**:
- Course is deleted.
- ![image](https://github.com/user-attachments/assets/ab239bf7-79c5-46bd-99da-42e5d2b88e00)


---

### Test Case 7: Invalid Login Attempt
**Scenario**: Verify that login fails for invalid credentials.  
**Steps**:
1. Navigate to the login page.
2. Enter invalid credentials (e.g., wrong password).
3. Click the "Login" button.  
**Expected Result**:
- Error message “Invalid credentials” appears.
- ![image](https://github.com/user-attachments/assets/7ae328ab-5910-41c0-8a1a-1c68d33faed6)


---

### Test Case 8: View Courses
**Scenario**: Verify that a user (student or instructor) can view all available courses.  
**Steps**:
1. Log in as a user.
2. Navigate to the "Courses" section.  
**Expected Result**:
- All available courses are listed.
- ![image](https://github.com/user-attachments/assets/a0d81ff8-0162-4809-be93-6aa204cd4f7e)


---

## Additional Links
- **GitHub Repository**: ([Link here](https://github.com/amro3z/learnzy.git))  
- **Meeting Link**: (https://nileuniversity.sharepoint.com/sites/Project_Meeting/Shared%20Documents/General/Recordings/Meeting%20in%20_General_-20241222_072337-Meeting%20Recording.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)
