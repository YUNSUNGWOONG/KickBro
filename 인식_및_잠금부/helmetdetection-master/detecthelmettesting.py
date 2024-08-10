import cv2
import tkinter as tk
from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
import torch
from pathlib import Path

# YOLOv5 모델 로드
model_path = './best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

camera = cv2.VideoCapture(0)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Helmet Detection")

        # Graphics window
        self.imageFrame = Frame(self.master, width=600, height=500)
        self.imageFrame.grid(row=0, column=0, padx=10, pady=2)

        # Capture video frames
        self.lmain = Label(self.imageFrame)
        self.lmain.grid(row=0, column=0)

        # Start button
        self.start_button = Button(self.master, text="Start Live Feed", command=self.start_live_feed)
        self.start_button.grid(row=1, column=0, pady=10)

        # Helmet status labels
        self.withhelmet = Label(self.master, text="Wearing a Helmet: Unknown")
        self.withhelmet.grid(row=2, column=0)

        self.withouthelmet = Label(self.master, text="Not Wearing a Helmet: Unknown")
        self.withouthelmet.grid(row=3, column=0)

    def start_live_feed(self):
        self.show_frame()
        self.update_helmet_status()

    def show_frame(self):
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)

    def update_helmet_status(self):
        ret, frame = camera.read()
        if not ret:
            return

        results = model(frame)

        helmet_detected = False
        for detection in results.xyxy[0]:  # xyxy format for bounding boxes
            if int(detection[-1]) == 0:  # Assuming class 0 is 'helmet'
                helmet_detected = True
                
                # Draw bounding box
                xmin, ymin, xmax, ymax = map(int, detection[:4])
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                
                break

        self.withhelmet.config(text="Wearing a Helmet: Yes" if helmet_detected else "Wearing a Helmet: No")
        self.withouthelmet.config(text="Not Wearing a Helmet: Yes" if not helmet_detected else "Not Wearing a Helmet: No")

        # Convert frame to display in tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)

        self.master.after(10, self.update_helmet_status)

root = tk.Tk()

app = Window(root)

root.mainloop()
