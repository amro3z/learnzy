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
- (Screenshot here)

### Class Diagram
- (Screenshot here)

### Use Case Diagram
- (Screenshot here)

### Website Screenshots
- (Screenshots here)

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

---

### Test Case 4: Watch a Course Video
**Scenario**: Verify that only enrolled students can watch course videos.  
**Steps**:
1. Log in as a student.
2. Attempt to watch a video from a course.  
**Expected Result**:
- Video plays for enrolled students.
- Prompt to enroll for non-enrolled students.

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

---

### Test Case 6: Delete a Course (Instructor)
**Scenario**: Verify that an instructor can delete a course.  
**Steps**:
1. Log in as an instructor.
2. Navigate to the list of created courses.
3. Select a course and click "Delete."  
**Expected Result**:
- Course is deleted.

---

### Test Case 7: Invalid Login Attempt
**Scenario**: Verify that login fails for invalid credentials.  
**Steps**:
1. Navigate to the login page.
2. Enter invalid credentials (e.g., wrong password).
3. Click the "Login" button.  
**Expected Result**:
- Error message “Invalid credentials” appears.

---

### Test Case 8: View Courses
**Scenario**: Verify that a user (student or instructor) can view all available courses.  
**Steps**:
1. Log in as a user.
2. Navigate to the "Courses" section.  
**Expected Result**:
- All available courses are listed.

---

## Additional Links
- **GitHub Repository**: ([Link here](https://github.com/amro3z/learnzy.git))  
- **Meeting Link**: (https://nileuniversity.sharepoint.com/sites/Project_Meeting/Shared%20Documents/General/Recordings/Meeting%20in%20_General_-20241222_072337-Meeting%20Recording.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)
