from flask import Flask, render_template, session, url_for, redirect, request, flash
from dbfunctions import *
from recommendations import get_recommendation
from predict import predict
from flask_socketio import SocketIO
import cv2
import threading
import exercise_fns
import base64
import numpy as np
from transformers import BertTokenizer, BertForQuestionAnswering
import torch
import nltk

nltk.download('punkt')
nltk.download('stopwords')


# Load the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')


model_load_path = 'model.pt'

# Load the model
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')  # Instantiate your model class
model.load_state_dict(torch.load(model_load_path))

# Ensure the model is in evaluation mode
model.eval()


app = Flask(__name__)
app.secret_key = b"030a8ee0eb274b3e7fd9db490b0fd6a532b1fa1f1fd6825c5852c7363358c4b6"
socketio = SocketIO(app)

exercise_thread = None
current_exercise = None


@app.route("/")
def about():
    return render_template("about.html")

@app.route("/home", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form["question"]
        answer = predict(question, model)
    else:
        if "username" not in session:
            return redirect(url_for("login"))
        question = answer = ""
    
    pie_chart_info = days_left(session["username"])
    age_group, phase, goal = get_details(session["username"])

    context = {
        "recommendation" : get_recommendation(phase, age_group, goal),
        "num_days_left" : pie_chart_info[0],
        "percentage" : pie_chart_info[1]
    }

    return render_template("userhome.html", context=context, question=question, answer=answer)

@app.route("/vaccine")
def vaccine():
    age_group, _, _ = get_details(session['username'])
    if age_group == 'adult':
        return render_template("adult_vaccine.html")
    elif age_group == 'teen':
        return render_template("teen_vaccine.html")
    elif age_group == 'old' :
        return render_template("old_vaccine.html")   

@app.route("/health")
def health():
    age_group, _, _ = get_details(session['username'])
    if age_group == 'adult':
        return render_template("adult_health.html")
    elif age_group == 'teen':
        return render_template("teen_health.html")
    elif age_group == 'old' :
        return render_template("old_health.html")   


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

# @app.route('/exercise/curl_count')
# def exercise_curl():
#     curl_thread = threading.Thread(target=curl_count)
#     curl_thread.start()
#     return render_template('curl_exercise.html')

# @app.route('/exercise/high_knees')
# def exercise_high_knees():
#     high_knees_thread = threading.Thread(target=high_knee_count)
#     high_knees_thread.start()
#     return render_template('high_knee_exercise.html')



# # Route for curl exercise
# @app.route('/exercise/curl_count')
# def exercise_curl():
#     global exercise_thread, current_exercise

#     # Stop the previous exercise thread if running
#     if exercise_thread and exercise_thread.is_alive():
#         exercise_thread.join()

#     # Start new thread for curl exercise
#     exercise_thread = threading.Thread(target=curl_count)
#     exercise_thread.start()
#     current_exercise = 'curl_count'

#     return render_template('curl_exercise.html')

# # Route for high knees exercise
# @app.route('/exercise/high_knees')
# def exercise_high_knees():
#     global exercise_thread, current_exercise

#     # Stop the previous exercise thread if running
#     if exercise_thread and exercise_thread.is_alive():
#         exercise_thread.join()

#     # Start new thread for high knees exercise
#     exercise_thread = threading.Thread(target=high_knee_count)
#     exercise_thread.start()
#     current_exercise = 'high_knees'

#     return render_template('high_knee_exercise.html')

# # Route for high knees exercise
# @app.route('/exercise/toe_touch')
# def exercise_toe_touch():
#     global exercise_thread, current_exercise

#     # Stop the previous exercise thread if running
#     if exercise_thread and exercise_thread.is_alive():
#         exercise_thread.join()

#     # Start new thread for high knees exercise
#     exercise_thread = threading.Thread(target=toe_touch_count)
#     exercise_thread.start()
#     current_exercise = 'toe touch'

#     return render_template('toe_touch_exercise.html')

exercise_thread = None
current_exercise = None
cap = None  # Global variable to hold the camera capture object

def start_exercise_thread(target_func):
    global exercise_thread, cap
    if cap:
        cap.release()  # Release the camera capture object if it exists
        cv2.destroyAllWindows()  # Close all OpenCV windows
    if exercise_thread and exercise_thread.is_alive():
        exercise_thread.join()
    exercise_thread = threading.Thread(target=target_func)
    exercise_thread.start()

@app.route('/exercise/curl_count')
def exercise_curl():
    start_exercise_thread(curl_count)
    return render_template('curl_exercise.html')

@app.route('/exercise/high_knees')
def exercise_high_knees():
    start_exercise_thread(high_knee_count)
    return render_template('high_knee_exercise.html')

@app.route('/exercise/toe_touch')
def exercise_toe_touch():
    start_exercise_thread(toe_touch_count)
    return render_template('toe_touch_exercise.html')


def curl_count():
    counter = 0
    number_of_reps = 5
    global cap
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
    global cap
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


def toe_touch_count():
    counter = 0
    number_of_reps = 5
    global cap
    cap = cv2.VideoCapture(0)
    stage = None
    while counter < number_of_reps:
        ret, frame = cap.read()

        if not(ret):
            break
        image, counter, stage = exercise_fns.count_toe_touch(frame, counter, number_of_reps, stage)

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




# SocketIO event handler for connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')


if __name__ == '__main__':
    socketio.run(app, debug=True)
