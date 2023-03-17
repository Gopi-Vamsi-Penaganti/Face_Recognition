import cv2


def detect_faces(frame):
    """
    Detect faces in the given frame using Haar cascade classifier.
    :param frame: Input frame to detect faces in
    :return: List of detected faces in the format [(x1, y1, w1, h1), (x2, y2, w2, h2), ...]
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
    )
    return faces


def draw_boxes(faces, frame, frame_number, out):
    """
    Draw bounding boxes around the detected faces in the given frame and write the frame to the output video file.
    :param faces: List of detected faces in the format [(x1, y1, w1, h1), (x2, y2, w2, h2), ...]
    :param frame: Input frame to draw boxes on
    :param frame_number: The number of the current frame
    :param out: The output video file to write the frame to
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Write the frame number on the frame
    cv2.putText(frame, f"Frame: {frame_number}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Write the frame to the output video file
    out.write(frame)


if __name__ == '__main__':
    # Initialize the video capture object
    video_capture = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # Initialize frame number
    frame_number = 0

    # Start the video capturing and face detection loop
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Detect faces in the current frame
        faces = detect_faces(frame)

        # Draw bounding boxes around the detected faces and write the frame to the output video file
        draw_boxes(faces, frame, frame_number, out)

        # Increment the frame number
        frame_number += 1

        # # Exit the program if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and video writer objects
    video_capture.release()
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()

    