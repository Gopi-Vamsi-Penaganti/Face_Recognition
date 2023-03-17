# Real-time Face Detection with OpenCV and Multiprocessing
This is a Python script that performs real-time face detection using OpenCV and multiprocessing. The script uses *Haar cascades* for detecting faces and draws bounding boxes around the detected faces.

## Requirements
* Python 3.x
* OpenCV 4.x
* NumPy
* A webcam or video file

## Installation
Clone the repository: [git clone](https://github.com/your-username/real-time-face-detection.git).

Change into the project directory: 
```
cd real-time-face-detection
```
Install the required dependencies: 
```
pip install -r requirements.txt
```
You can install these packages by running the following command:
```
pip install -r requirements.txt
```
## Usage
To run the script, use the following command:

```
python face_detection.py
```

This will start the script, which will capture video from your default camera and display it on the screen with bounding boxes around any detected faces. The output video will also be saved to a file named "output.avi" in the same directory as the script.

To exit the script, press the "**q**" key on your keyboard.

## Options
You can change the number of worker processes used for face detection by editing the num_processes variable in the **if __name__ == '__main__':** block.

License
This script is licensed under the *MIT License*. 
