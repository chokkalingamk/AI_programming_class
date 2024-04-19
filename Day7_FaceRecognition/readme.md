# Face Recognition Project

This project uses OpenCV for face recognition. It trains a machine learning model on a dataset of face images, and then uses this model to recognize faces in real-time video from a webcam.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy
- Os

## Dataset Creation

Before running the face recognition program, you need to create a dataset of face images. This is done with the `create_data.py` script.
It takes multiple pictures of you and saves them in separate folders within the datasets directory. Each folder is named after your desired label (e.g., "YourName").

1. Create a new folder named `datasets` in the project directory.
2. Run `create_data.py` script.
3. This script will open a webcam window. Position your face in the window and press the spacebar to capture images. Each time you press the spacebar, a new set of face images will be saved in the `datasets` folder with a unique name.
4. Repeat this process for each person you want to include in the dataset.

## Usage
1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install OpenCV library using pip:

    ```bash
    pip install opencv-python ,imutils , numpy, os, opencv-contrib-python
    ```
3. Save the `face_recognize.py` file in the same directory as the main program..
4. Run the program by executing the following command:
   ```bash
    python face_recognize.py
    ```
5. The program will open a window and start recognizing faces in the live video feed from your default camera.
6. Press "Esc" to exit the program.
   
## Code Breakdown

1. **Import Libraries:**

- `imutils:` This library provides a set of utility functions for basic image processing tasks such as resizing, translation, rotation, and displaying images. It's often used to simplify common operations in computer vision projects.
- `cv2 (OpenCV):` OpenCV  is a popular open-source library for computer vision and image processing. It provides a wide range of functions for tasks like image manipulation, object detection, face recognition, and more.
- `os:` This library provides a way to interact with the operating system. It allows you to perform various operating system-related tasks such as navigating file systems, running shell commands, and managing directories.
- `numpy:` NumPy is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. It is commonly used in scientific computing and data analysis.

2. **Setup**

- `size = 4:` Sets a variable for the size of the resized images (not used in this specific code).
- `haar_file =` 'haarcascade_frontalface_default.xml': Defines the path to the pre-trained Haar cascade classifier for face detection.
- `datasets = 'datasets':` Sets the path to the directory containing facial image datasets (one subdirectory per person).
- `print('Training...'):` Prints a message indicating the training process is about to begin.

3. **Data Preparation:**

- `(images, labels, names, id) = ([], [], {}, 0):` Initializes empty lists and a dictionary for storing training data.
- `for (subdirs, dirs, files) in os.walk(datasets):` Iterates through the datasets directory, its subdirectories, and files.
  - `for subdir in dirs:` Loops through each subdirectory (representing a person).
    - `names[id] = subdir:` Assigns the current person's name (subdirectory name) to the names dictionary with an ID key.
    - `subjectpath = os.path.join(datasets, subdir):` Constructs the complete path to the current person's subdirectory.
    - `for filename in os.listdir(subjectpath):` Loops through each file (image) within the person's subdirectory.
      - `path = subjectpath + '/' + filename:` Constructs the complete path to the image file.
      - `label = id:` Assigns the current person's ID as the label for the image.
      - `images.append(cv2.imread(path, 0)):` Reads the image in grayscale mode using cv2.imread and appends it to the images list.
      - `labels.append(int(label)):` Appends the corresponding label as an integer to the labels list.
    - `id += 1:` Increments the ID for the next person.
- `(width, height) = (130, 100):` Sets the desired width and height for resizing the images (not crucial for this code).

4. **Data Conversion and Model Training:**

- `(images, labels) = [numpy.array(lis) for lis in [images, labels]]:` Converts images and labels into NumPy arrays for efficient processing.
- `model = cv2.face.FisherFaceRecognizer_create():` Creates a FisherFace recognizer for face recognition.
- `model.train(images, labels):` Trains the FisherFace model using the prepared images and their corresponding labels.

5. **Face Detection and Recognition:**

- `face_cascade = cv2.CascadeClassifier(haar_file):` Loads the pre-trained Haar cascade classifier for face detection.
- `webcam = cv2.VideoCapture(0):` Initializes a webcam capture object for capturing video frames.
- `cnt=0:` Initializes a counter to track the number of frames where an unknown person is detected.


> The main loop `(while True)` continuously performs the following steps:

   1. ***Capture Frame:***
      - `(_, im) = webcam.read():` Captures a frame from the webcam and stores it in the im variable.

   2. ***Convert to Grayscale:***

      - `ngray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY):` Converts the captured frame to grayscale for face detection.

   3. ***Detect Faces:***

      - `faces = face_cascade.detectMultiScale(gray, 1.3, 5):` Detects faces in the grayscale frame using the cascade classifier. The parameters 1.3 and 5 control the scale factor and minimum number of neighbors, respectively, for effective face detection.

6. **Process Each Detected Face:**

- `for (x, y, w, h) in faces:`: Iterates through each detected face in the frame.

  1. ***Resize Face:***

     - `face = gray[y:y + h, x:x + w]:` Extracts the region of interest (ROI) containing the detected face from the grayscale frame.
     - `face_resize = cv2.resize(face, (width, height)):` Resizes the extracted face ROI to the desired dimensions (width, height) defined earlier (not used in this specific code, but potentially helpful for normalization).
  2. ***Prediction:***
     -    `prediction = model.predict(face_resize):` Uses the trained model to predict the most likely person corresponding to the detected face. The output prediction is a tuple containing:
     -    `prediction[0]:` Predicted person's ID (index in the names dictionary).
     -   `prediction[1]:` Confidence score of the prediction (lower score indicates higher confidence).

  3. ***Draw Recognition Results:***
  
       - `cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3):` Draws a green rectangle around the recognized face.
       - `if prediction[1]<800:`: Checks if the confidence score is below a threshold (800 in this case). A lower score suggests a more confident prediction. 
         - `cv2.putText(im, '%s - %.0f' % (names[prediction[0]], prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_COMPLEX,1,(51, 255, 255)):`
           - Retrieves the person's name from the `names` dictionary using the predicted ID.
           - Formats the output string with the predicted name (e.g., "John") and confidence score.
           - Prints the person's name and confidence score on the frame using `cv2.putText` at the top-left corner of the face rectangle.
           - Font and color are set for readability.
       - `print (names[prediction[0]]):` Prints the recognized person's name to the console.
       - `cnt=0:` Resets the counter for unknown person detection.
     - `else:`: Runs if the confidence score is above the threshold, indicating a less certain prediction.
       - `cnt+=1:` Increments the counter for unknown person detection.
       - `cv2.putText(im,'Unknown',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0)):` Prints "Unknown" on the frame at the top-left corner of the face rectangle.
       - `if(cnt>100):`: Checks if the counter reaches a threshold (100 frames). This indicates a persistent unknown person might be present.
         - `print("Unknown Person"):` Prints "Unknown Person" to the console to alert you.
         - `cv2.imwrite("input.jpg",im):` Saves a snapshot of the current frame as "input.jpg" for potential further analysis.
         - `cnt=0:` Resets the counter.

7. **Display Frame:**

 - `cv2.imshow('OpenCV', im):` Displays the processed frame containing detected and recognized faces (or "Unknown" for uncertain predictions) on a window titled "OpenCV".

8. **Handle User Input (Optional):**

- `key = cv2.waitKey(10):` Waits for 10 milliseconds for a key press. If a key is pressed within 10 milliseconds, its corresponding key code is returned in the key variable.
- `if key == 27:`: Checks if the 'Esc' key (key code 27) was pressed.
 - `break:` If 'Esc' is pressed, the loop breaks, terminating the program.

9. **Release Resources:**

- `webcam.release():` Releases the webcam capture object, freeing up resources.
- `cv2.destroyAllWindows():` Closes all OpenCV windows, including the "OpenCV" window displaying the video stream.













