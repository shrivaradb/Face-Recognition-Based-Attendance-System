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

## 📁 Project Structure

