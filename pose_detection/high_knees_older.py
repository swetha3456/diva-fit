import cv2
import mediapipe as mp
import numpy as np
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

not_live = 1

if not_live:
    video_path = '/home/dyuthi/Videos/Screencasts/knee_jumps.webm'
else:
    video_path = 'high_knees_live.webm'


cap = cv2.VideoCapture(video_path)


landmarks = []
csv_data = []
frame_number = 0
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    max_knee_left_coords, min_knee_left_coords = -1, 1000
    dirn = -1
    prev = 0
    change_count = 0
    reps = 0
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
          # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        
        if results.pose_landmarks:
            landmarks.append(results.pose_landmarks.landmark)
            current = round(abs(landmarks[-1][mp_pose.PoseLandmark.LEFT_KNEE.value].z), 2)
        


            if prev != 0 and dirn == -1 and frame_number == 4:
                dirn = 1 if current > prev else 0
            elif prev != 0:
                if current > prev and dirn == 0:
                    change_count += 1
                elif current < prev and dirn == 1:
                    change_count += 1
                
                if change_count == 2 and (current < 0.2 or current > 0.5):
                    #print("************************rep here*******************")
                    reps += 1
                    dirn = int(not(dirn))

            print(current)
            prev = current

            if frame_number % 20 == 0:
                if max_knee_left_coords - min_knee_left_coords < 0.5:
                    print('*****************LAZY********************')
                max_knee_left_coords = min_knee_left_coords = current
            else:        
                max_knee_left_coords = max(current, max_knee_left_coords)
                min_knee_left_coords = min(current, min_knee_left_coords)

        font = cv2.FONT_HERSHEY_SIMPLEX 
  
        # Use putText() method for 
        # inserting text on video 
        cv2.putText(image,  
                    str(reps),  
                    (50, 50),  
                    font, 1,  
                    (0, 255, 255),  
                    2,  
                    cv2.LINE_4) 
        
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        
        if cv2.waitKey(5) & 0xFF == 27:
            break
        frame_number += 1

cap.release()
cv2.destroyAllWindows()

# import numpy as np

# # Initialize lists to store coordinates
# left_hip_coords = []
# right_hip_coords = []
# left_knee_coords = []
# right_knee_coords = []
# left_ankle_coords = []
# right_ankle_coords = []

# # Extract coordinates for each frame
# for frame_landmarks in landmarks:
#     # left_hip_coords.append([
#     #     frame_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
#     #     frame_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
#     #     frame_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z
#     # ])
#     # right_hip_coords.append([
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z
#     # ])
#     left_knee_coords.append([
#         frame_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
#         frame_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
#         frame_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z
#     ])
#     # right_knee_coords.append([
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z
#     # ])
#     left_ankle_coords.append([
#         frame_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
#         frame_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
#         frame_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z
#     ])
#     # right_ankle_coords.append([
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
#     #     frame_landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z
#     # ])

# 0.5801963210105896 - knee
# 0.6330416426062584 - ankle
