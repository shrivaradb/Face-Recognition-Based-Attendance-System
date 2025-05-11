import cv2  # OpenCV for image and video processing
import numpy as np  # NumPy for numerical operations
import face_recognition  # Library for face detection and recognition
import os  # For file system operations
from datetime import datetime  # To handle date and time

# === Load known faces ===
path = 'images'  # Path where known face images are stored
images = []  # List to store image data
names = []  # List to store names
rolls = []  # List to store roll numbers

# Loop through each image file in the folder
for file in os.listdir(path):
    img = cv2.imread(f"{path}/{file}")  # Read image from file
    images.append(img)  # Add image to list
    roll, name = file.split('.')[0].split('_')  # Extract roll and name from filename
    rolls.append(roll)  # Store roll number
    names.append(name)  # Store name

# === Encode known faces ===
def find_encodings(images):
    encode_list = []  # List to hold encodings
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        encode = face_recognition.face_encodings(img)[0]  # Get face encoding
        encode_list.append(encode)  # Add encoding to list
    return encode_list

known_encodings = find_encodings(images)  # Generate encodings for all known faces

# === Mark attendance with descriptive format ===
def mark_attendance(roll, name):
    updated = False  # Flag to check if record is updated
    lines = []  # List to hold existing attendance lines
    today = datetime.now().strftime('%Y-%m-%d')  # Get current date in YYYY-MM-DD

    try:
        with open('attendance.txt', 'r') as f:  # Open attendance file
            lines = f.readlines()  # Read all lines
    except FileNotFoundError:
        pass  # If file doesn't exist, skip

    # Check if student already marked today
    for i in range(len(lines)):
        data = lines[i].strip().split(', ')  # Split line into parts
        if data[0] == f'Roll No: {roll}':  # If roll number matches
            count = int(data[2].split(': ')[1]) + 1  # Increment attendance count
            lines[i] = f'Roll No: {roll}, Name: {name}, Attendance: {count}, Date: {today}\n'  # Update line
            updated = True
            break

    # If student not marked yet, add new entry
    if not updated:
        lines.append(f'Roll No: {roll}, Name: {name}, Attendance: 1, Date: {today}\n')

    # Write updated lines back to file
    with open('attendance.txt', 'w') as f:
        f.writelines(lines)

# === Start webcam and recognize faces ===
cap = cv2.VideoCapture(0)  # Start webcam
print("Press '1' to quit.")
seen_today = set()  # Set to track which roll numbers have been marked

# Loop to continuously read frames from webcam
while True:
    success, img = cap.read()  # Read a frame
    if not success:
        break  # Exit if frame not captured

    small_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # Resize frame to 1/4 size
    rgb_small_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)  # Convert to RGB

    faces_cur_frame = face_recognition.face_locations(rgb_small_img)  # Detect face locations
    encodes_cur_frame = face_recognition.face_encodings(rgb_small_img, faces_cur_frame)  # Get encodings

    # Loop through detected faces
    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        matches = face_recognition.compare_faces(known_encodings, encode_face)  # Compare with known encodings
        face_dist = face_recognition.face_distance(known_encodings, encode_face)  # Calculate distances
        match_index = np.argmin(face_dist)  # Find index with smallest distance

        if matches[match_index]:  # If match found
            name = names[match_index]  # Get matched name
            roll = rolls[match_index]  # Get matched roll number
            
            if roll not in seen_today:  # If not already marked today
                mark_attendance(roll, name)  # Mark attendance
                seen_today.add(roll)  # Add to seen list

                # Scale face location back to original size
                y1, x2, y2, x1 = [v * 4 for v in face_loc]
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw rectangle
                cv2.putText(img, f'{name} ({roll})', (x1, y1 - 10),  # Display name and roll
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('Face Attendance', img)  # Show webcam feed
    
    if cv2.waitKey(1) == 49:  # Exit if key '1' is pressed (ASCII 49)
        break

cap.release()  # Release webcam
cv2.destroyAllWindows()  # Close OpenCV windows
