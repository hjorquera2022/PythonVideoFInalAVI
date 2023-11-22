import os
import cv2

# Get the path to the directory
directory = "C:\\Users\\hjorquera\\Desktop\\DAV\\VIDEOS.30fps\\ch3\\2020"
outputFile = "C:\\Users\\hjorquera\\Desktop\DAV\\\VIDEOS.30fps\ch3\\output_ch3.2020.avi"

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate over the files
for file in files:

    # Check if the file is an .avi file
    if file.endswith(".avi"):

        # Get the path to the file
        file_path = os.path.join(directory, file)

        # Open the file
        cap = cv2.VideoCapture(file_path)

        # Check if the file is opened successfully
        if not cap.isOpened():
            print("Error opening file")
            exit(1)

        # Get the frame width and height
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Create a VideoWriter object
        out = cv2.VideoWriter(outputFile, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

        # Write the frames to the output file
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            print(file)
            out.write(frame)

        # Close the output file
        out.release()

        # Close the video file
        cap.release()

# Destroy the window
cv2.destroyAllWindows()