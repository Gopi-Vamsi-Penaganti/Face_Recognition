import cv2
import multiprocessing


def detect_faces(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
    )
    return faces


def draw_boxes(faces, frame, frame_number):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Write the frame number on the frame
    cv2.putText(frame, f"Frame: {frame_number}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame


def worker(input_queue, output_queue):
    frame_number = 0
    while True:
        # Get the frame from the input queue
        frame = input_queue.get()

        # Detect faces in the current frame
        faces = detect_faces(frame)

        # Draw bounding boxes around the detected faces and update the frame number
        frame = draw_boxes(faces, frame, frame_number)
        frame_number += 1
        print(frame_number)

        # Put the processed frame into the output queue
        output_queue.put(frame)


if __name__ == '__main__':
    # Initialize the video capture object
    video_capture = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # Initialize the queues
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    # Create and start the worker processes
    num_processes = 3
    pool = multiprocessing.Pool(num_processes, worker, (input_queue, output_queue))

    # Start the video capturing loop
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Put the raw frame into the input queue
        input_queue.put(frame)

        # Get the processed frame from the output queue and display it
        processed_frame = output_queue.get()
        cv2.imshow('Video', processed_frame)

        # Write the frame to the output video file
        out.write(processed_frame)

        # Exit the program if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release the video capture and video writer objects
    video_capture.release()
    out.release()

    # Terminate the worker processes
    pool.terminate()

    # Destroy all windows
    cv2.destroyAllWindows()


    