import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ck
import mediapipe as mp
import cv2
from PIL import Image, ImageTk

landmarks = ['x1', 'y1', 'z1', 'v1', 'x2', 'y2', 'z2', 'v2', 'x3', 'y3', 'z3', 'v3', 'x4', 'y4', 'z4', 'v4', 'x5', 'y5',
             'z5', 'v5', 'x6', 'y6', 'z6', 'v6', 'x7', 'y7', 'z7', 'v7', 'x8', 'y8', 'z8', 'v8', 'x9', 'y9', 'z9', 'v9',
             'x10', 'y10', 'z10', 'v10', 'x11', 'y11', 'z11', 'v11', 'x12', 'y12', 'z12', 'v12', 'x13', 'y13', 'z13',
             'v13', 'x14', 'y14', 'z14', 'v14', 'x15', 'y15', 'z15', 'v15', 'x16', 'y16', 'z16', 'v16', 'x17', 'y17',
             'z17', 'v17', 'x18', 'y18', 'z18', 'v18', 'x19', 'y19', 'z19', 'v19', 'x20', 'y20', 'z20', 'v20', 'x21',
             'y21', 'z21', 'v21', 'x22', 'y22', 'z22', 'v22', 'x23', 'y23', 'z23', 'v23', 'x24', 'y24', 'z24', 'v24',
             'x25', 'y25', 'z25', 'v25', 'x26', 'y26', 'z26', 'v26', 'x27', 'y27', 'z27', 'v27', 'x28', 'y28', 'z28',
             'v28', 'x29', 'y29', 'z29', 'v29', 'x30', 'y30', 'z30', 'v30', 'x31', 'y31', 'z31', 'v31', 'x32', 'y32',
             'z32', 'v32', 'x33', 'y33', 'z33', 'v33']
window = tk.Tk()
window.geometry("660x500")
window.title("OpenCV Pose")
ck.set_appearance_mode("dark")
big_frame = ttk.Frame(window)
big_frame.pack(fill="both", expand=True)
style = ttk.Style(window)
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")
frame = tk.Frame(height=480, width=640)
frame.place(x=10, y=10)
lmain = tk.Label(frame)
lmain.place(x=0, y=0)
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
cap = cv2.VideoCapture(0)

def detect():
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5),
        mp_drawing.DrawingSpec(color=(255,102,0), thickness=5, circle_radius = 10))

    img = image[:, :640, :]
    imgarr = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(imgarr)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, detect)

detect()
window.mainloop()