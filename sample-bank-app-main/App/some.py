import cv2
import tkinter as tk
import os
import random
import string
from PIL import Image, ImageTk

def capture_images_to_random_folder():
    # Create a Tkinter window
    window = tk.Tk()
    window.title('Camera View')

    # Create a camera object
    cap = cv2.VideoCapture(0)

    # Generate a random folder name
    random_folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Specify the path to save images
    save_path = "captured_images/" + random_folder_name + "/"

    # Create the directory to store captured images
    os.makedirs(save_path)

    # Create a function to capture an image
    def capture_image():
        for i in range(15):
            # Capture a frame from the camera
            ret, frame = cap.read()

            # Save the image to a file
            file_name = f"captured_image_{i}.jpg"
            file_path = save_path + file_name
            cv2.imwrite(file_path, frame)


    # Create a label to display the camera view
    label = tk.Label(window)
    label.pack()

    # Create a button to capture an image
    button = tk.Button(window, text='Capture Image', command=capture_image)
    button.pack()

    # Create a function to update the camera view
    def update_camera_view():
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to a Tkinter-compatible image
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (640, 480))
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        label.config(image=image)
        label.image = image

        # Call the function again after 33 milliseconds
        window.after(33, update_camera_view)

    # Start updating the camera view
    update_camera_view()

    # Start the Tkinter event loop
    window.mainloop()

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

# Call the function to capture images to a random folder
capture_images_to_random_folder()
