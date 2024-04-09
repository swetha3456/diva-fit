from flask import Flask, render_template, session, url_for, redirect, request, flash
from dbfunctions import *
from flask_socketio import SocketIO
import cv2
import threading
import exercise_fns
import base64
import numpy as np

app = Flask(__name__)
app.secret_key = b"030a8ee0eb274b3e7fd9db490b0fd6a532b1fa1f1fd6825c5852c7363358c4b6"
socketio = SocketIO(app)

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("userhome.html")

@app.route("/calendar")
def calendar():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("calendar.html")

@app.route("/exercise")
def exercise():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("exercises.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if authenticate_user(request.form["username"], request.form["logpass"]):
            session["username"] = request.form["username"]
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials")

    return render_template("login.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        context = {
            "username" : request.form["username"],
            "password" : request.form["logpass"],
            "age" : int(request.form["Age"]),
            "weight" : float(request.form["weight"]),
            "goals" : request.form["goals"],
            "period_duration" : request.form["duration"],
            "conditions" : request.form["conditions"],
            "date" : request.form["period-date"],
            "cycle_length" : request.form["cycle-length"],
            "difficulty" : request.form["difficulty"]
        }

        register_user(context)
        return redirect(url_for("home"))

    return render_template("signin.html")

which_exercise = None

@app.route('/exercise/curl_count')
def exercise_curl():
    curl_thread = threading.Thread(target=curl_count)
    curl_thread.start()
    return render_template('curl_exercise.html')

@app.route('/exercise/high_knees')
def exercise_high_knees():
    high_knees_thread = threading.Thread(target=high_knee_count)
    high_knees_thread.start()
    return render_template('high_knee_exercise.html')


def curl_count():
    counter = 0
    number_of_reps = 5
    cap = cv2.VideoCapture(0)
    stage = None
    while counter < number_of_reps:
        ret, frame = cap.read()

        if not(ret):
            break
        image, counter, stage = exercise_fns.count_curl(frame, counter, number_of_reps, stage)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        # Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', image)
        frame_bytes = base64.b64encode(buffer)


        # Emit the frame to the frontend
        socketio.emit('video_frame', {'image': frame_bytes.decode('utf-8')})

    ret, frame = cap.read()
    
    image = np.zeros((500, 500, 3), np.uint8)

    cv2.putText(image, str(counter) + '/' + str(number_of_reps), 
            (10,60), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    

    cv2.putText(image, 'Well done!!', 
            (100,200), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    

    # Convert the frame to JPEG format
    _, buffer = cv2.imencode('.jpg', image)
    frame_bytes = base64.b64encode(buffer)


    # Emit the frame to the frontend
    socketio.emit('video_frame', {'image': frame_bytes.decode('utf-8')})
    
    

    cap.release()
    cv2.destroyAllWindows()


def high_knee_count():
    counter = 0
    number_of_reps = 5
    cap = cv2.VideoCapture(0)
    stage = None

    frame_number = 0
    prev_rep_frame = 0
    while counter < number_of_reps:
        ret, frame = cap.read()

        if not(ret):
            break
        image, counter, stage, frame_number, prev_rep_frame = exercise_fns.count_high_knees(frame, counter, number_of_reps, stage, frame_number, prev_rep_frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        # Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', image)
        frame_bytes = base64.b64encode(buffer)


        # Emit the frame to the frontend
        socketio.emit('video_frame', {'image': frame_bytes.decode('utf-8')})
        frame_number += 1

    ret, frame = cap.read()
    
    image = np.zeros((500, 500, 3), np.uint8)

    cv2.putText(image, str(counter) + '/' + str(number_of_reps), 
            (10,60), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    

    cv2.putText(image, 'Well done!!', 
            (100,200), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    

    # Convert the frame to JPEG format
    _, buffer = cv2.imencode('.jpg', image)
    frame_bytes = base64.b64encode(buffer)


    # Emit the frame to the frontend
    socketio.emit('video_frame', {'image': frame_bytes.decode('utf-8')})
        
    

    cap.release()
    cv2.destroyAllWindows()




# SocketIO event handler for connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')


if __name__ == '__main__':
    socketio.run(app, debug=True)
