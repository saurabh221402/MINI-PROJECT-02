# VIRTUAL MOUSE PROJECT

In this project we will be using the live feed coming from the webcam to create a virtual mouse using hand tracking.

# OBJECTIVE

The main objective of the proposed AI virtual mouse system is to develop an
alternative to the regular and traditional mouse system to perform and control the
mouse functions, and this can be achieved with the help of a web camera that
captures the hand gestures and hand tip and then processes these frames to perform
the particular mouse function such as left click, right click .
To eliminate the need for a physical mouse, leveraging computer vision and motion
sensing for touchless and immersive human-computer interaction.

# MODULES REQUIREMENTS
* cv2(openCV)
* Mediapipe
* autopy

# OpenCV:

OpenCV is a huge open-source library for computer vision, machine learning, and image processing. 
OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process 
images and videos to identify objects, faces, or even the handwriting of a human.
It can be installed using "pip install opencv-python"

# Mediapipe:

MediaPipe is a framework for building multimodal (eg. video, audio, any time series data), 
cross platform (i.e Android, iOS, web, edge devices) applied ML pipelines.

It can be installed using "pip install mediapipe"

# Autopy:

AutoPy is a simple, cross-platform GUI automation library for Python. It includes functions for controlling
the keyboard and mouse, finding colors and bitmaps on-screen, and displaying alerts.

It can be installed using "pip install autopy"


# METHODOLOGY

 
1. The Camera Used in the AI Virtual Mouse System.

The proposed AI virtual mouse system is based on the frames that have been captured
by the webcam in a laptop or PC. By using the Python computer vision library
OpenCV, the video capture object is created and the web camera will start capturing
video. The web camera captures and passes the frames to the AI virtual system.

2. CapturingtheVideoandProcessing
   
The AIvirtualmouse system uses the webcam where each frame is captured till the
termination of the program. The video frames are processed from BGR to RGB color
space to find the hands in the video frame by frame as shown in the following code:
def findHands(self, img, draw True):
imgRGB cv2.cvtColor(img, cv2.COLOR_BGR2RGB) self.results
self.hands.process(imgRGB)

3. (Virtual Screen Matching) Rectangular Region for Moving through the Window
   
The AI virtual mouse system makes use of the transformational algorithm, and it
converts the co- ordinates of fingertip from the webcam screen to the computer
window full screen for controlling the mouse. When the hands are detected and when
we find which finger is up for performing the specific mouse function, a rect- angular
box is drawn with respect to the computer window in the webcam region where we
move throughout the window using the mouse cursor .

4. Detecting Which Finger Is Up and Performing the ParticularMouseFunction.
   
In this stage, we are detecting which finger is up using the tip Id of the respective
finger that we found using the MediaPipe and the respective co-ordinates of the
fingers that are up, and according to that, the particular mouse
function is performed.

5. Mouse Functions Depending on the Hand Gestures and Hand Tip Detection Using Computer Vision in this project

* For the Mouse Cursor Moving around the
Computer Window. If the index finger is up with tip Id 1 is up, the mouse cursor is made to move around the
window of the computer using the AutoPy package of Python.

* For the Mouse to Perform Left Button Click. If both the index finger with tip Id 1 and the middle
finger with tip Id 2 are up and the distance between thetwo fingers is lesser than 30px, the computer is made to
perform the left mouse button click using the Autopy.

* For the Mouse to Perform Right Button Click. If both the index finger with tip Id 1 and the pinky finger
with tip Id 4 are up the computer is made to perform the right mouse button click using the Autopy Python
package.


# NOTE

I faced alot of dependency issues throughout this project. Some of the issues and their solutions are as follows:

* autopy not installing: This is because autopy currently doesn't support Python versions above 3.8
* webcam not opening: It was a bug in mediapipe and was fixed in latest python versions
  Hence, inorder for the project to run smoothly, you need to degrade the Python version to 3.8

