# Face Detection Program

This program uses the OpenCV library to perform real-time face detection using the Haar cascade classifier.

## Requirements
- Python 3.x
- OpenCV library

## Usage
1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install OpenCV library using pip:

    ```bash
    pip install opencv-python
    ```
3. Download the `haarcascade_frontalface_default.xml` file from the OpenCV GitHub repository or use the provided file.
4. Run the program by executing the following command:
   ```bash
    python FaceDetection_program.py
    ```
5. The program will open a window and start detecting faces in the live video feed from your default camera.
6. Press "Esc" to exit the program.

## Code Breakdown

1. **Import Libraries:**
   - The script begins by importing the necessary libraries (`cv2`).

2.  **Haar Cascade Classifier:**
    ```python
    alg = "haarcascade_frontalface_default.xml"
    haar_cascade = cv2.CascadeClassifier(alg)
    ```
- `alg`: This variable stores the path to the Haar cascade classifier XML file (`haarcascade_frontalface_default.xml`). This file contains pre-trained data for detecting frontal faces.
- `haar_cascade`: This line creates a CascadeClassifier object using the specified XML file. This object is used for face detection in the following steps.


3. **Camera Capture:**
    ```python
    cam = cv2.VideoCapture(0)
    ```
- This line Initializes a video capture object using camera ID 0 (default camera).
- This object is used to capture video frames from the camera.

4. **Main Loop:**
    ```python
    while True:
        _,img = cam.read()
        cv2.imshow("FaceDetection",img)
        key = cv2.waitKey(10)
        if key == 27:
        break
    cam.release()
    cv2.destroyAllWindows()
    ```
- The while True loop continuously captures video frames.
- `_,img = cam.read()`: This line reads a frame from the camera. The `_` discards the frame return value (usually a timestamp) and stores the actual image data in the `img` variable.
- `cv2.imshow("FaceDetection",img)`: This line displays the captured image with the title "FaceDetection" in a window.
- `key = cv2.waitKey(10)`: This line waits for 10 milliseconds for a key press. The function returns the pressed key code if a key is pressed within the specified time, otherwise it returns -1.
- if `key == 27`: This condition checks if the 'Esc' key (key code 27) is pressed. If so, the loop breaks, terminating the program.

5. **Image Processing and Face Detection:**
    ```python
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),5)
    ```

-   `grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)`: This line converts the captured image (which is in BGR format) to grayscale format. The Haar cascade classifier typically works better with grayscale images.
- `face = haar_cascade.detectMultiScale(grayImg,1.3,4)`: This line performs the actual face detection. The detectMultiScale method of the CascadeClassifier object takes the grayscale image and two parameters:
  - `scaleFactor`: This parameter specifies how much the image size is reduced at each image scale. A value of 1.3 is commonly used.
  - `minNeighbors`: This parameter specifies the minimum number of neighbors required to return a candidate bounding box. A higher value reduces false positives but might miss some faces. The method returns a list of bounding boxes (x, y, width, height) for the detected faces.
- The for loop iterates through the list of detected faces:
  - `(x,y,w,h)`: These variables represent the coordinates (x, y) of the top-left corner, width, and height of the bounding box for a detected face.
  - `cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),5)`: This line draws a blue rectangle (color: (255, 255, 0)) with a thickness of 5 pixels around the detected face on the original color image (`img

