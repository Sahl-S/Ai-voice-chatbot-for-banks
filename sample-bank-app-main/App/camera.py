
import cv2
from deepface import DeepFace
import pandas as pd
import os
import numpy as np
import shutil
import json
from pyzbar.pyzbar import decode
import databases
import tkinter as tk
from tkinter import ttk
import random
import string





def imgcapt():

    # Open the default camera (device index 0)
    cap = cv2.VideoCapture(0)
    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Unable to open the camera")
        exit()
    # Capture an image from the camera
    ret, frame = cap.read()
    # Check if the image was captured successfully
    if not ret:
        print("Unable to capture image")
        exit()

    # Save the image to a file

    cv2.imwrite("camcaptured\image.jpg", frame)

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    print("Image saved as image")

import cv2
import os
import random
import string

def facecapt():
    # Open the default camera (device index 0)
    cap = cv2.VideoCapture(0)
    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Unable to open the camera")
        exit()
    random_folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Specify the path to save images
    save_path = "newfacecaptured/" + random_folder_name + "/"

    # Create the directory to store captured images
    os.makedirs(save_path, exist_ok=True)
    # Capture an image from the camera
    for i in range(15):
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Save the image to a file
        file_name = f"captured_image_{i}.jpg"
        file_path = save_path + file_name
        cv2.imwrite(file_path, frame)
        if not ret:
            print("Unable to capture image")
            exit()

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    print("Image saved",)
    return{"Foldername":random_folder_name}
'''    
    #below code is for single img
    result = DeepFace.verify(img1_path="camdb\\jmr\\1.jpg", img2_path="camdb\\jmr\\me.jpg", detector_backend='mtcnn', model_name="Facenet")
    print(json.dumps(result, indent=2))
'''

#face recognition from db
def facerecog():
    try:
        dfs = DeepFace.find(img_path = "camcaptured\\image.jpg", db_path = "camdb", detector_backend='mtcnn', model_name="Facenet")
        print(dfs)
        facial_fail=0
        return facial_fail



    except ValueError as e:
        print("Error:",e)
        print("Error occured")
        facial_fail=1

        #pop up window
        def popupmsg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup, text=msg, font=("arial", 20, "bold"))
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()
        if facial_fail==1:
            popupmsg("Face not detected")
        return facial_fail

    print("facial_fail is ",facial_fail)





    #copy the new img to db
    filename= "text.txt"
    with open(filename, 'r+') as imglog:
        dfs_liststr=str(dfs)
        imglog.write(dfs_liststr)

    # Read the text file into a DataFrame
    df = pd.read_csv('text.txt', header=None)

    # Extract the paths that match the criteria
    paths = df[0].str.contains('camdb\\\\[a-zA-Z0-9_]+\\\\').unique()

    # Use np.where to extract the paths
    paths = np.where(df[0].str.contains('camdb\\\\[a-zA-Z0-9_]+\\\\'), df[0], None)
    paths = np.unique(paths[paths != None])

    # Extract the directory path using os.path.dirname
    paths = [os.path.dirname(path) for path in paths]

    # Remove duplicates
    paths = list(set(paths))

    # Print the paths
    print(paths)
    path=paths[0]
    path = path.strip("1   ")
    path = path.strip("0   ")
    print(path)

    #copy image
    source_file = "camcaptured\\image.jpg"
    # Remove duplicates from the list of file paths
    dest_fold = path
    shutil.copy(source_file,dest_fold)

    check_db_uname=path.strip("camdb\\ ")

    print(check_db_uname)
    filename = "dbname.txt"
    with open(filename, 'r+') as dbname:
        dbname.write(check_db_uname)





def textcapt():
    '''
    print(Qr_img_to_text("textmod/adhaardemo.PNG"))

    # Open the default camera (device index 0)
    cap = cv2.VideoCapture(0)
    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Unable to open the camera")
        exit()
    # Capture an image from the camera
    ret, frame = cap.read()
    # Check if the image was captured successfully
    if not ret:
        print("Unable to capture image")
        exit()

    # Save the image to a file

    cv2.imwrite("temp\image.jpg", frame)

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    print("Image saved as image")
    '''
    '''
    # Load the image
    img = Image.open('textmod/bashi.jpg')

    # Convert the image to a numpy array
    img_array = np.asarray(img)

    # Create a reader object
    reader = Reader(['en'])

    # Read the text from the image
    test = reader.readtext(img_array)

    # Print the recognized text
    print(test)

    filename = "textcap.txt"
    with open(filename,'r+') as txtlog:
        txtcap_liststr = str(test)
        txtlog.write(txtcap_liststr)
    '''
    # Load the image
    image_path='QR.jpg'
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # QR code detection
    detector = cv2.QRCodeDetector()
    decoded_objects = decode(gray)

    if decoded_objects:
        print("QR Code detected successfully.")
        # Print QR code data
        for obj in decoded_objects:
            QRdata = obj.data.decode('utf-8')
            #print("QR Code Data:", QRdata)
    else:
        print("No QR Code found in the image.")
    filename = "textcap.txt"
    #creating text file
    #with open(filename, 'r+') as txtlog:
        #txtcap_liststr = str(QRdata)
        #txtlog.write(txtcap_liststr)
    # Read data from the text file
    with open(filename, "r") as file:
        data = file.readlines()
    # Initialize variables
    Name = ""
    DOB = ""
    Gender = ""
    Mobile_No = ""
    Email = ""
    Father_Name = ""
    Address = ""

    # Iterate through each line and extract information
    for line in data:
        if "Name:" in line:
            Name = line.split(":")[1].strip()
        elif "DOB:" in line:
            DOB = line.split(":")[1].strip()
        elif "Gender:" in line:
            Gender = line.split(":")[1].strip()
        elif "Mobile No:" in line:
            Mobile_No = line.split(":")[1].strip()
        elif "Email:" in line:
            Email = line.split(":")[1].strip()
        elif "Aadhar:" in line:
            Aadhar = line.split(":")[1].strip()
        elif "Address:" in line:
            Address = line.split(":")[1].strip()

    # Print the extracted information
    print("Name:", Name)
    print("DOB:", DOB)
    print("Gender:", Gender)
    print("Mobile No:", Mobile_No)
    print("Email:", Email)
    Aadhar=789456123321
    print("Aadhar No:", Aadhar)
    print("Address:", Address)

    return {
        "Name": Name,
        "DOB": DOB,
        "Gender": Gender,
        "Mobile No": Mobile_No,
        "Email": Email,
        "Aadhar No": Aadhar,
        "Address": Address
    }





#imgcapt()
#facerecog()
#textcapt()
#facecapt()
