import face_recognition
import cv2
import os

def authenticate_user():
    api_key = input("Enter your FACE RECOGNITION API key (leave blank if not using): ")

    known_faces_dir = "face_data"
    if not os.path.exists(known_faces_dir):
        os.makedirs(known_faces_dir)

    known_encodings = []
    for filename in os.listdir(known_faces_dir):
        image_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])

    print("[*] Scanning face using webcam...")
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()

    if not ret:
        print("[-] Failed to access camera.")
        return False

    rgb_frame = frame[:, :, ::-1]
    encodings = face_recognition.face_encodings(rgb_frame)

    if encodings:
        for known_encoding in known_encodings:
            match = face_recognition.compare_faces([known_encoding], encodings[0])
            if match[0]:
                print("[+] Face recognized!")
                return True

    print("[-] Face not recognized.")
    return False