# Human-recognizer
OpenCV-Python is employed for real-time human detection in a video. Here's a concise technical overview:

Video Input: 
OpenCV is used to initialize video capture from a file.

Haar Cascade Classifier: 
A pre-trained Haar Cascade classifier for full-body detection is loaded.

Frame Processing Loop: 
Frames from the video are processed sequentially.

Object Detection: 
The Haar Cascade classifier is applied to identify human bodies.

Visual Feedback: 
Detected human bodies are marked with rectangles.

Real-time Display: 
Frames with detections are displayed continuously.

User Interaction: 
The program exits upon detecting the 'q' key press.