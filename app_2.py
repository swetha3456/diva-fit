from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
import base64

app = Flask(__name__)
socketio = SocketIO(app)

# Function to capture video and emit frames to the frontend
def curl_count():
    cap = cv2.VideoCapture(0)
    counter = 0
    number_of_reps = 20
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        
        # Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = base64.b64encode(buffer)

        # Emit the frame to the frontend
        socketio.emit('video_frame', {'image': frame_bytes.decode('utf-8')})

    cap.release()

# Route to render the video streaming page at /exercises
@app.route('/exercises/curl_count')
def exercises():
    return render_template('index_video.html')

# SocketIO event handler for connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.start_background_task(target=curl_count)

if __name__ == '__main__':
    socketio.run(app, debug=True)
