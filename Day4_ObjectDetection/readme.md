# Motion Detection Program using OpenCV

This Python script implements a basic motion detection system using OpenCV. It continuously captures frames from a webcam, identifies moving objects, and displays a bounding box around them.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- imutils (`imutils`)

## Libraries
The script utilizes the following libraries:

* OpenCV (cv2): For computer vision tasks like image processing and video capturing.
* Time (time): To introduce a delay between frames for smoother processing.
* imutils (imutils): A utility library for image processing tasks, used for resizing images in this script.

You can install the required libraries using pip:

```bash
pip install opencv-python imutils
```
## How to Run

1. Make sure your webcam is connected to your computer.
2. Run the following command in your terminal to start the program:
```bash
python cameraObjDetection_final.py
```
3. Press q to exit the program.

## Notes
- The program calculates the absolute difference between the first frame and the current frame to detect motion.
- It then applies a Gaussian blur and thresholding to the difference image to reduce noise and highlight the moving objects.
- If the area of the contour of the moving object is greater than a predefined threshold, it considers it as a moving object and draws a rectangle around it.


## Code Breakdown

1. **Import Libraries:**
   - The script begins by importing the necessary libraries (`cv2`, `time`, and `imutils`).

2. **Camera Setup:**
   - `cam = cv2.VideoCapture(0)`: Initializes a video capture object using camera ID 0 (default camera).
   - `time.sleep(1)`: Introduces a one-second delay to allow the camera to warm up.

3. **Variables:**
   - `firstFrame`: Stores the first captured frame for background comparison. Initialized as `None` initially.
   - `area`: Defines the minimum area threshold for considering a contour as a moving object.

4. **Main Loop:**
   - The `while True` loop continuously captures frames and processes them for motion detection.

5. **Frame Capture:**
   - `_, img = cam.read()`: Reads a frame from the camera and discards the frame status flag (`_`).

6. **Text Overlay:**
   - `text = "Normal"`: Initializes a variable `text` to display the current status ("Normal" or "Moving Object detected").

7. **Image Preprocessing:**
   - `img = imutils.resize(img, width=1000)`: Resizes the captured frame to a width of 1000 pixels using the `imutils` library.
   - `grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`: Converts the frame from BGR (Blue, Green, Red) color space to grayscale.
   - `gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)`: Applies Gaussian blurring to the grayscale image with a kernel size of (21, 21) for noise reduction.

8. **Background Initialization:**
   - `if firstFrame is None:`: Checks if the `firstFrame` has been captured yet.
     - `firstFrame = gaussianImg`: If `firstFrame` is None, it captures the current frame as the background for comparison.
     - `continue`: Skips to the next iteration of the loop to avoid processing on the first frame.

9. **Motion Detection:**
   - `imgDiff = cv2.absdiff(firstFrame, gaussianImg)`: Calculates the absolute difference between the current frame and the background frame, highlighting areas of change (potential motion).

10. **Thresholding:**
- `threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]`: Applies binary thresholding to the difference image. Pixels with a difference greater than 25 are set to white (255), and the rest are set to black (0). This creates a binary image highlighting potential motion regions.

11. **Contour Detection:**
   - `threshImg = cv2.dilate(threshImg, None, iterations=2)`: Applies dilation to the thresholded image to fill in small holes and improve object detection. You can experiment with erosion for the opposite effect.
   - `cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)`: Finds contours in the thresholded image. Contours represent the boundaries of connected white regions.
   - `cnts = imutils.grab_contours(cnts)`: Grabs the external contours from the `cnts` list using the `imutils` library.

12. **Object Detection:**
   - `for c in cnts:`: Iterates through the detected contours.
     - `if cv2.contourArea(c) < area:`: Filters out small contours (noise) by checking if their area is less than the defined `area` threshold.
     - `(x, y, w, h) = cv2.boundingRect(c)`: If the contour area is significant, calculates the bounding rectangle coordinates of the contour (`x`, `y`, `w`, and `h`).
     - `cv2.rectangle(img, (x, y), (x + w, y + h