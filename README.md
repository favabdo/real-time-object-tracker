# **Real-Time Object Tracker**

A simple real-time object tracking application using OpenCV's CSRT tracker.  
Allows a user to select an object via webcam and tracks it live with a bounding box.





##  **Description**

The task to submit to Eyego
•	Allow a user to select an object in the first frame using a bounding box.
•	Track the selected object in real time as it moves.
•	Display the tracking results in a live video feed.

This project addresses the task of building a real-time object tracker that:
o	Opens your webcam.
o	Lets you select an object (ROI) in the first frame.
o	Tracks that object in real time as it moves.

I choose the **CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)** algorithm because:
	It is well-suited for single-object tracking** scenarios.
	Provides a good balance between tracking accuracy and processing speed**.



---
## 📍 **Usage Flow**:

- The camera view will open.
- Press (S ) to pause and enable ROI selection.
- Draw a bounding box around the object and  ENTER.
- Watch the object tracking frame-by-frame—press R to (reselect ROI or lose the tracking)  
-- Press (C) to Cancel ROI selection.
- Press (Esc) any time to Quit



## 🎥 **Demo Video**

Watch the tracker in action
Watch the demo :[]







