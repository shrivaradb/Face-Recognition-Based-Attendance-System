# Face Recognition Attendance System

A real-time face recognition-based attendance system built using Python, OpenCV, and the face_recognition library. This project automates attendance by detecting and recognizing faces through a webcam feed and logs the details (name, roll number, date, and count) into a file.

---

## 📌 Project Description

This Face Recognition Attendance System is a computer vision project that captures real-time video input, detects faces, and matches them with a set of known faces. When a face is successfully matched, the system marks attendance by logging the roll number, name, date, and attendance count into a text file.

The system eliminates the need for manual attendance tracking and prevents issues like proxy attendance. It is useful for classrooms, offices, or events where attendance needs to be tracked efficiently and accurately.

---

## 🚀 Features

- Real-time face detection and recognition
- Automatically logs attendance with:
  - Roll number
  - Name
  - Date
  - Count of attendances
- Prevents duplicate attendance for the same day
- Simple text-based attendance log (`attendance.txt`)
- Lightweight and easy to deploy

---

## 🧰 Technologies Used

- **Python 3**
- **OpenCV** (`cv2`)
- **face_recognition**
- **NumPy**
- **datetime**
- **os (standard library)**

---

## 🛠️ How to Use

1. **Install Required Libraries**
   - Open your terminal or command prompt.
   - Run the following command to install the required dependencies:
     ```
     pip install opencv-python face_recognition numpy
     ```

2. **Add Known Faces**
   - Navigate to the `images/` directory.
   - Add face images of people you want to recognize. Make sure:
     - Each image file is named in the format: `RollNumber_Name.jpg` (e.g., `1_Arnav.jpg`).
     - Each image contains one clear, front-facing face.

3. **Run the System**
   - Open the terminal in the project directory.
   - Run the main script:
     ```bash
     python main.py
     ```
   - The webcam will activate and begin scanning for faces.

4. **Mark Attendance**
   - When a face is recognized:
     - It will display the name and roll number on screen.
     - It will log the attendance to `attendance.txt`.

5. **Stop the System**
   - To stop the webcam and end the program, press the `1` key.

6. **Check Attendance**
   - Open `attendance.txt`.
   - You'll see entries with:
     - Roll Number
     - Name
     - Date
     - Count (number of times the person has been marked present)

---



